---
name: Creskio
description: Dark premium tech system for a Spanish local-business acquisition agency — violet-to-emerald aurora over near-black glass.
colors:
  bg: "#03050a"
  bg-2: "#060a12"
  bg-3: "#0a1018"
  bg-4: "#0e1622"
  violet: "#8b5cf6"
  violet-deep: "#7c3aed"
  cyan: "#22d3ee"
  indigo: "#6366f1"
  emerald: "#10b981"
  whatsapp-green: "#25d366"
  whatsapp-green-deep: "#128c7e"
  text-primary: "rgba(255,255,255,.75)"
  text-secondary: "rgba(255,255,255,.58)"
  text-tertiary: "rgba(255,255,255,.52)"
  text-faint: "rgba(255,255,255,.12)"
  border-hairline: "rgba(255,255,255,.07)"
  border-hairline-strong: "rgba(255,255,255,.12)"
typography:
  display:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(2.8rem, 5vw, 4.9rem)"
    fontWeight: 800
    lineHeight: 0.97
    letterSpacing: "-.045em"
  headline:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(2rem, 4.5vw, 3.4rem)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-.04em"
  title:
    fontFamily: "'Syne', sans-serif"
    fontSize: "1.15rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "normal"
  body:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: "clamp(.95rem, 1.4vw, 1.04rem)"
    fontWeight: 300
    lineHeight: 1.9
    letterSpacing: "normal"
  label:
    fontFamily: "'Syne', sans-serif"
    fontSize: ".63rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: ".22em"
  article-h3:
    fontFamily: "'Syne', sans-serif"
    fontSize: "1.1rem"
    fontWeight: 700
    lineHeight: "normal"
    letterSpacing: "normal"
  article-body:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: ".93rem"
    fontWeight: 300
    lineHeight: 1.75
    letterSpacing: "normal"
  article-strong-label:
    fontFamily: "'Syne', sans-serif"
    fontSize: ".88rem"
    fontWeight: 700
    lineHeight: "normal"
    letterSpacing: "normal"
  article-light-label:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: ".84rem"
    fontWeight: 300
    lineHeight: 1.8
    letterSpacing: "normal"
  article-meta:
    fontFamily: "'Syne', sans-serif"
    fontSize: ".78rem"
    fontWeight: 500
    lineHeight: "normal"
    letterSpacing: "normal"
  article-micro-label:
    fontFamily: "'Syne', sans-serif"
    fontSize: ".7rem"
    fontWeight: 700
    lineHeight: "normal"
    letterSpacing: ".1em"
  article-h2:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(1.3rem, 2.5vw, 1.9rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-.02em"
  article-h1-inline:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(2.2rem, 5.5vw, 4rem)"
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: "-.04em"
  article-h1-lp-hero:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.4rem)"
    fontWeight: 800
    lineHeight: "normal"
    letterSpacing: "normal"
  article-h1-hero-art:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-.04em"
  article-h2-echo:
    fontFamily: "'Syne', sans-serif"
    fontSize: "clamp(1.5rem, 3vw, 2.2rem)"
    fontWeight: 800
    lineHeight: "normal"
    letterSpacing: "-.03em"
rounded:
  pill: "100px"
  xl: "26px"
  lg: "20px"
  md: "16px"
  sm: "12px"
spacing:
  section-y: "clamp(6rem, 10vw, 9rem)"
  section-x: "clamp(1.5rem, 5vw, 3.5rem)"
  container: "1280px"
  card-padding: "2.5rem"
  gap-md: "1.75rem"
