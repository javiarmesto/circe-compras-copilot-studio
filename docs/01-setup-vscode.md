# 01 · VS Code: extensiones, plugin de CAT y marketplace

Prepara el equipo para crear Circe desde VS Code, con GitHub Copilot Chat o con Claude Code. Hazlo antes del punto 1 de [03](03-demo-paso-a-paso.md). Unos 30 minutos.

El repositorio ya trae dos ficheros que te ahorran pasos:

- `.vscode/extensions.json`: VS Code te propone instalar las extensiones necesarias al abrir la carpeta.
- `.claude/settings.json`: registra el marketplace `microsoft/copilot-studio-plugin` y marca `mcs-assistant` como recomendado. Lo leen Claude Code y también VS Code.

## 1 · Requisitos

Comprueba en el terminal de VS Code:

```powershell
code --version          # VS Code actualizado (Help → Check for Updates)
pac                     # Power Platform CLI 2.9.3 o superior (lo exige mcs-assistant)
python --version        # 3.10 o superior
git --version; gh --version
claude --version        # Claude Code
node --version          # Node.js 20 o superior: hooks y scripts del plugin son JavaScript
```

Si falta PAC: `dotnet tool install --global Microsoft.PowerApps.CLI.Tool` (o `update` si ya está).

## 2 · Extensiones de VS Code

Abre la carpeta del repo. VS Code muestra la notificación de extensiones recomendadas: **Install All**. Si no aparece, Extensions (`Ctrl+Shift+X`) → escribe `@recommended` → instala las de "Workspace Recommendations".

| Extensión | Para qué | Comprobación |
|---|---|---|
| Copilot Studio (Microsoft, `ms-CopilotStudio.vscode-copilotstudio`) | Clone, pull, push y el binario de servidor de lenguaje que usa el plugin de CAT | Icono de Copilot Studio en la barra lateral |
| GitHub Copilot Chat | Chat y modo agente en VS Code | Icono de chat, sesión iniciada |
| Claude Code | Claude Code en panel de VS Code | Icono de Claude en la barra lateral |
| Python | Ejecutar y depurar el script de la skill | Intérprete seleccionado abajo a la derecha |

La extensión de Copilot Studio es necesaria **aunque trabajes solo con Claude Code**: el plugin de CAT usa su binario para clonar y sincronizar.

**Inicia sesión en la extensión de Copilot Studio:** icono en la barra lateral → **Sign In** → **Allow** → cuenta del tenant de demo. Comprueba que ves el entorno de demo en la lista.

## 3 · Settings de usuario para plugins de agente

`Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)** y añade:

```json
"chat.plugins.enabled": true,
"chat.plugins.marketplaces": [
  "microsoft/copilot-studio-plugin"
]
```

- `chat.plugins.enabled` activa los plugins de agente (preview). Si aparece como gestionado por la organización y en `false`, no puedes cambiarlo tú: usa Claude Code (punto 5) y pide el cambio al administrador.
- `chat.plugins.marketplaces` añade el marketplace de Microsoft. Si ya tienes otros, añádelo a la lista sin borrarlos.

Guarda y ejecuta **Developer: Reload Window**.

## 4 · Instalar el plugin en VS Code (GitHub Copilot Chat)

**Opción A · desde el marketplace**

1. Extensions (`Ctrl+Shift+X`) → escribe `@agentPlugins`.
2. Busca `mcs-assistant` (marketplace `copilot-studio-plugin`) → **Install**.
3. Acepta el diálogo de confianza tras revisar que el origen es `microsoft/copilot-studio-plugin`.

También verás la recomendación con `@agentPlugins @recommended`, que viene de `.claude/settings.json`.

**Opción B · desde el repositorio**

`Ctrl+Shift+P` → **Chat: Install Plugin From Source** → `https://github.com/microsoft/copilot-studio-plugin` → **Trust**.

**Comprobación**

- `Ctrl+Shift+P` → **Chat: Plugins**: aparece `mcs-assistant` habilitado.
- En el chat, modo **Agent** → **Configure Skills**: aparecen las skills del plugin.
- `Ctrl+Shift+P` → **MCP: List Servers**: si el plugin trae servidores MCP, aparecen aquí.
- En el chat escribe `/` y comprueba qué órdenes añade el plugin. Anótalas: son las que usarás en [03](03-demo-paso-a-paso.md).

En Insiders, el plugin queda en `%USERPROFILE%\.vscode-insiders\agent-plugins\github.com\microsoft\copilot-studio-plugin`.

### Prueba de viabilidad en Copilot Chat (10 min)

`mcs-assistant` está escrito en formato de plugin de Claude: órdenes, subagentes y un hook de inicio en Node que instala dependencias y crea `%USERPROFILE%\.copilot-studio-cli\plugin-paths.json`, que es donde `/add-skill` busca sus scripts. VS Code admite ese formato, pero el hook solo actúa si recibe la variable de datos del plugin. Compruébalo antes de decidir:

