import pandas as pd
import json
from pathlib import Path

# Leer Excel (ubicado en la raíz del repo)
params = pd.read_excel("Series.xlsx", sheet_name="Parámetros")
data   = pd.read_excel("Series.xlsx", sheet_name="Data")

# Limpiar datos
data.columns = [str(c).strip() for c in data.columns]
date_col = data.columns[0]
data[date_col] = pd.to_datetime(data[date_col]).dt.strftime("%Y-%m-%d")
data = data.dropna(how="all").fillna("null")

# Construir JSON
output = {
    "metadata": {
        "tickers": params.iloc[:, 0].tolist(),
        "names":   params.iloc[:, 1].tolist()
    },
    "dates": data[date_col].tolist(),
    "series": {}
}

for col in data.columns[1:]:
    vals = data[col].tolist()
    output["series"][col] = [None if v == "null" else float(v)
                              for v in vals]

# Guardar como JSON en data/
Path("data").mkdir(exist_ok=True)
with open("data/bloomberg.json", "w") as f:
    json.dump(output, f, separators=(",", ":"))

print(f"OK bloomberg.json generado: {len(output['dates'])} fechas, "
      f"{len(output['series'])} series")
print("Tickers:", output['metadata']['tickers'])
