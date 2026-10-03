---
description: Paso 4 · Validar, empaquetar e importar la skill circe-reposicion desde código
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 4 del recorrido: la skill.

1. Explica en tres líneas por qué la `description` de `demo/skills/circe-reposicion/SKILL.md` decide cuándo se activa.
2. `python scripts/build-kit.py`. Debe decir "Skill válida" y generar `demo/packages/circe-reposicion-v1.zip`.
3. Pull del workspace de la pasada. `add-skill.js` importa una carpeta, no un ZIP: extrae `demo/packages/circe-reposicion-v1.zip` en el scratchpad y usa la orden `add-skill` del plugin `mcs-assistant` sobre esa carpeta para importarla en el workspace, con el nombre `circe-reposicion`. Si no encuentra su script, está en `scripts/add-skill.js` dentro de la carpeta del plugin.
4. Muestra lo creado en `behaviors/` y el diff. **Espera mi OK**, commit "skill v1" y push con el subagente Manage. Después pull y commit "sincroniza formato tras push" (el push quita la description de `skill.mcs.yml`; el portal la toma del `SKILL.md`).
5. Prueba en Preview: conversación nueva, con `demo/data/inventario-demo.csv` adjunto **desde el primer mensaje** (así la traza muestra la skill y el script en un solo turno):
   «Prepara la reposición de los próximos siete días. Aplica nuestra política y los lotes. Devuelve un CSV y un informe breve con las incidencias que deba resolver.»
6. Cuando la persona que realiza la demo descargue `proposal.csv` y `report.md`, compáralos con `evidence/local-v1/`.

Control: 2216,00 EUR, B200 y D400 en revisión especial, incidencias E500, G700 y H800, "Used skill: circe-reposicion" en la traza (también puede aparecer la skill integrada `analyzing-csv`, que preprocesa el CSV). En el portal, Skills muestra una sola `circe-reposicion` con su descripción. Si `add-skill` rechaza el workspace (no es CLI agent) o la skill no aparece activa tras el push, dilo: la alternativa es subir el ZIP en el portal y hacer pull para enseñar el diff.

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.
