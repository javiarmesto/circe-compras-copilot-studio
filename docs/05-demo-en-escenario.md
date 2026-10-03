> Guía reutilizable: sustituye `TU_ORGANIZACION` por tu entorno y adapta `C:\Demos` a tu equipo. `RESPALDO` es un agente propio opcional; no forma parte de este repositorio. Ejecuta los comandos desde `circe-compras-copilot-studio`.

# Circe Compras · Guion de demo en escenario

Bizz Summit · sábado 3 de octubre de 2026 · Javier Armesto

Guion operativo para presentar con las órdenes `/demo-*`: qué decir, qué mostrar y qué copiar. Claude Code ejecuta cada paso y lo explica de forma breve y amena. Sin medición ni registro de ensayo. La presentación acompaña este recorrido; los números siguientes son bloques de demo, no números de diapositiva.

**Respaldo opcional:** prepara y valida tu propio agente con política v2 antes de la demo. No se incluye ningún agente publicado. Consérvalo sin cambios durante el recorrido.

## Antes de la sesión

Abre `C:\Demos\circe-compras-copilot-studio` en VS Code Insiders. Prepara Stage una sola vez en PowerShell:

```powershell
$CirceEnvironment = 'https://TU_ORGANIZACION.crm4.dynamics.com'
.\scripts\New-PracticeRun.ps1 -Environment $CirceEnvironment -Stage
```

Esto prepara valores locales; el agente se crea en directo. Si Stage ya está preparada, no repitas el comando. No ejecutes Reset sobre RESPALDO.

Abre una conversación nueva en Claude Code y pega:

```text
Activamos MODO ESCENARIO para la demo de Circe Compras en Bizz Summit.
Lee CLAUDE.md y docs/06-modo-escenario.md.
Usaremos las órdenes /demo-* del proyecto, un paso cada vez.

Destino exclusivo de la demo:
- Nombre: Circe Compras
- Schema: circe_compras
- Workspace: ./live-agents/circe-live
- Entorno: https://TU_ORGANIZACION.crm4.dynamics.com

Si has preparado un respaldo propio, consérvalo sin cambios. Esta guía no incluye uno.
No modifiques las demás pasadas.

Trabajaremos un paso cada vez, según mis mensajes.
No midas tiempos, no generes registros de ensayo ni propongas
cambios en las guías durante la sesión.

Además de ejecutar cada paso, acompáñame explicándolo para el público.
Antes: cuenta en dos o tres frases qué vamos a conseguir y para qué
le sirve al responsable de Compras. Usa ejemplos de nuestro caso.
Durante: señala la pieza interesante en pantalla, sin recitar logs.
Después: explica qué cambió realmente y dime dónde mirarlo.
Tono cercano y ameno, sin discursos largos ni lenguaje de ensayo.
Distingue siempre lo esperado de lo que hayas observado.

Antes de escribir en el tenant, muestra el comando o el diff
y espera mi OK. No avances al siguiente paso por tu cuenta.

Revisa el contenido tras cada pull: las instrucciones no deben
quedar vacías. Conserva los cambios locales pendientes.
No edites manualmente .mcs/.

Confirma que la última entrada de practice/runs.json es stage
y coincide con este destino. Si no coincide, detente y explícame por qué.
Después esperarás /demo-00-preflight. No crees todavía el agente.
```

Ten preparados PowerPoint, el portal y `C:\Demos\circe-compras-copilot-studio\demo\data\inventario-demo.csv`. Copia una orden por paso en **Claude Code**, dentro de este repo. Son órdenes del proyecto, no del Preview ni órdenes propias de Copilot Chat. El modo escenario adapta su narración y omite tiempos y registros. No pegues también el prompt largo: queda como apoyo si necesitas una instrucción explícita.

**Antes de empezar con público, en Claude Code:**

```text
/demo-00-preflight
```

El script de Stage puede crear una plantilla de registro; en modo escenario no la rellenamos. Si el preflight está correcto, deja abierta esta conversación para comenzar la demo.

**La dinámica en cada bloque:** tú introduces el objetivo, copias la orden, Claude lo explica y prepara el trabajo, revisas el comando o el diff y das tu OK. Después enseñas el resultado y haces la conversación en Preview. Los textos de «Qué dices» son sugerencias; puedes decirlos con tus palabras.

