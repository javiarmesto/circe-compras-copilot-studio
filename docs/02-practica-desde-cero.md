# Practicar desde cero

Completa antes [la instalación](01-setup-vscode.md). Trabaja en la raíz del repositorio con tu propio entorno.

## Preparar una pasada nueva

```powershell
$CirceEnvironment = 'https://TU_ORGANIZACION.crm4.dynamics.com'
.\scripts\New-PracticeRun.ps1 -Environment $CirceEnvironment
```

Sustituye la URL de ejemplo. Cada pasada prepara un nombre y una carpeta propios; el agente se crea al ejecutar el paso 1. Revisa la entrada de `practice/runs.json` antes de seguir.

En Claude Code, pide que lea `CLAUDE.md` y use la pasada recién preparada. Ejecuta las órdenes `/demo-00-preflight` a `/demo-06-publicar` siguiendo [el recorrido](03-demo-paso-a-paso.md). Las guías HTML ofrecen prompts alternativos y botones de copia.

## Preparar una sesión

Con `New-PracticeRun.ps1 -Stage` se preparan el nombre `Circe Compras`, schema `circe_compras` y workspace `live-agents/circe-live`. Comprueba antes que no colisionen con un agente existente. No borres una práctica anterior para empezar otra si puedes usar un destino nuevo.

Si quieres un respaldo, prepara y verifica un agente propio antes de la sesión. No se distribuye ninguno. Un push actualiza el borrador; publicar es una acción separada.

## Limpieza opcional

`Reset-Practice.ps1` puede borrar workspaces locales. Lee su ayuda y revisa los destinos y los cambios pendientes antes de ejecutarlo. No forma parte obligatoria del inicio. Las eliminaciones en el tenant requieren revisar y confirmar cada destino.

No subas la carpeta `practice/`, workspaces conectados, perfiles ni registros de tenant al repositorio.
