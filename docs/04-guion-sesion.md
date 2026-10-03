# Guion de la sesión · Circe Compras

## La pregunta de negocio

Compras necesita saber qué reponer para los próximos siete días y qué incidencias resolver. La propuesta debe respetar lotes y una política que puede cambiar.

## Recorrido principal

1. Crear un agente desde VS Code y explicar su cometido y sus límites.
2. Incorporar la política como conocimiento.
3. Ajustar las instrucciones para que consulte la política antes de responder.
4. Incorporar la skill: instrucciones, referencias y script de cálculo.
5. Procesar el CSV y revisar propuestas e incidencias.
6. Cambiar el umbral de 500 a 1000 EUR y repetir el mismo encargo.
7. Publicar la versión revisada si el usuario decide hacerlo.

El total y las cantidades se mantienen: cambia la revisión requerida para B200. La decisión humana sigue siendo necesaria y no se crean pedidos.

Usa la [guía HTML principal](05-demo-en-escenario.html) para copiar las órdenes y los prompts. Ejecuta las órdenes desde el repositorio `circe-compras-copilot-studio`.

## Complemento: GitHub Copilot Chat

La [mini demo](08-mini-demo-copilot-chat.html) presenta los especialistas de mcs-assistant. Crea un destino independiente y comprueba antes la compatibilidad de cada agente con tu versión del plugin. El runtime de Copilot Studio y la superficie de autoría de GitHub Copilot Chat tienen responsabilidades distintas.

## Qué demuestra el material

Se pueden revisar y versionar las piezas del agente desde VS Code y contrastar su comportamiento en Copilot Studio. Una regla docente no constituye un sistema de permisos. El uso visible de una skill no demuestra por sí solo que se haya ejecutado un comando Python concreto.

Si preparas un respaldo, verifica su versión y explica cuándo continúas con él. No se incluye un agente publicado en este repositorio.
