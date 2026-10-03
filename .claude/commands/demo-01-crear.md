---
description: Paso 1 · Crear el agente desde el terminal y versionar su workspace
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 1 del recorrido: nace el agente.

1. Toma nombre, schema, workspace y entorno de la última entrada de `practice/runs.json`.
2. Prepara el comando: `./scripts/New-Circe.ps1 -Deploy -Environment <entorno> -ProjectDir <workspace> -Name "<nombre>" -SchemaName <schema>`. Lee el script y explica en tres líneas qué `pac` lanza y qué crea en Dataverse.
3. **Muestra el comando y espera mi OK.** Tras el OK, ejecútalo y mide el tiempo.
4. Explica el workspace generado: qué define cada fichero, dónde están las instrucciones y qué metadatos usa para pull/push. No toques `.mcs/`.
5. Comprueba en `settings.mcs.yml` si la plantilla es `cliagent-…` y dilo expresamente: es la señal de que el agente está en el GitHub Copilot harness. Pide al usuario que lo confirme en el portal.
6. `git init` dentro del workspace, crea un `.gitignore` con `.github/` (telemetría de Claude Code y Copilot), commit "scaffold inicial" y muestra el log.

Control: agente visible en `pac copilot list`, plantilla `cliagent-`, commit hecho. Si la plantilla no es `cliagent-`, para y propón la alternativa de `docs/03` (crear en el portal con ese harness y `pac copilot clone`).

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.

