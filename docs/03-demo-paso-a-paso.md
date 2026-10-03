# Circe Compras · Recorrido paso a paso

Trabaja en la raíz de este repositorio con VS Code y tu propio entorno de Copilot Studio. Instala primero los requisitos de [01-setup-vscode.md](01-setup-vscode.md).

## Preparar una práctica

```powershell
$CirceEnvironment = 'https://TU_ORGANIZACION.crm4.dynamics.com'
.\scripts\New-PracticeRun.ps1 -Environment $CirceEnvironment
```

Sustituye la URL antes de ejecutar. El script prepara nombres y rutas locales; la creación en el tenant se hace en el paso 1. En Claude Code indica que lea `CLAUDE.md` y trabaje con la pasada recién preparada. No uses el entorno de otra persona.

## Órdenes de Claude Code

| Paso | Orden | Qué añade |
|---|---|---|
| 0 | `/demo-00-preflight` | Verifica herramientas, plugin, destino y resultados locales |
| 1 | `/demo-01-crear` | Crea un agente y su workspace con identidad nueva |
| 2 | `/demo-02-politica` | Incorpora la política v1 como conocimiento |
| 3 | `/demo-03-ciclo` | Explicita cuándo consultar el conocimiento |
| 4 | `/demo-04-skill` | Incorpora la skill y calcula la reposición |
| 5 | `/demo-05-cambio` | Cambia el umbral a v2 conservando identidades |
| 6 | `/demo-06-publicar` | Publica el borrador revisado, previa confirmación |

La [guía HTML](05-demo-en-escenario.html) contiene qué explicar, qué mostrar y los prompts con botones de copia. Solicita «modo escenario» para una explicación amena sin registros de ensayo. No pegues a la vez una orden y su prompt alternativo.

## Prueba en Preview

Abre una conversación nueva y adjunta `demo/data/inventario-demo.csv` desde el primer mensaje:

```text
Prepara la reposición de los próximos siete días.
Aplica nuestra política y los lotes.
Devuelve un CSV y un informe breve con las incidencias que deba resolver.
```

Resultado de referencia local: 2216 EUR; tres propuestas; incidencias E500, G700 y H800. Con v1, B200 y D400 requieren revisión especial. Con v2, solo D400. Repite el mismo encargo con el mismo CSV para comparar.

Comprueba que el conocimiento está Ready antes de probar. Una respuesta coherente o la traza «Used skill» no acreditan por sí solas una llamada concreta al script. No se crean pedidos ni se conecta a un ERP.

## Sincronizar y publicar

Revisa el destino y los cambios antes de actuar. Sigue el contrato de tu plugin instalado: Manage puede derivar las operaciones a skills específicas. Preserva los cambios locales antes del pull; si cambia o desaparece contenido de instrucciones, `template` o `language`, detente y revisa el diff. Nunca edites `.mcs/` a mano.

Espera a que cada operación termine. Si publish devuelve un error, verifica el estado antes de reintentar. No presentes un resultado no confirmado como una publicación correcta.

## GitHub Copilot Chat

La [guía complementaria](08-mini-demo-copilot-chat.html) utiliza un agente independiente. Consulta sus alternativas para Init, Architect y Describer según el contrato de la versión instalada. Las órdenes `/demo-*` son del proyecto de Claude Code.