1. Abre una sesión **nueva** de chat en modo Agent y escribe `/mcs-assistant`: deben aparecer `chat`, `migrate`, `add-skill`, `delete-agent` y `add-knowledge` (en Copilot Chat van con espacio, `/mcs-assistant add-skill`; en el panel de Claude Code, con dos puntos).  Los cuatro subagentes del plugin (Architect, Describer, Init y Manage) aparecen también en el selector de agentes de Copilot Chat: las capturas de tu propia instalación.
2. En el terminal: `Test-Path $env:USERPROFILE\.copilot-studio-cli\plugin-paths.json`. Si da `False`, el hook no se ha ejecutado en VS Code.
3. Pide: `/add-skill` con `demo/packages/circe-reposicion-v1.zip` **solo para validarla, sin importarla**. Debe localizar `scripts/add-skill.js` y validar el paquete.
4. Pide al subagente **Copilot Studio Manage** que liste los agentes del entorno de demo (solo lectura).

**Decisión:**

| Resultado | Qué usas en la demo |
|---|---|
| 1 a 4 correctos | Puedes usar Copilot Chat; mantén Claude Code como respaldo |
| Falla 2 o 3 | Claude Code en el panel de VS Code para todo lo del plugin; Copilot Chat solo para explicar o editar YAML |
| Falla 1 | El plugin no carga en Copilot Chat: todo con Claude Code |

La demo sigue siendo "desde VS Code" en cualquier caso: Claude Code corre dentro del editor.

## 5 · Instalar el plugin en Claude Code

Abre Claude Code en la raíz del repo (panel de Claude o `claude` en el terminal de VS Code).

**En el panel de Claude Code de VS Code, `/plugin` no funciona** (responde "/plugin isn't available in this environment"). Instálalo desde el menú:

1. Escribe `/` en el panel → **Manage plugins**.
2. Pestaña **Marketplaces**: comprueba que está `copilot-studio-plugin` (`GitHub: microsoft/copilot-studio-plugin`). Si no está, añádelo desde ahí. Al confiar en la carpeta, `.claude/settings.json` ya lo propone.
3. Pestaña **Plugins**: instala y habilita `mcs-assistant`.

**En Claude Code de terminal** (`claude`) sí funcionan las órdenes:

```text
/plugin marketplace add microsoft/copilot-studio-plugin
/plugin install mcs-assistant@copilot-studio-plugin
```

**Comprobación:** en el panel escribe `/mcs` y deben aparecer `/mcs-assistant:chat`, `/mcs-assistant:migrate`, `/mcs-assistant:add-knowledge`, `/mcs-assistant:delete-agent` y `/mcs-assistant:add-skill`. Las órdenes llevan el prefijo del plugin. 

## 6 · Opcional: GitHub Copilot CLI

Si usas Copilot CLI, VS Code también detecta los plugins que instalas con él:

```powershell
copilot plugin marketplace add microsoft/copilot-studio-plugin
copilot plugin install mcs-assistant@copilot-studio-plugin
```

## 7 · Comprobación final

- [ ] `pac`, `python`, `git`, `gh` y `claude` responden
- [ ] Extensión Copilot Studio instalada y con sesión en el tenant de demo
- [ ] `chat.plugins.enabled` en `true` y marketplace añadido
- [ ] `mcs-assistant` visible en **Chat: Plugins** (VS Code) y en **Manage plugins** (panel de Claude Code)
- [ ] Lista de órdenes del plugin anotada en el registro
- [ ] `pac auth create` hecho contra el entorno de demo (punto 2 de [03](03-demo-paso-a-paso.md))

## Problemas frecuentes

| Síntoma | Qué hacer |
|---|---|
| El plugin falla al clonar o sincronizar con PAC antiguo | `dotnet tool update --global Microsoft.PowerApps.CLI.Tool` (mínimo 2.9.3) |
| Aparece también el plugin `copilot-studio` 1.0.4 | Es el antiguo (`skills-for-copilot-studio`), detectado desde Copilot CLI. Desactívalo en **Chat: Plugins** |
| No aparece `@agentPlugins` o el plugin | Revisa `chat.plugins.enabled`; recarga la ventana |
| El ajuste está gestionado por la organización | Usa Claude Code; pide el cambio al administrador |
| "destination path already exists" al instalar | Borra `%APPDATA%\Code\agentPlugins\github.com\microsoft\copilot-studio-plugin` y repite |
| El plugin no puede clonar ni sincronizar | Falta la extensión Copilot Studio o su sesión |
| Skills u órdenes del plugin no cargan en Copilot Chat | Usa Claude Code para la demo |
| `/add-skill` no encuentra `add-skill.js` en Copilot Chat | Falta `plugin-paths.json` (el hook no se ejecutó): usa Claude Code |

## Referencias

- [Agent plugins in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins)
- [Instalar la extensión de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-install-configure)
- [microsoft/copilot-studio-plugin](https://github.com/microsoft/copilot-studio-plugin)
