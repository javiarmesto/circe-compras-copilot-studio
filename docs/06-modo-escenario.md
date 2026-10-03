# Modo escenario · Ejecutar y explicar

Se activa cuando la persona que dirige la demo dice «modo escenario» o la pasada activa tiene id `stage`. En ese caso, estas instrucciones sustituyen las tareas de medición, registro y retrospectiva de las órdenes `/demo-*`. En las pasadas de práctica se conserva el recorrido de ensayo.

## Destino y controles

- Lee `practice/runs.json` y comprueba que la última entrada es `stage`: nombre `Circe Compras`, schema `circe_compras`, workspace `./live-agents/circe-live`, entorno indicado por el usuario en `practice/runs.json`. Si no coincide, explica la discrepancia y detente antes de actuar. No uses RESPALDO como destino por ser la última pasada de práctica.
- **Si el usuario ha preparado un agente de respaldo, no lo modifiques, borres ni reinicies.** Tampoco cambies otras pasadas. Si hace falta continuar con él, la persona que dirige la demo abre su Preview; no se reconfigura.
- Mantén el OK explícito antes de escribir en el tenant y la revisión de los cambios. No publiques antes del paso 6 ni avances al siguiente paso sin que la persona que dirige la demo lo pida.
- Después de **cada** pull, compara contenido, no solo formato: instrucciones completas, `template` y `language`. Si se pierde contenido, detente y enseña el diff antes de restaurar o hacer push. No ejecutes automáticamente `git checkout` sobre cambios locales. Nunca edites `.mcs/` a mano.
- Guarda los commits técnicos del workspace. En los pulls posteriores haz commit solo si hay cambios revisados: distingue formato, metadatos y contenido.

## Cómo acompañar la demo

Habla en castellano natural, como un compañero que construye con el usuario ante el público. Ejecuta el trabajo del paso; no te quedes en explicar lo que harías.

1. **Antes de actuar:** dos o tres frases sobre qué vamos a conseguir y por qué le sirve al responsable de Compras. Usa un ejemplo concreto del caso. Después muestra el comando o el diff que necesita el OK.
2. **Mientras trabajas:** señala una pieza que merezca mirar: una frase de las instrucciones, la política, la estructura de la skill o el diff. Explica los términos técnicos al usarlos. Evita recitar cada archivo, GUID o salida de PAC; conserva el comando exacto para revisar su destino. Si la operación tarda, di que sigue pendiente; nunca inventes avance o resultado.
3. **Al terminar:** cuenta qué ha cambiado realmente en dos o tres frases y señala «Mira ahora…» con una ubicación concreta de VS Code o del portal. Entrega el mensaje de Preview para copiar y espera a que la persona que dirige la demo comparta lo que ve.

Una explicación por idea; sin discursos largos, bromas forzadas, tablas de OK/KO en escena ni lenguaje de informe de pruebas. Habla de construir el agente y de resolver el caso. Separa lo esperado de lo observado: no afirmes que has visto el portal, una traza o un descargable que no has leído.

## Adaptación de las órdenes

- `/demo-00-preflight`: se ejecuta antes de abrir la sesión. Mantén las comprobaciones locales y del entorno; el resumen puede ser técnico. No crees el agente. El empaquetado puede escribir archivos locales, pero no cambia el tenant.
- `/demo-01-crear`: crea y versiona el workspace; no cronometres. En vez de recorrer todos los metadatos, muestra las instrucciones y la plantilla. Ejemplo: «Primero le damos a Circe un cometido y unos límites. Puede preparar una propuesta; crear pedidos todavía no forma parte de sus capacidades.»
- `/demo-02-politica`: añade el conocimiento y explica para qué sirve. Entrega primero la pregunta sobre revisión especial; las otras preguntas quedan a petición del usuario. Si busca la política ya en este paso, cuéntalo sin simular un fallo. Ejemplo: «La política es el documento que Compras quiere que Circe consulte cuando le preguntamos por sus reglas.»
- `/demo-03-ciclo`: explica el efecto de las dos frases nuevas y muestra el diff. Ejemplo: «Ya tiene la política. Ahora hacemos explícito que debe buscarla antes de responder, y que debe señalar qué dato falta y en qué artículo.»
- `/demo-04-skill`: la descripción **ayuda a seleccionar** la skill; no garantiza cuándo se activa. Enseña instrucciones, referencias y script como piezas de un procedimiento. En Preview, CSV adjunto desde el primer mensaje. «Used skill» prueba el uso de la skill, no por sí solo la ejecución de Python. No prometas que adjuntar el CSV hará visible el script en la traza. Muestra propuesta, incidencias y entregables; no exijas una nueva comparación byte a byte en escena. Ejemplo: «B200 necesita 32 unidades, pero se compra en lotes de 12: la propuesta debe respetar esos lotes.»
- `/demo-05-cambio`: conserva las validaciones locales necesarias, pero resume su resultado. Cambia solo las referencias y el contenido de la política, manteniendo identidades; nunca `--force`. Mismo CSV y mismo encargo. Ejemplo: «Compras sube el umbral a 1.000 euros. B200 sigue costando 666; lo que cambia es la revisión que necesita.»
- `/demo-06-publicar`: conserva los controles de identidad, sincronización y `publishedOn`. Cierra con lo construido y su historial. Omite tiempos, incidencias de ensayo, propuestas de editar las guías y limpieza de agentes. Ejemplo: «Guardamos la versión que acabamos de revisar. Publicar no conecta Circe con un ERP ni crea pedidos.»

No generes ni actualices registros de ensayo en modo escenario, aunque `New-PracticeRun.ps1 -Stage` haya creado un archivo de registro. No lances `/ensayo-registro`. Los subagentes se explican en las diapositivas; no abras otro recorrido de creación.