### Presentación que acompaña esta guía

Usa **BizzSummit2026_Circe_Compras_v4.pptx**, de 24 diapositivas. Los números de esta guía indican la **posición real en PowerPoint**, contando la portada como 1. Mantén la guía en tu pantalla de apoyo y proyecta la PPT, VS Code o el portal según indique cada bloque.

### Apertura con público · diapositivas 1 a 4

Todavía no ejecutes `/demo-01-crear`. Abre el caso en PowerPoint:

| Diapositiva | Qué cuentas | Cuándo avanzas |
|---|---|---|
| **1 · Circe Compras, construida como código** | «Hoy vamos a construir un asistente de compras desde VS Code. Y después cambiaremos una regla para ver cómo se mantiene.» | Cuando el público tenga clara la idea de la sesión. |
| **2 · Gracias a nuestros sponsors** | Agradecimiento breve a quienes hacen posible el evento. | Sin detenerte en leer todos los logos. |
| **3 · Javier Armesto** | Preséntate y conecta tu trabajo en aplicaciones de negocio con el caso de Compras. | Tras explicar por qué te interesa este enfoque. |
| **4 · El recorrido** | Presenta Isla Eea, el inventario ficticio y las seis piezas que vamos a construir. «Circe preparará una propuesta. La decisión de compra sigue siendo humana.» | Abre la **5** para introducir la creación y entra en el bloque 1 de esta guía. |

<details>
<summary>Mapa completo: dónde encajan las 24 diapositivas</summary>

| PPT | Momento de la guía | Uso en escena |
|---|---|---|
| 1 | Apertura | Presentar el propósito |
| 2 | Apertura | Agradecer a patrocinadores |
| 3 | Apertura | Presentarte |
| 4 | Apertura | Explicar caso y recorrido |
| 5 | 1 · Crear | Introducir `/demo-01-crear` |
| 6 | 2 · Conocimiento | Introducir `/demo-02-politica` |
| 7 | 3 · Instrucciones | Introducir `/demo-03-ciclo` |
| 8 | 4 · Skill v1 | Introducir `/demo-04-skill` |
| 9 | 5 · Política v2 | Introducir `/demo-05-cambio` |
| 10 | 6 · Publicar | Introducir `/demo-06-publicar` |
| 11 | Después de la demo | Localizar las piezas en el repositorio |
| 12 | Después de la demo | Explicar cómo mantener el agente |
| 13 | Copilot Chat y subagentes | Presentar los cuatro especialistas |
| 14 | Copilot Chat y subagentes | Repartir responsabilidades |
| 15 | Copilot Chat y subagentes | Enseñar el selector de Copilot Chat |
| 16 | Copilot Chat y subagentes | Explicar la cadena de migrate |
| 17 | Copilot Chat y subagentes | Relacionar Manage con lo que acabamos de hacer |
| 18 | Copilot Chat y subagentes | Comparar Init y nuestro script |
| 19 | Copilot Chat y subagentes | Explicar la lectura del workspace con Describer |
| 20 | Copilot Chat y subagentes | Relacionar requisitos y piezas con Architect |
| 21 | Copilot Chat y subagentes | Mostrar otro punto de partida, sin ejecutarlo |
| 22 | Cierre y preguntas | Recuperar la idea principal |
| 23 | Cierre y preguntas | Abrir preguntas |
| 24 | Cierre y preguntas | Agradecer y mostrar el QR de feedback |

</details>

## 1. Crear el agente

**PPT 5 · Crear — antes de ejecutar la orden.** Introduce el cometido y los límites de Circe. Después pasa a **VS Code → Claude Code** y copia `/demo-01-crear`. Al terminar, muestra el workspace y el harness en el **portal**.

**Al terminar este bloque:** vuelve a PowerPoint y abre la **diapositiva 6** para introducir el siguiente paso.

**Qué dices:**

> Vamos a construir un asistente de compras desde VS Code. Empezamos por su cometido y sus límites, y después incorporaremos el conocimiento y el cálculo.

**En Claude Code · copia esta orden:**

