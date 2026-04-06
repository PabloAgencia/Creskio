# AUDIT — Portfolio Agencia Costa Digital

## Estado inicial
- Viewport: ✓ ya correcto
- img responsive: parcial — faltaba `height: auto`
- Breakpoint 768px: ✗ ausente en CSS principal
- Breakpoint 480px: ✗ ausente
- Fonts: legibles (usa clamp())

## Fixes aplicados
1. **img height:auto** — `img{max-width:100%;display:block}` → añadido `height:auto`
2. **@media (max-width: 768px)** — añadido: nav oculto en mobile, font-size 15px
3. **@media (max-width: 480px)** — añadido: font-size 14px, h1/h2 con clamp(), nav padding reducido
