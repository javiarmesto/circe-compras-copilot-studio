# Circe Compras · Copilot Studio desde VS Code

Demo de Javier Armesto para Bizz Summit ES 2026. Crea y evoluciona un agente de Copilot Studio desde VS Code con Claude Code o GitHub Copilot Chat y el plugin `mcs-assistant` de Microsoft Power CAT.

Circe recibe un inventario ficticio en CSV, aplica una política de compras y utiliza una skill con un script Python para preparar una propuesta de reposición. Devuelve propuestas e incidencias para decisión humana. **No conecta con Business Central, no crea pedidos y no envía mensajes.**

## Empieza aquí

1. [Preparar VS Code, PAC y el plugin](docs/01-setup-vscode.md).
2. [Crear tu primera práctica](docs/02-practica-desde-cero.md).
3. [Recorrido de la demo](docs/03-demo-paso-a-paso.md).
4. [Guía HTML de Claude Code con botones para copiar](docs/05-demo-en-escenario.html).
5. [Guía HTML de GitHub Copilot Chat](docs/08-mini-demo-copilot-chat.html).

Descarga los HTML y ábrelos localmente en tu navegador. Sustituye `TU_ORGANIZACION` por tu entorno y adapta las rutas de ejemplo. El respaldo citado en las guías es opcional y no se incluye.

## Comprobación local, sin tenant

```powershell
git clone https://github.com/javiarmesto/circe-compras-copilot-studio.git
cd circe-compras-copilot-studio
python scripts/build-kit.py
python -m unittest discover -s tests
```

Requisitos del material: Python 3.10+, Node.js 20+, Git, Power Platform CLI compatible con `pac copilot init --authoring-mode` y la extensión Microsoft Copilot Studio. El plugin declara PAC 2.9.3 como mínimo; comprueba los requisitos de tu versión instalada. Para crear y ejecutar el agente necesitas tu propio entorno y acceso a las capacidades usadas. El uso del servicio puede consumir capacidad facturable.

## Qué contiene

| Ruta | Contenido |
|---|---|
| `demo/agent/` | Instrucciones del agente |
| `demo/skills/circe-reposicion/` | Procedimiento, script Python y referencias |
| `demo/data/` | Inventario ficticio y políticas v1/v2 |
| `demo/packages/` | Paquetes de la skill, regenerables con `build-kit.py` |
| `.claude/commands/` | Órdenes `/demo-00-preflight` a `/demo-06-publicar` |
| `scripts/` | Inicialización y preparación de prácticas |
| `tests/` | Pruebas del cálculo |
| `evidence/local-v1/`, `evidence/local-v2/` | Salidas de referencia local |

Con el inventario de ejemplo, el total es **2216 EUR**. En v1 (umbral 500 EUR), B200 y D400 requieren revisión especial. En v2 (1000 EUR), solo D400. Las incidencias son E500, G700 y H800.

Las salidas de referencia validan el cálculo local; no prueban por sí solas la ejecución del script dentro de una conversación. Revisa lo que realmente muestra tu entorno.

## Presentación y contribuciones

El PowerPoint y los materiales del evento están en [BizzSummit2026](https://github.com/javiarmesto/BizzSummit2026). Este es el repositorio operativo de la demo.

Usa tus propias credenciales y configuración local. No subas `.mcs/`, perfiles de autenticación, archivos `.env`, workspaces conectados ni registros de tenant. Las operaciones sobre el entorno deben revisarse antes de ejecutarlas. Respeta el contrato de la versión instalada de `mcs-assistant`: las operaciones pueden delegarse en skills específicas.

El plugin [microsoft/copilot-studio-plugin](https://github.com/microsoft/copilot-studio-plugin) es experimental y cambia con frecuencia. El material es docente, no una solución de producción ni una implementación de autorizaciones de compra.