```text
/demo-01-crear
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
Crea el agente de escenario usando scripts/New-Circe.ps1:
-Deploy
-Environment https://TU_ORGANIZACION.crm4.dynamics.com
-ProjectDir ./live-agents/circe-live
-Name "Circe Compras"
-SchemaName circe_compras

Muéstrame el comando antes de ejecutarlo.
Después, muestra las instrucciones y la plantilla del workspace.
Inicializa su Git, conserva la exclusión de .mcs/, excluye
.github/ y crea el commit "scaffold inicial".
No añadas conocimiento ni skills.
```

</details>

Revisa el destino y responde **«OK, ejecuta»**.

**Qué muestras:** instrucciones en `settings.mcs.yml`, commit inicial y harness en el portal.

**En Preview:**

```text
Hola, ¿qué puedes hacer y cuáles son tus límites?
```

Si menciona capacidades aún no instaladas, explica que describir su cometido no acredita su ejecución.

## 2. Incorporar el conocimiento de negocio

**PPT 6 · Conocimiento — antes de ejecutar la orden.** Explica que la política aporta las reglas de Compras. Pasa a **VS Code → Claude Code** y copia `/demo-02-politica`. Tras sincronizar, muestra el documento en el **portal** y pregunta por la revisión especial en Preview.

**Al terminar este bloque:** vuelve a PowerPoint y abre la **diapositiva 7** para introducir el siguiente paso.

**Qué dices:**

> Las instrucciones definen su función. La política de Compras aporta las reglas que debe consultar.

**En Claude Code · copia esta orden:**

```text
/demo-02-politica
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
Añade demo/data/politica-compras.md como conocimiento de fichero
subido al agente de escenario, usando add-knowledge de mcs-assistant.
Conserva el nombre politica-compras.md.

Haz el pull necesario y revisa que conserva las instrucciones,
template y language. Si pierde contenido, detente y muestra el diff.

Muestra los archivos generados y el diff antes del push.
Tras mi OK, sincroniza con Manage y guarda el commit "política v1".
```

</details>

**Qué muestras:** documento de política y conocimiento en `Ready`.

**En una conversación nueva de Preview:**

```text
¿Cuándo requiere revisión especial una propuesta de compra?
```

Puede buscarla o pedirla. Cuenta lo que suceda; el recorrido no necesita que falle.

## 3. Precisar el comportamiento

**PPT 7 · Comportamiento — antes de ejecutar la orden.** Introduce la diferencia entre disponer de conocimiento y dar una instrucción clara para consultarlo. Pasa a **VS Code**, copia `/demo-03-ciclo` y muestra el diff. Después abre una conversación nueva en **Preview**.

**Al terminar este bloque:** vuelve a PowerPoint y abre la **diapositiva 8** para introducir el siguiente paso.

**Qué dices:**

> Podemos hacer más explícito cuándo debe consultar la política. El cambio queda visible y podemos comprobar su efecto.

**En Claude Code · copia esta orden:**

```text
/demo-03-ciclo
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
En las instrucciones del agente de escenario, sustituye:
"Si no tienes la política, pídela."

Por:
"La política de compras está en tu conocimiento (politica-compras.md): búscala antes de responder sobre reglas. Pídela solo si la búsqueda no devuelve nada."

Añade al final:
"Si falta un dato obligatorio, nombra el campo y el artículo afectado."

Valida el YAML y muestra el diff de contenido.
Tras mi OK, crea el commit "instrucciones: política desde conocimiento"
y sincroniza con Manage. Conserva el resto de la configuración.
```

</details>

**Qué muestras:** las dos frases en el diff.

**En New chat de Preview:**

```text
¿Cuándo requiere revisión especial una propuesta de compra?
```

Después:

```text
¿Y una línea de 500 EUR exactos?
```

Muestra la búsqueda y explica el resultado observado: más de 500 EUR por línea, especial; exactamente 500, normal. Señala la diferencia entre tener un documento y dar una instrucción clara para consultarlo.

## 4. Incorporar la skill y preparar la reposición

**PPT 8 · Skill — antes de ejecutar la orden.** Presenta las piezas de la skill. Pasa a **VS Code**, copia `/demo-04-skill` y muestra su estructura. Después ve a **Preview**, adjunta el CSV y pide la reposición. Enseña el informe y las incidencias.

**Al terminar este bloque:** vuelve a PowerPoint y abre la **diapositiva 9** para introducir el siguiente paso.

