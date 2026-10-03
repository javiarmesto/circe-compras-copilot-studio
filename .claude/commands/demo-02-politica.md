---
description: Paso 2 · Añadir la política v1 como conocimiento desde el workspace
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 2 del recorrido: Circe pequeña, sin skill.

1. Workspace: última entrada de `practice/runs.json`. Haz pull con el subagente Copilot Studio Manage y compara `settings.mcs.yml` con HEAD. El primer pull tras crear el agente puede vaciar en local las instrucciones, `template` y `language` aunque en el portal estén bien: si pasa, dilo, restaura con `git checkout -- settings.mcs.yml` y sigue.
2. Usa la orden `add-knowledge` del plugin `mcs-assistant` para añadir `demo/data/politica-compras.md` como documento subido desde fichero local, con el nombre de fichero `politica-compras.md` (las instrucciones del paso 3 lo citan así). Un fichero subido no admite nombre visible propio, y Copilot Studio sustituye la description por una genérica: no es un error.
3. Muestra el YAML generado y el diff con git. **Espera mi OK** y haz push con el subagente Manage. Commit "política v1". Después haz pull y, si solo cambia el formato de los YAML, commit "sincroniza formato tras push".
4. Dame las tres preguntas de control para el Preview del portal y lo que debe responder:
   - «¿Cuándo requiere revisión especial una propuesta de compra?» → en este paso el agente **puede pedir la política o buscarla**: las instrucciones dicen "Si no tienes la política, pídela" y el resultado varía entre conversaciones (p01 la pidió, p02 la buscó). Anota cuál de las dos pasa; el paso 3 hace explícita la prioridad de búsqueda y la comprueba en una nueva conversación
   - «¿Y una línea de 500 EUR exactos?» → revisión normal (umbral estrictamente superior)
   - «Calcula mi reposición» → pide el CSV y no afirma haber calculado

Si `add-knowledge` no es capaz o el conocimiento no aparece tras el push, dilo y propón añadirlo en el portal y hacer después pull para enseñar el diff.

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.

