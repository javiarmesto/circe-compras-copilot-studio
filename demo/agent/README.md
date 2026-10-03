# Plantilla del agente

`instructions.md` es la identidad que se pasa a PAC o se pega en el portal. La plantilla completa combina estas instrucciones, la política y la skill empaquetada por `scripts/build-kit.py`.

El workspace YAML del agente se crea con el scaffold real de PAC. No se distribuyen GUID inventados ni un ZIP que se haga pasar por solución exportada. `scripts/New-Circe.ps1` usa `pac copilot init --authoring-mode cli-copilot`, documentado por Microsoft, y mantiene el estado de sincronización generado por la herramienta.

El paquete `circe-reposicion.zip` sí es una skill para importar, con `SKILL.md` en la raíz. Una skill ZIP y una solución de Power Platform son artefactos diferentes.

Después de crear el agente, añadir la política como conocimiento y cargar la skill desde Build > Skills. Si el plugin CAT soporta ese cambio en tu versión, puede automatizarlo siguiendo `demo/prompts/02-build.md`. Revisar siempre los archivos reales del scaffold antes de editar.

Estado inicial: plantilla preparada; bootstrap, importación de skill y ejecución conversacional pendientes de ensayo en el tenant.