**Qué dices:**

> Saber explicar la política está bien, pero Compras necesita preparar una reposición. Ahora añadimos una skill: el procedimiento, sus reglas y el script que calcula la propuesta.

**En Claude Code · copia esta orden:**

```text
/demo-04-skill
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
Prepara la skill v1 con scripts/build-kit.py.
Muéstrame brevemente SKILL.md, su description,
references/policy.json y scripts/replenishment.py.

Extrae demo/packages/circe-reposicion-v1.zip e importa su carpeta
en el workspace de escenario usando add-skill de mcs-assistant,
con nombre circe-reposicion.

Muestra los archivos nuevos antes del push.
Tras mi OK, crea el commit "skill v1" y sincroniza con Manage.
Revisa los cambios de metadatos posteriores y conserva el contenido.
```

</details>

**Qué muestras:** estructura de la skill y una sola `circe-reposicion` en el portal. La descripción ayuda a seleccionar la skill, sin garantizar su activación.

**En New chat, adjunta el CSV antes de enviar:**

```text
Prepara la reposición de los próximos siete días.
Aplica nuestra política y los lotes.
Devuelve un CSV y un informe breve con las incidencias que deba resolver.
```

Enseña el uso de la skill y los archivos descargables. Puede aparecer también `analyzing-csv`.

| Resultado v1 | Valor |
|---|---|
| Propuestas | A100, B200 y D400 |
| Total | 2.216,00 EUR |
| Revisión normal | A100: 500 EUR |
| Revisión especial | B200: 666 EUR; D400: 1.050 EUR |
| Incidencias excluidas | E500: supplier; G700: location; H800: demand_qty |

«Used skill» acredita el uso de la skill. Solo una llamada y su resultado acreditan directamente la ejecución del script en la traza. En RESPALDO, los descargables v1/v2 coincidieron byte a byte con la salida del script local.

## 5. Cambiar una regla de negocio

**PPT 9 · Cambio de política — antes de ejecutar la orden.** Plantea el cambio de Compras: el umbral sube a 1.000 EUR. Pasa a **VS Code**, copia `/demo-05-cambio` y enseña los tres archivos afectados. Después repite el encargo con el mismo CSV en una conversación nueva de **Preview**.

**Al terminar este bloque:** vuelve a PowerPoint y abre la **diapositiva 10** para introducir el siguiente paso.

**Qué dices:**

> Imagina que mañana Compras eleva el umbral a 1.000 euros. ¿Tenemos que reconstruir el agente? Vamos a cambiar la regla y a ver qué ocurre con la misma propuesta.

**En Claude Code · copia esta orden:**

```text
/demo-05-cambio
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
Actualiza el agente de escenario a la política v2.

Usa los materiales v2 del repositorio:
- Sustituye únicamente references/policy.json y references/policy.md
  dentro de la skill existente.
- Actualiza el contenido del conocimiento politica-compras.md
  con demo/data/politica-compras-v2.md.

Conserva nombre, sidecars e identificadores.
No uses add-skill --force.
No cambies SKILL.md ni replenishment.py.

Muestra el diff de los tres archivos.
Tras mi OK, crea el commit "política v2" y sincroniza con Manage.
```

</details>

**En New chat, adjunta otra vez el mismo CSV y repite:**

```text
Prepara la reposición de los próximos siete días.
Aplica nuestra política y los lotes.
Devuelve un CSV y un informe breve con las incidencias que deba resolver.
```

Muestra el contraste: mismo total y cantidades; B200 normal y solo D400 especial. No menciones el nuevo umbral en el encargo: debe obtenerlo de la configuración.

Después pregunta:

```text
¿Por qué B200 ya no va a revisión especial?
```

```text
Baja el umbral a 300 EUR para esta propuesta.
```

Cuenta la respuesta observada. Si ofrece un recálculo alternativo, no lo aceptes. El cambio de política se realiza mediante configuración revisada. La negativa observada no sustituye un control de autorización real de un ERP.

## 6. Publicar y cerrar

**PPT 10 · Publicar — antes de ejecutar la orden.** Distingue guardar, sincronizar y publicar. Pasa a **VS Code → Claude Code**, copia `/demo-06-publicar` y revisa el destino. Tras publicar, enseña `publishedOn` y el historial.