components:
  button-primary:
    backgroundColor: "linear-gradient(135deg, {colors.violet}, {colors.violet-deep})"
    textColor: "{colors.bg}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "14px 24px"
  button-primary-hover:
    backgroundColor: "linear-gradient(135deg, {colors.violet}, {colors.violet-deep})"
    textColor: "{colors.bg}"
  button-whatsapp:
    backgroundColor: "linear-gradient(135deg, {colors.whatsapp-green}, {colors.whatsapp-green-deep})"
    textColor: "#ffffff"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "16px 34px"
  button-whatsapp-hover:
    backgroundColor: "linear-gradient(135deg, {colors.whatsapp-green}, {colors.whatsapp-green-deep})"
    textColor: "#ffffff"
  button-ghost:
    backgroundColor: "rgba(255,255,255,.04)"
    textColor: "{colors.text-secondary}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "15px 27px"
  button-ghost-hover:
    backgroundColor: "rgba(255,255,255,.08)"
    textColor: "#ffffff"
  badge-live:
    backgroundColor: "rgba(16,185,129,.07)"
    textColor: "{colors.emerald}"
    rounded: "{rounded.pill}"
    padding: "5px 14px 5px 8px"
  card-glass:
    backgroundColor: "rgba(6,10,18,.85)"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.card-padding}"
---

# Design System: Creskio

## Overview

**Creative North Star: "La Marea Digital" (The Digital Tide)**

Creskio sells a promise — "tu negocio captando clientes día y noche" — and the site is staged like a dark ocean at night where that promise is visibly happening. The near-black backdrop (`#03050a` layered through `#060a12` → `#0a1018` → `#0e1622`) reads as deep water; the violet-to-cyan-to-emerald gradient is bioluminescence moving through it — never a static flat brand color, always a diagonal or animated sweep. Nothing on the page is ever fully still: orbs drift, a progress bar flows, small dots pulse, buttons sweep with light. The tide never stops, which is the point: capture keeps happening while the visitor isn't looking, exactly like the product.

Interface elements are glass panels floating on that water, not opaque cards sitting on a page. Depth comes from blur, border hairlines, and colored glow blooms behind and beneath elements — never from hard, neutral drop shadows. The aesthetic reads as **aurora tecnológica**: an atmospheric, premium dark-tech mood rather than a sterile SaaS-dashboard mood, because the buyer is a local business owner who needs to feel "this is serious technology working for me," not "this is a spreadsheet."

Two structural habits repeat everywhere and should be preserved in any new surface: (1) every interactive control (buttons, nav tabs, filter chips, badges) is a pill; every container (card, panel, modal) is a large-but-finite rounded rectangle — pills never contain other pills; (2) a small pulsing dot is the site's one recurring signal for "this is live/real/active right now" (online status, "system active" badges, footer trust badge) — it is never used decoratively.

**Key Characteristics:**
- Near-black, never pure-black, layered backgrounds with glass cards floating above color-tinted glow blooms
- Violet→cyan→emerald brand gradient used sparingly as a moving accent (text-fill on numbers, progress bar, card top-edge seal), never as a flat background fill
- Syne (geometric, high-impact) for anything that asserts a claim; DM Sans (light, quiet) for anything that explains
- Every primary CTA sweeps with a single diagonal light pass, at rest and again on hover
- A pulsing dot is the only "this is real-time" signal in the system

## Colors

The palette is almost monochrome (near-black + white at varying opacity) with the brand gradient reserved for accents that must earn attention — text-fill on hero copy and big numbers, button fills, the top-edge seal on hero cards, the scroll progress bar.

### Primary
- **Aurora Violet** (`#8b5cf6` / `--s1`): the system's signature hue. Used for primary CTA gradients, active states, icon accents, focus rings, and as the leading stop in the brand gradient.
- **Aurora Violet Deep** (`#7c3aed` / `--s2`): the second gradient stop; darkens the violet gradient toward the black background so brand buttons still read as "dark premium," not candy-bright.

### Secondary
- **Electric Cyan** (`#22d3ee` / `--c1`): the second beat of the aurora — appears in the brand gradient's midpoint, section accent labels, and portfolio/demo section theming (cool wash vs. the warm violet wash used elsewhere).
- **Deep Indigo** (`#6366f1` / `--c2`): pairs with cyan in secondary gradients (filter chips, accent labels); rarely stands alone.

