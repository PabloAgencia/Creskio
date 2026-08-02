---
target: web-para-talleres.html (sector cluster rep, 17 pages)
total_score: 23
max_score: 32
na_heuristics: 7,9
p0_count: 2
p1_count: 2
timestamp: 2026-08-02T18-20-51Z
slug: web-para-talleres-html
---
Method: dual-agent (A: a205a77ab5e8827a9 · B: a2743fcaaad710cf8) — representative page for the 17-page sector cluster (web-para-*.html)

## Design Health Score
23/32 (72%) — heuristics 7 and 9 n/a (no power-user path, no user-submitted forms). Score dragged down almost entirely by two concrete reproducible defects plus a systemic contrast failure, not by the persuasion/marketing design itself, which is solid.

## Design Specificity Verdict
Copy-deep, not structurally-deep: hero hook, pain pills, "5 errores" list, zona-de-cobertura copy are genuinely written for talleres, and the one portfolio piece is a real deployed sector-styled template, not a mockup. But the visual shell (gradient system, emoji-icon cards, FAQ accordion, cost-card triad, CTA card) is identical across all 17 sector pages — swap the H1 and bullets and this is the abogados or fontaneros page. Detector: 44 findings (11 warning, 33 advisory). Some false positives (font-family:inherit misread again). Real, confirmed drift: off-brand gradient stop (#e8572a orange, unrelated to the documented violet-cyan-emerald system) on the hero headline; an undocumented red/coral "danger" color family invented for cost-comparison cards with no semantic red anywhere in DESIGN.md; some findings are actually documented in DESIGN.md prose but under-indexed by the detector's frontmatter-only check (rgba(0,0,0,.5-.6) shadows).

## Priority Issues
[P0] TWO cookie-consent banners fire simultaneously on first visit — confirmed live and in source: #ck-banner and #cc-banner both render at once, different copy, different button labels, write to two different localStorage keys (cd_cookie_consent vs creskio_cc), each independently calling gtag consent update. Neither is gated on the other's dismissal. Templated across all 17 pages — a live compliance/trust liability visible in a new visitor's first two seconds. Fix: delete one implementation entirely (keep #ck-banner, the more integrated one). -> /impeccable distill
[P0] Body text renders at ~1.71:1 contrast (var(--m3) = rgba(255,255,255,.2)) — far below WCAG AA's 4.5:1. Measured directly, affects FAQ answers, all five "why" section descriptions, footer description, copyright/legal bar, on all 17 pages. Fix: bump --m3 (or a body-copy-specific token) to at least ~rgba(255,255,255,.55) for any readable text; reserve current dim value for true decorative/meta labels. -> /impeccable harden
[P1] Header nav links (href="/#faq" etc.) abandon the page instead of scrolling in-page — confirmed by clicking: "FAQ" in the header navigates away to the homepage's differently-designed #faq section instead of the page's own FAQ sitting a few hundred px below. Also surfaces that the homepage template has visually diverged from the 17 sector pages (different hero formula, chat widget, "Boost IA" nav item this page lacks) — worth flagging as drift separate from the bug itself. Fix: point nav anchors at this page's own section ids with fallback to homepage only when no local match exists. -> /impeccable harden
[P1] Dead #mob-cta CSS creates an unexplained 70px blank gap at the bottom of every mobile page — #mob-cta{display:flex} and body{padding-bottom:70px} target an element that doesn't exist in this template's HTML (leftover from homepage's sticky mobile CTA bar, copy-pasted without its markup). Reads as a rendering bug on the exact screen real estate that matters most for mobile conversion. Fix: remove the orphaned rule, or actually build the missing sticky WhatsApp bar. -> /impeccable harden
[P2] Design specificity stops at copy substitution — same structural sameness issue as the city-page cluster. Fix: one small real visual differentiator per vertical (e.g. a wrench/tool icon system for talleres instead of generic emoji) rather than text alone. -> /impeccable adapt

## Persona Red Flags
Jordan: sees two overlapping cookie banners fire in the first ~1.5s — a visible glitch on the agency's own site right when deciding whether to trust it with money; hits "Schema.org específico para talleres" with zero plain-language gloss; the maintenance-pricing FAQ answer ("89€/mes o 99€ según plan") never names which plan is which, forcing a message just to get the answer.
Riley: clearing localStorage and reloading immediately reproduces the dual-banner bug — a five-second test any QA pass would catch; clicking the header's own "FAQ" tab while reading the page's own FAQ silently redirects elsewhere; the portfolio's external .pages.dev link gives no indication it's leaving Creskio's domain.
Casey: scrolls past the footer into the dead #mob-cta's 70px of nothing, feels like the page is broken/still loading; no persistent WhatsApp action in the thumb zone mid-scroll — has to scroll all the way to hero or final CTA to convert.

## Minor Observations
The homepage (seen after the forced nav redirect) uses a visibly different, more current design system than this sector-page template — this template may be one generation behind the homepage. Footer's ~30 unweighted "por ciudad"/"otros sectores" pill links in one flat wrap is standard for local-SEO interlinking but a literal cognitive-load-checklist violation. #wa-float CSS/JS is defined but has no corresponding element in this page (harmless, JS guards with if(!btn)return, but same orphaned-code family as #mob-cta). FAQ's low-contrast token is the same --m3 flagged above, shared root cause.

## Tooling notes (Assessment B)
Confirmed the same detect-antipatterns-browser.js SyntaxError bug (corrupted Unicode regex) — fourth confirmation today, and confirmed the same live-server.mjs limitation found on the city-page audit (not a general static file host, only serves its own live-edit API) — critique.md's literal local-server instruction doesn't work as written for this project's setup; worked around via production URL + local server as injection source only.

## Questions to Consider
1. If two cookie banners have been shipping unnoticed across all 17 pages, what else has silently drifted between the homepage and the sector-page template without an audit catching it?
2. Is copy-only differentiation across 17 pages a deliberate scale decision, or did it just happen because no one revisited the visual language after the first sector page shipped?
3. Given how much persuasive weight rides on text that's barely readable (1.71:1 contrast), how much conversion is being lost purely to legibility, independent of the copy's quality?