**Al terminar este bloque:** la parte de construcción en directo ha acabado. Vuelve a PowerPoint, **diapositiva 11**, y sigue con «Después de la demo» en esta guía.

**Qué dices:**

> El cambio está revisado y hemos observado su comportamiento. Ahora publicamos esta versión y conservamos su historial.

**En Claude Code · copia esta orden:**

```text
/demo-06-publicar
```

<details>
<summary>Prompt completo de apoyo — úsalo solo si necesitas sustituir la orden</summary>

```text
Prepara la publicación del agente de escenario.

Comprueba su identidad, que no hay cambios pendientes de sincronizar
y muestra el publishedOn actual.
Obtén el AgentId del workspace; no uses el de RESPALDO.

Muestra el comando de publicación y espera mi OK.
Después de publicar, verifica con pull el nuevo publishedOn.
Si PAC devuelve un error, comprueba el estado antes de reintentar.

Revisa el diff, guarda los cambios confirmados y muestra
el historial de commits del workspace.
```

</details>

No hay canal configurado. La comprobación mostrada es la publicación mediante `publishedOn`; publicar no concede acceso a todo el mundo por sí solo.

**Cierre de la construcción en directo:**

> Hemos construido un agente, incorporado conocimiento y una skill, y cambiado una regla de negocio. Desde VS Code podemos revisar esos cambios, conservar su historia y contrastar sus resultados. Copilot Studio es donde el agente se ejecuta.

## Después de la demo · las piezas y su mantenimiento

**Vuelve a PowerPoint después de publicar. Diapositivas 11 y 12.** Aquí ayudas al público a ordenar lo que acaba de ver.

### 11 · El repositorio: las piezas del agente

**Qué dices:**

> Si mañana alguien se incorpora al proyecto, ¿dónde encuentra cada cosa? Aquí están las instrucciones, la política, el procedimiento de cálculo y las órdenes que hemos utilizado.

Relaciona las carpetas con lo mostrado. Aclara que `/demo-*` son prompts guardados en este proyecto para conducir el trabajo, mientras que `mcs-assistant` aporta las capacidades del plugin. Si abres el explorador de VS Code, enseña solo esas carpetas y vuelve a la **12**.

### 12 · Mantener el agente

**Qué dices:**

> Hoy hemos cambiado un umbral. Si cambia la fórmula de cálculo, sabemos dónde revisarla. Y si queremos crear pedidos en el ERP, hará falta añadir la integración, sus permisos y su aprobación.

Recorre la tabla con un ejemplo. Cierra este bloque recordando que Circe llega hasta una propuesta revisable. **Avanza a la 13** para explicar quién puede ayudarnos a construir y mantener estas piezas.

## Copilot Chat y los cuatro subagentes

**PowerPoint · diapositivas 13 a 21.** Es el bloque sobre el plugin que quieres conservar. El recorrido principal usa las diapositivas y sus capturas, sin crear otro agente ni iniciar una migración.

**Transición:**

> Hasta aquí hemos visto el resultado. Ahora veamos cómo reparte el plugin el trabajo de construirlo y cómo aparece también en GitHub Copilot Chat.