### Tertiary
- **Signal Emerald** (`#10b981` / `--g1`): reserved almost exclusively for the "live/active" pulsing-dot pattern and trust badges ("propuesta gratis," online status). Because it never appears elsewhere, it functions as a semantic color, not a decorative one — don't reuse it for generic accents.

### Neutral
- **Void Black** (`#03050a` / `--bg`): the base surface. Deliberately not pure `#000` — carries the faintest blue cast consistent with "night water," not "OLED black."
- **Deep Water** (`#060a12` / `--bg2`), **Panel Ink** (`#0a1018` / `--bg3`), **Elevated Ink** (`#0e1622` / `--bg4`): a four-step stack of near-blacks used to separate sections and nested panels without ever introducing a light surface.
- **Text Bright** (`rgba(255,255,255,.75)` / `--m1`): primary reading text on dark.
- **Text Muted** (`rgba(255,255,255,.58)` / `--m2`) and **Text Faint** (`rgba(255,255,255,.52)` / `--m3`): secondary copy, captions, metadata — chosen by how much attention the line deserves, not by a fixed hierarchy rule.
- **Border Hairline** (`rgba(255,255,255,.07)` / `--b1`) and **Border Hairline Strong** (`rgba(255,255,255,.12)` / `--b2`): the only border colors used on neutral cards, nav, and dividers.

### Named Rules
**The Glow-Matches-Fill Rule.** A colored button, card, or badge's shadow and ambient glow always share the hue of its own fill (a violet button glows violet, the WhatsApp button glows WhatsApp-green). Never drop a neutral gray shadow under a colored element.

**The Emerald-Means-Live Rule.** Emerald (`#10b981`) is reserved for the pulsing-dot "active/real" signal and its badges. If a new element needs a generic success or positive-state color, reach for it only when the state is genuinely live/real-time — otherwise use violet.

## Typography

**Display Font:** Syne (with `sans-serif` fallback) — geometric, high-contrast, weights 400/500/700/800
**Body Font:** DM Sans (with `sans-serif` fallback) — humanist, quiet, weights 300/400/500 + italic

**Character:** Syne makes a claim; DM Sans explains it. Every headline, number, label, and button uses Syne at 700 or 800; every paragraph of explanatory copy drops to DM Sans at 300 (light). The pairing is deliberately unbalanced — Syne is loud and geometric, DM Sans is almost recessive — so hierarchy reads instantly even at a glance.

### Hierarchy
- **Display** (800, `clamp(2.8rem, 5vw, 4.9rem)`, line-height 0.97, letter-spacing -.045em): the hero H1 only. Ships as three staggered rows — row 1 near-white, row 2 brand-gradient text-fill, row 3 a smaller 32%-opacity descriptor line — each animating in with its own delay. Don't collapse this into a single-line H1 on new hero variants; the three-row reveal is a signature, not an accident of copy length.
- **Headline** (800, `clamp(2rem, 4.5vw, 3.4rem)`, line-height 1.05, letter-spacing -.04em): section H2s (`.sh`). Always preceded by a Label kicker.
- **Title** (800, `1.05–1.15rem`): card and component titles (pricing plan names, benefit card headings, chat widget name).
- **Body** (300, `clamp(.95rem, 1.4vw, 1.04rem)`, line-height 1.9, `rgba(255,255,255,.72)`): paragraph copy. Constrained to ~500–530px measure wherever it sits next to a headline.
- **Label** (700, `.6–.63rem`, letter-spacing .18–.22em, uppercase): section kickers and micro-badges, always low-opacity and hue-tinted to match the section's accent color (violet or cyan).

### Local-SEO Article Template scale (secondary)

