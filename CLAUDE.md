# CLAUDE.md · Circe Compras

Repo de la demo de la sesión de Bizz Summit 2026 (3 de octubre, 10:00, sala Berlin 112): crear y mantener un agente de Copilot Studio **desde VS Code y Claude Code**, con el GitHub Copilot harness y la skill `circe-reposicion`. Lee `docs/HANDOFF.md` al empezar una sesión nueva.

## Reglas de trabajo

- **Nada toca el tenant sin OK explícito.** Antes de `pac copilot init`, `push`, `publish`, `delete`, `solution import` o cualquier orden del plugin que escriba en el entorno, muestra el comando exacto (o el diff) y espera a que la persona que dirige la demo diga OK. Leer (`pac org who`, `pac copilot list`, `pull`) no necesita OK.
- **Siempre pull antes de push.** Usa los agentes y skills de la versión instalada de `mcs-assistant`; Manage puede derivar clone, pull, push y publish a skills específicas. Preserva cambios locales antes del pull.
- **Nunca edites a mano la carpeta `.mcs/`** de un workspace: son metadatos de sincronización.
- **No inventes YAML.** Si una capacidad no está documentada por PAC o por el plugin, dilo y propón el portal como alternativa.
- **El cálculo lo hace el script.** No reimplementes la aritmética de `demo/skills/circe-reposicion/scripts/replenishment.py` ni cambies sus reglas.
- **Cada workspace de agente lleva su propio Git** dentro de `live-agents/<run>/` (la carpeta está excluida del repo). Commit tras cada paso aprobado.
- Todo en castellano de España. Usa la identidad Git configurada por cada participante y un correo noreply para material público.

## Valores esperados (datos ficticios)

| Caso | Resultado |
|---|---|
| v1 (umbral 500 EUR) | 2216,00 EUR · 3 propuestas · B200 y D400 en revisión especial · incidencias E500, G700, H800 |
| v2 (umbral 1000 EUR) | 2216,00 EUR · solo D400 en revisión especial · B200 normal · mismas incidencias |
| B200 | 36 unidades aunque faltaban 32: lote de 12 |

Comprobación local: `python scripts/build-kit.py` (debe decir "Skill válida") y `python -m unittest discover -s tests` (10 OK).

## Mapa del repo

- `demo/agent/instructions.md` · instrucciones del agente
- `demo/skills/circe-reposicion/` · skill (SKILL.md, script, política)
- `demo/data/` · inventario ficticio y políticas v1/v2 (`.json` para el script, `.md` como conocimiento)
- `demo/prompts/` · encargos originales de la demo
- `scripts/New-Circe.ps1` · crea el agente (`-Deploy -Environment -ProjectDir -Name -SchemaName`)
- `scripts/New-PracticeRun.ps1` / `Reset-Practice.ps1` · práctica desde cero con agentes `circe_compras_pNN`
- `scripts/build-kit.py` · valida y empaqueta la skill en `demo/packages/`
- `evidence/local-v1`, `local-v2` · resultados esperados; `evidence/tenant/` · registros de ensayo (no se versiona)
- `docs/` · setup, práctica, demo paso a paso (ensayo), guion de escenario (`04`) y handoff

## Órdenes del proyecto (`.claude/commands`)

`/demo-00-preflight` · `/demo-01-crear` · `/demo-02-politica` · `/demo-03-ciclo` · `/demo-04-skill` · `/demo-05-cambio` · `/demo-06-publicar` · `/ensayo-registro`

Cada una ejecuta un paso del recorrido de la sesión con sus controles. Úsalas en orden en el primer ensayo.

## Demo en escenario

Cuando la persona que dirige la demo diga «modo escenario» o la pasada activa sea `stage`, lee y aplica `docs/06-modo-escenario.md` antes de cualquier `/demo-*`. Ejecuta cada paso con una explicación breve, concreta y amena para el público. La guía personal con órdenes y botones de copia está en `docs/05-demo-en-escenario.html` (fuente Markdown al lado). Si el usuario dispone de un respaldo propio, consérvalo sin cambios. El repositorio no incluye ninguno.

