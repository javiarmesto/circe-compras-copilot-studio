---
description: Paso 0 · Comprobaciones previas del ensayo o de la sesión (solo lectura)
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Comprobaciones previas de la demo. No crees ni cambies recursos en el tenant. El empaquetado de la skill escribe archivos locales.

1. Lee la última entrada de `practice/runs.json` y dime la pasada activa: id, nombre, schema, workspace y entorno. Si no existe, pide al usuario que ejecute `./scripts/New-PracticeRun.ps1 -Environment <URL>` y para.
2. Versiones: `pac` (mínimo 2.9.3), `python --version`, `node --version`, `git --version`.
3. Plugin: confirma que el plugin `mcs-assistant` está disponible en esta sesión y lista sus órdenes y subagentes tal como aparecen.
4. Tenant: `pac org who` y `pac copilot list --environment <entorno de la pasada>`. Confirma que el entorno activo es el de la pasada y que el agente de la pasada **no** existe todavía. `pac copilot list` no muestra el schema: búscalo por el nombre de la pasada.
5. Local: `python scripts/build-kit.py` y `python -m unittest discover -s tests`.

Resume en una tabla: comprobación, resultado, OK/KO. Si algo es KO, di qué hacer antes de seguir.