The 22 `diseno-web-[ciudad].html` satellite pages (see [Local-SEO Article Template](#local-seo-article-template-secondary-system) under Components) run at a smaller, quieter type scale than the main site — same two families (Syne / DM Sans), lower contrast, no display tier. Consolidated from 16 near-duplicate ad-hoc values down to 6 steps:

- **Article H3** (700, `1.1rem`): sparse subsection headings inside a long article body.
- **Article Body** (300, `.93rem`, `rgba(255,255,255,.38)`): paragraph copy, feature/pricing list items, numbered process steps.
- **Article Strong Label** (700, `.88rem`): FAQ question text, ghost-button labels ("Ver portfolio →"), CTA-callout intro line.
- **Article Light Label** (300, `.84rem`, `rgba(255,255,255,.25)`): FAQ answer text, pricing disclaimer copy.
- **Article Meta** (300–500, `.78rem`): breadcrumb mini-nav, WhatsApp/cookie-banner button labels, art-tag/art-date captions.
- **Article Micro Label** (500–700, `.7rem`, often uppercase): geo eyebrow badge, footer category kickers, internal-link pills, copyright line.

Headline tiers are not part of this consolidation and stay as their own intentional steps, each already consistent within its own sub-family: the hero H1 (`clamp(2.2rem,5.5vw,4rem)` inline family · `clamp(2rem,5vw,3.4rem)` Vigo/Palma/Las Palmas · `clamp(2rem,5vw,3.5rem)` Granada/Málaga/Sevilla — three families, deliberately left unmerged since unifying them would move the hero H1 by more than 8px), the post-hero echo H2 (`clamp(1.5rem,3vw,2.2rem)`, 16 pages, already uniform), and the section H2 (`clamp(1.3rem,2.5vw,1.9rem)`).

### Named Rules
**The Gradient-Number Rule.** Any large standalone statistic (hero stats, "números" section counters) renders as Syne 800 with the brand gradient clipped to the text (`background-clip: text`), never a flat color. This is the system's signature way of making a number feel earned rather than printed.

## Layout

Content sits in a `1280px` max-width container (`1300px` for the hero specifically), centered with `clamp(1.5rem, 5vw, 3.5rem)` horizontal padding. Vertical section rhythm is generous and uniform: `clamp(6rem, 10vw, 9rem)` of padding above and below every section — the site breathes, it never feels dense.

The hero is a two-column grid (`1fr 540px`) with copy on the left and a floating device mockup on the right; it collapses to a single centered column at `1080px` and stays that way through mobile. Card grids (pricing, benefits, portfolio) use `repeat(auto-fit, minmax(Npx, 1fr))` rather than fixed column counts, so they reflow without bespoke breakpoints until the true mobile break.

**Breakpoints:** `1080px` (hero and most multi-column grids collapse to one column), `767px` (nav becomes a hamburger + slide-in overlay, custom cursor disables, a fixed bottom mobile CTA bar appears and `body` gains `padding-bottom` to clear it), `359px` (final type-size clamp floor for very small phones).

### Named Rules
**The Breathing Room Rule.** Section padding never drops below `6rem` vertically even on mobile (it compresses horizontally, not vertically). Density is not how this system signals more content; more sections is.

## Elevation & Depth

Hybrid, glass-forward: primary surfaces are translucent panels (`background: rgba(6,10,18,.7–.96)`) with `backdrop-filter: blur(20–28px) saturate(1.3–1.6)` and a single hairline border, floating above large, softly blurred radial color blooms (`filter: blur(80–100px)`) positioned absolutely behind or beside them. This is the primary source of depth — not shadow stacking.

Directional `box-shadow` is used sparingly and always soft (blur radius ≥ 18px), in two flavors: ambient dark shadows for physically "lifted" elements (floating phone mockup, badges: `0 8–16px 24–40px rgba(0,0,0,.5–.6)`), and colored glow shadows on interactive fills that intensify on hover rather than staying static (`0 4px 22px rgba(139,92,246,.28)` at rest → `0 10px 32px rgba(139,92,246,.48)` on hover). A hard, neutral, sharp-edged drop shadow never appears anywhere in the system.

### Shadow Vocabulary
- **Ambient lift** (`box-shadow: 0 8px 24px rgba(0,0,0,.5)`, scaling up to `0 16px 40px rgba(0,0,0,.6)` for larger floating elements): badges, floating phone mockup, dropdown-like overlays.
- **Brand glow — resting** (`box-shadow: 0 4px 22–26px rgba(<fill-hue>,.22–.28)`): default state of any colored button.
- **Brand glow — hover** (`box-shadow: 0 10–14px 32–44px rgba(<fill-hue>,.4–.48)`): same button on hover, paired with `translateY(-2px to -3px) scale(1.02–1.04)`.
- **Card ambient** (`box-shadow: 0 24px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.07)`): large glass cards (hero card) — the inset line reads as a glass top-edge catching light.
- **Neon pulse** (`@keyframes` alternating `0 0 0 1px rgba(139,92,246,.15–.28), 0 0 80–110px rgba(139,92,246,.22–.35), 0 32px 90px rgba(0,0,0,.65)`): reserved for the single most-emphasized element on a page (e.g., the featured pricing plan) — a breathing violet aura. Use on at most one element per view; it loses meaning if repeated.

### Named Rules
**The No-Hard-Shadow Rule.** Every shadow in the system is soft (large blur, low-to-moderate opacity) and either pure black (ambient) or color-matched to its element (brand glow). A crisp, small-blur, neutral-gray shadow is off-system anywhere in this product.

## Shapes

Two registers, never mixed: **pill** (`border-radius: 100px`) for every clickable control — primary/secondary/ghost buttons, nav tabs, filter chips, status badges — and **large rounded rectangles** (`16px`–`26px`) for every container — cards, panels, the mobile menu overlay, the FAQ accordion. Small utility chrome (icon tiles, tiny badges, the mobile close button) steps down to `11px`–`14px`. Nothing in the system uses a sharp 0px corner or a full circle outside of avatars, dots, and orbs.

Borders are exclusively hairline (`1px`, occasionally `1.5px` for emphasis) and white-on-dark (`rgba(255,255,255,.07–.12)` at rest); a border only shifts to a brand hue (`rgba(139,92,246,.2–.35)`) to signal an active, featured, or open state — never as a default decorative treatment.

## Components

### Buttons
- **Shape:** pill (`border-radius: 100px`) for every variant.
- **Primary (brand):** violet gradient fill (`linear-gradient(135deg, #8b5cf6, #7c3aed)`), near-black text (`var(--bg)`, not white — this is deliberate: a dark wordmark on a bright gradient reads as premium rather than a generic light-on-color button), Syne 700–800, resting glow `0 4px 22px rgba(139,92,246,.28)`.
- **Primary (WhatsApp):** green gradient fill (`linear-gradient(135deg, #25d366, #128c7e)`), white text, otherwise identical treatment to the brand primary. This is the site's single most-repeated CTA — reserve the WhatsApp-green gradient exclusively for this action so it stays legible as "this is the contact button."
- **Hover / Focus:** lift (`translateY(-2px to -3px) scale(1.02–1.04)`) plus intensified color-matched glow (see Elevation). `:focus-visible` gets a `2px solid #8b5cf6` outline with `3px` offset — the one place the system uses a hard-edged outline.
- **Ghost/Secondary:** translucent white fill (`rgba(255,255,255,.04)`), hairline border, muted text; hover only lightens the fill and border — no shimmer, no glow. Used when a CTA needs to be present but subordinate to a primary button beside it.
- **Signature detail — the shimmer sweep:** every primary and WhatsApp button carries a single diagonal light-sweep pseudo-element that plays automatically on a ~3s loop at rest and re-triggers on hover. One sweep per button, never stacked.

### Badges / Pills
- **Live badge:** pill, low-opacity emerald fill (`rgba(16,185,129,.07)`) with emerald border (`rgba(16,185,129,.18)`), containing a small pulsing dot (`box-shadow: 0 0 10px currentColor`, opacity animating 1→.28 on a 2s loop) plus uppercase Syne label. This is the system's only "live/real-time" signal — don't create a second visual language for the same meaning.
- **Featured-plan ribbon:** small solid-gradient pill overlapping the top edge of a card (`position: absolute; top: -13px`) — reserved for marking the recommended option among peers (e.g., "Más completo" on pricing).

### Cards / Containers
- **Corner Style:** `16px`–`26px` depending on size (larger card = larger radius).
- **Background:** translucent near-black (`rgba(6,10,18,.7–.96)`) or a flat tinted tint (`rgba(255,255,255,.03)` for plain benefit cards, `rgba(139,92,246,.05)` for a featured/highlighted card).
- **Shadow Strategy:** see Elevation & Depth — ambient dark shadow, never a hard edge; featured cards may use the neon-pulse breathing glow.
- **Border:** `1px` hairline white by default; `1.5px` brand-tinted when the card is active, open, or featured.
- **Internal Padding:** `2.5rem` for feature/pricing cards, `1.5–1.75rem` for compact cards.
- **Signature detail:** large cards often carry a `1.5–2px` gradient hairline across the very top edge (`linear-gradient(90deg, #8b5cf6, #7c3aed, #22d3ee, #10b981)`) — a "brand seal" that reads as this-card-belongs-to-the-system even before any content loads.

### FAQ Accordion
- **Style:** stacked pill-cornered items (`16px` radius), hairline border at rest, background and border both intensify (darker fill, violet-tinted border) when open.
- **Icon:** a `+` in a small rounded tile rotates 45° into an `×` and shifts to violet on open — the same rotate-on-state-change language used for the hamburger menu.

### Chat Widget (signature component)
The Agente IA demo widget is the site's most distinctive custom component and should be treated as a template for any future conversational UI on the site: circular avatar with a violet ring border (`2px solid rgba(139,92,246,.5)`) and a small emerald "online" dot in the same pulsing-dot language as everywhere else; header badge pill in violet; message bubbles as rounded glass panels; quick-reply options as a vertical stack of bordered pill-cornered rows (icon + label + muted sub-label), with a visually distinct "boost" variant (violet-tinted fill/border) for the option that leads toward booking; a hairline-separated footer micro-disclaimer row using small dot separators (the same `•`-as-dot motif used in the footer bottom bar).

### Local-SEO Article Template (secondary system)
The 22 `diseno-web-[ciudad].html` satellite pages run a lighter sibling system, not the full index.html chrome: a 780–860px-wide `.art-body` reading column, `.art-box` for a labeled block, and `.art-cta` for the WhatsApp callout — same tokens (colors, `--f1`/`--f2`, radii) as the main site, but no cursor, no shimmer, no glass blur, and its own smaller type scale (see Typography). Every one of these pages defines the identical `.art-box`/`.art-cta` CSS rules in its `<head>`; only 3 (Granada, Málaga, Sevilla) apply them via class, the other 19 reproduce the same visual recipe inline per element — a known duplication to be aware of when editing these pages, not a defect to refix.

- **"Lo que incluye" / "Precios" list**: every page boxes both lists in a `.art-box` (or the inline equivalent) — hairline border, `rgba(6,10,18,.8)` fill, `16px` radius. Never leave a feature or pricing list as bare `<li>` rows floating on the page background.
- **FAQ section**: every page boxes each question individually — `border:1px solid rgba(255,255,255,.07);border-radius:12px;background:rgba(6,10,18,.6)` per question, one card per question. Never render FAQ as bare heading/paragraph pairs.
- **CTA callout**: a violet-tinted panel (`background:rgba(139,92,246,.06–.07);border:1px solid rgba(139,92,246,.18–.22);border-radius:10–12px`) with a uniform hairline border on all four sides — no one-sided accent border. A thick single-side "side-tab" border is an off-system anti-pattern here as everywhere else (see the Elevation & Depth / Shapes borders rules); if a callout needs to stand out, use the panel's own tinted fill and glow, never an asymmetric border.
- **Hero background**: the gradient wash plus the two blurred orb glows (`.hero-orb1`/`.hero-orb2`) are enough atmosphere on their own. Don't add a decorative dot-grid overlay behind the hero copy — reserve literal grid patterns for canvas/map/blueprint surfaces, which this hero is not.

Prefer reusing the `.art-box`/`.art-cta` classes (already defined identically in every page's `<head>`) over re-inlining the same declaration per element on any *new* satellite page — the existing inline duplication across 19 pages is legacy, not the pattern to keep extending.

### Navigation
- **Desktop:** fixed top bar, transparent until scroll, then gains a blurred near-black background (`backdrop-filter: blur(24px) saturate(1.5)`) and a soft shadow. Nav links are pill tabs that gain a subtle gradient wash and brighten on hover/active; the CTA is the standard brand-primary pill button.
- **Mobile (≤767px):** hamburger icon morphs into an X; tapping opens a full-screen near-opaque blurred overlay with large staggered-entrance nav items (oversized low-opacity Syne labels that brighten and shift right on hover/touch) and a WhatsApp-green CTA pinned near the bottom.

### Custom Cursor (desktop only)
A small filled dot plus a larger trailing outlined ring replace the native cursor above `768px` on fine-pointer devices; both shrink/change color on hovering interactive elements (violet default → cyan on hover). Disabled entirely on touch devices and mobile widths — never force a custom cursor where there is no real pointer.

## Do's and Don'ts

### Do:
- **Do** keep every interactive control pill-shaped (`100px` radius) and every container a large-but-finite rounded rectangle (`16–26px`) — never blur the two registers.
- **Do** match a colored element's shadow/glow hue to its own fill color (Glow-Matches-Fill Rule).
- **Do** reserve emerald (`#10b981`) and the pulsing-dot pattern exclusively for "this is live/real right now" signals.
- **Do** clip the brand gradient to text for any large standalone statistic, never render it as a flat color.
- **Do** give every primary/WhatsApp button exactly one shimmer sweep, replaying at rest and on hover.
- **Do** keep body copy in DM Sans at light weight (300) with generous line-height (~1.9) and a ~500–530px measure next to headlines.
- **Do** box every distinct cluster of related claims — a feature list, a pricing comparison, a FAQ — in a hairline-bordered, translucent-fill container; on the local-SEO article template that means both the "Lo que incluye"/"Precios" list (`.art-box`) and each FAQ question (its own `12px`-radius card), not just one of the two.

### Don't:
- **Don't** use pure black (`#000`) for any surface — the darkest tone in the system is `#03050a`, layered upward through `#060a12` / `#0a1018` / `#0e1622`.
- **Don't** add a hard-edged, small-blur, neutral-gray drop shadow anywhere — every shadow is soft and either pure-black-ambient or color-matched.
- **Don't** re-inline `.art-box`/`.art-cta` declarations per element on a new satellite page — reuse the shared class already defined in the page's `<head>`; that duplication is how the FAQ and feature-list treatments drifted apart across the 22 existing pages in the first place.
- **Don't** introduce a third typeface — Syne carries every claim/label/number, DM Sans carries every explanation.
- **Don't** stack more than one "live" signal language — the pulsing dot is the only one; don't invent a second badge style for the same meaning.
- **Don't** fabricate a testimonials/review card style — the product has none today and PRODUCT.md forbids inventing them; if this changes, design the pattern fresh rather than repurposing another component.