| Diapositiva | Qué explicas de forma amena | Qué muestras o haces |
|---|---|---|
| **13 · Cuatro subagentes, un ciclo de vida** | «Podemos repartir el trabajo entre especialistas, cada uno con un cometido concreto.» | Presenta el bloque y avanza a la 14. |
| **14 · Cuatro especialistas con límites claros** | «Init arranca, Architect diseña, Manage sincroniza y publica, y Describer lee lo que hemos construido.» | Relaciona cada responsabilidad con una acción. Los límites escritos no sustituyen los permisos técnicos. |
| **15 · El mismo plugin, otro asistente** | «La demo la hemos conducido desde Claude Code. Aquí podéis ver los especialistas del plugin en el selector de GitHub Copilot Chat.» | Enseña la captura del selector. Si abres Copilot Chat, limita la visita a enseñar el selector ya preparado y vuelve a la 16. No instales ni actualices el plugin en escena. |
| **16 · /mcs-assistant:migrate** | «En una migración hay tareas encadenadas, pero sigue habiendo una persona que revisa el paso de una a otra.» | Explica la secuencia dibujada. No lances migrate: es una posibilidad adicional, fuera de la construcción de Circe. |
| **17 · Manage** | «Este es el especialista que nos ha acompañado al traer y enviar los cambios.» | Conecta pull, diff, push y publish con lo observado en la demo. No hace falta repetirlos. |
| **18 · Init** | «Init sirve para arrancar. Nuestro script prepara ese arranque con los valores de Circe.» | Usa la comparación de la diapositiva y aclara por qué has utilizado el script. |
| **19 · Describer** | «¿Podría alguien entender qué hace Circe leyendo su workspace? Ese es el trabajo que queremos mostrar aquí.» | Explica la lectura y el informe en lenguaje llano. Una ejecución en vivo es opcional, solo si estaba preparada y hay margen. Pide lectura, sin cambios ni sincronización. Si no la haces, sigue a la 20. |
| **20 · Architect** | «Un requisito de negocio puede acabar en una instrucción, conocimiento o una skill. La decisión depende de lo que necesitemos resolver.» | Recorre dos filas de la tabla y relaciónalas con la política y el cálculo de Circe. |
| **21 · Architect: otro punto de partida** | «También podemos empezar describiendo lo que necesitamos y revisar el diseño propuesto.» | Explica el recorrido como alternativa para explorar después. No ejecutes los comandos de la diapositiva ni uses Arch01 o RESPALDO. |

**Si vas justo de tiempo:** muestra 13, 14 y 15, conecta brevemente Manage en la 17 y termina con Describer en la 19. Deja 16, 18, 20 y 21 como ampliación y salta a la **22**. Es un recorte del bloque, no otro recorrido técnico.

## Cierre y preguntas

**PowerPoint · diapositivas 22 a 24.** Ya no hay más órdenes de demo.

### 22 · Para llevarse

> Hemos visto dónde vive cada decisión: la política aporta las reglas, la skill prepara el cálculo y la persona revisa la propuesta. Desde VS Code podemos construir estas piezas, leer sus cambios y conservar su historia.

Conecta la conclusión con el cambio de B200 que acaban de ver. Evita repasar todos los comandos otra vez.

### 23 · ¿Alguna pregunta?

Abre preguntas. Si necesitas volver a una pieza concreta, usa el mapa de diapositivas de «Preparación y apertura». No hagas nuevos cambios en el agente por una sugerencia del público.

### 24 · Gracias y feedback

Agradece la asistencia y deja visible el QR de feedback para que puedan escanearlo. Con esto termina la sesión.

## Si necesitas el respaldo

Si has preparado un respaldo propio, ábrelo, inicia un chat nuevo y adjunta el CSV con el encargo de reposición. Explica que continúas con la versión preparada, que ya utiliza la política v2. No la devuelvas a v1 en escena. Para mostrar el antes/después, utiliza los descargables o capturas v1 guardados.

Si preparas un respaldo propio, verifica su publicación y su política antes de usarlo. Requiere tu conexión y autenticación. Conserva los resultados ficticios de referencia como alternativa local.

## Qué explicar mientras trabaja la herramienta

- **Creación:** «Aquí hay dos asistentes con trabajos distintos: Claude nos ayuda a construir; Circe atenderá las preguntas y encargos de Compras.»
- **Conocimiento:** «¿Dónde cambiaríais una regla de Compras? Vamos a localizar el documento que la recoge y la instrucción que pide consultarlo.»
- **Skill:** «Pensad en los lotes: si necesito 32 unidades y el proveedor vende de 12 en 12, necesito un procedimiento que respete esa regla.»
- **Cambio:** «Antes de enviar el cambio, podemos leer exactamente qué hemos modificado. El diff nos permite revisar una regla pequeña sin recorrer toda la configuración.»
- **Publicación:** «Este historial cuenta cómo hemos construido Circe: cometido, conocimiento, procedimiento y una nueva regla de negocio.»

Durante una espera, mantén la diapositiva del paso actual o el estado de la operación a la vista. Reserva las diapositivas 13 a 21 para el bloque de Copilot Chat y subagentes, después de la demo, para conservar el hilo. Si recurres a RESPALDO, muestra el resultado v2 con la diapositiva 9 y retoma la explicación en la 11; no publiques ni modifiques el respaldo.

