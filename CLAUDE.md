# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Renta Fija 2026-I** is a Fixed Income course curriculum delivered as interactive HTML documents. The course covers 15 weeks of material organized into 4 thematic modules: Fundamentals, Interest Rate Risk, Credit & Derivatives, and Portfolio Management. The repository contains:

- **index.html**: Main course map with tabbed slide navigation (15 slides: 1 executive summary + 14 weekly overviews)
- **w1_onepager.html through w4_onepager.html**: Detailed one-pager documents for individual weeks
- No build process; all files are static HTML with embedded CSS and JavaScript
- Content is in Spanish (es)

## Architecture & Design

### index.html Structure

**Core Layout**: CSS Grid shell with three main regions:
- Top nav bar (`#topnav`): Tab-style week selector with smooth scrolling
- Main stage (`#stage`): Slide container with absolute positioning; slides fade and slide in/out
- Bottom nav bar (`#botnav`): Previous/Next buttons, progress indicator, slide counter

**Slide Navigation**:
- Managed by vanilla JS function `goTo(n, dir)` that:
  - Positions new slide off-screen, forces browser paint, then animates both old and new slides simultaneously
  - Uses CSS transitions (`.35s ease`) for smooth visual effect
  - Cleans up inline styles after animation completes
- Supports: tab clicks, Previous/Next buttons, timeline clicks (on summary slide), arrow keys
- The `TOTAL = 15` constant defines the number of slides; updating this requires updating nav tabs and the `LABELS` array

**One-Pager Availability**:
- Managed via `ONEPAGERS_AVAILABLE` array at the bottom of index.html
- Any week number added to this array will make its "One-pager" button clickable
- Unavailable weeks show "Próximamente" tooltip on hover
- Links are removed and disabled state applied to unavailable buttons

### One-Pager Structure (w#_onepager.html)

One-pagers use a multi-module layout with:
- Header with eyebrow, title, subtitle, and pill-style tags
- Concept cards (light background, left-border accent)
- Formula boxes (dark navy background with highlighted equations)
- Comparison strips (side-by-side grids with borders)
- Responsive grids (2–3 columns that collapse to 1 on mobile)

Math rendering uses **MathJax** (not KaTeX); configured for both inline `\(...\)` and display `\[...\]` delimiters.

### Styling System

Both files use CSS custom properties (`:root` variables) for consistent theming:
```
--navy: #061942   (dark backgrounds)
--corp: #1E3771   (accents, borders)
--mid:  #0054B0   (primary action color)
--accent: #E8A020 (special highlights, one-pagers)
--off:  #F2F2F2 or #F5F7FA (light surfaces)
--white: #FFFFFF
--text: #0D1B2A (body text)
--muted: #4A5568 or #475569 (secondary text)
```

Color-coded keyword badges in index.html:
- `.kw-blue`: Navy-background keywords (active/key)
- `.kw-outline`: Bordered keywords (related)
- `.kw-gray`: Muted keywords (supporting)

## Common Development Tasks

### View the Course Map Locally

Open `index.html` in a web browser. The navigation is fully functional in any modern browser (Chrome, Firefox, Safari, Edge). No server required.

**To test one-pager linking**: Add the week number to `ONEPAGERS_AVAILABLE` array in index.html, then click the "One-pager" button on that week's slide.

### Edit Course Content

All content is inline in the HTML files. Search for the week number (e.g., `slide-3` for Week 3) to locate the relevant section.

**Content structure for each week**:
1. Metadata tag: date, phase badge (Basic/Intermediate/Advanced)
2. Card header: week title and one-pager link
3. Executive summary paragraph
4. Keywords section (colored badge groups)
5. Bibliography section (color-coded by source)
6. Concepts list (numbered, with inline formatting)
7. Two-column grid with practical applications and course connections

### Add a New Week

To add a new week slide:

1. **Add navigation tab** in the top nav (`#topnav`):
   ```html
   <div class="nav-tab" data-slide="16">S16</div>
   ```

2. **Create slide HTML** by copying an existing week and updating:
   - Slide ID: `id="slide-16"`
   - Date range and phase badge
   - Week title and content
   - Bibliography sources
   - Concepts

3. **Update constants** in the JavaScript section:
   - Increase `TOTAL` from 15 to 16
   - Add label to `LABELS` array: `'S16 · [topic]'`

4. **Link one-pager** (when ready):
   - Create `w16_onepager.html`
   - Add `16` to `ONEPAGERS_AVAILABLE` array

### Update One-Pager Links

The one-pager buttons appear as badges with an external-link icon on each week's card. To make a one-pager available:

1. Ensure the file exists: `w#_onepager.html`
2. Add the week number to the `ONEPAGERS_AVAILABLE` array in index.html
3. The button will become clickable; unavailable weeks remain disabled with "Próximamente" tooltip

### Modify Styling

Both files use inline `<style>` blocks. Key areas:

- **Color variables**: Update `:root` custom properties at the top of the style block
- **Slide animations**: `.slide` transition timing and transform rules (default `.35s ease`)
- **Responsive breakpoints**: `@media(max-width:768px)` and `@media(max-width:900px)`
- **Typography**: Font sizes use `clamp()` for fluid scaling

### Add Mathematical Notation

- **index.html**: Uses KaTeX via CDN (lines 403–407). Delimiter syntax: `\(...\)` for inline, `\[...\]` for display.
- **One-pagers**: Use MathJax via CDN. Same delimiter syntax.

To add an equation, wrap it in the appropriate delimiters; the libraries render automatically on page load.

### Test Keyboard Navigation

- **Arrow keys**: Left/Right arrows navigate slides; Up/Down also work
- **Tab clicks**: Direct navigation to any week
- **Timeline clicks** (on summary): Jump to specific week
- **Previous/Next buttons**: Standard forward/backward navigation

## Content Guidelines

### Bibliography Format

Each week includes 5–10 sources organized by subtopic (e.g., "1. Characteristics of Fixed Income Instruments"). Use color-coded pills for authors:

- `.bib-pill.schweser`: SchweserNotes (blue)
- `.bib-pill.fabozzi`: Fabozzi (orange)
- `.bib-pill.tuckman`: Tuckman (green)
- `.bib-pill.veronesi`: Veronesi (purple)
- `.bib-pill.martellini`: Martellini (red)

Tooltips (on hover) show full reading references.

### Exam Slide (Week 8)

Week 8 is marked as an exam week (`.exam-tab` and `.exam-step` classes). The slide includes:
- Exam icon (64px emoji)
- Exam title and date range
- Topic chips
- Coverage note (e.g., "PC1 covers S1–S7")

## Git Workflow

- Files are versioned individually; no build artifacts
- `.gitignore` excludes the `backup/` directory
- Commits should reference the week(s) and content type (e.g., "Update W3 concepts and bibliography")

## Browser Compatibility

Tested on modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+). Uses:
- CSS Grid and Flexbox (no IE 11 support)
- `scrollIntoView()` with smooth behavior
- CSS custom properties
- Arrow function syntax (ES6+)

Mobile responsiveness: Tested at 768px and below (tablet) and standard mobile widths.
