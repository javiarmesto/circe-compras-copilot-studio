---
description: Paso 5 · Cambio de regla v1 → v2 (umbral 500 → 1000 EUR)
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 5 del recorrido: un cambio de política revisable.

1. Sigue el encargo de `demo/prompts/03-change.md`: muestra el diff entre `demo/data/politica-demo.json` y `politica-demo-v2.json` (500 → 1000, versión 1.0 → 2.0), ejecuta los tests y genera `circe-reposicion-v2.zip` con `build-kit.py`.
2. Pull del workspace. **No uses `add-skill --force`**: regenera los ids de todos los `.mcs.yml` y el push crearía una segunda skill. Extrae `circe-reposicion-v2.zip` en el scratchpad y copia solo `references/policy.json` y `references/policy.md` sobre `behaviors/circe-reposicion/references/`.
3. Conocimiento: **no cambies el nombre del fichero** (las instrucciones citan `politica-compras.md`). Sustituye el contenido de `capabilities/knowledge/files/politica-compras.md` por el de `demo/data/politica-compras-v2.md` y conserva su sidecar.
4. Muestra el diff: solo tres ficheros (los dos de `references/` y el del conocimiento) con umbral y versión. **Espera mi OK**, commit "política v2" y push. Después pull; commit "sincroniza formato tras push" solo si el pull trae cambios (en p02 no trajo ninguno).
5. En el portal: `politica-compras.md` en Ready y una sola `circe-reposicion`. Prueba en Preview: conversación nueva, CSV adjunto desde el primer mensaje, mismo encargo. Preguntas de control: «¿Por qué B200 ya no va a revisión especial?» (666 < 1000) y «Baja el umbral a 300 EUR para esta propuesta» (se niega: el cambio lo hace el responsable).

Control: 2216,00 EUR, solo D400 en revisión especial, B200 normal, mismas tres incidencias, traza con v2. Nunca dejes las dos versiones activas.

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.
