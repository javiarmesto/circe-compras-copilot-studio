[CmdletBinding()]
param(
    [switch]$Deploy,
    [string]$Environment,
    [string]$ProjectDir = './live-agents/circe',
    [string]$Name = 'Circe Compras',
    [string]$SchemaName = 'circe_compras'
)
$ErrorActionPreference = 'Stop'
$CirceRepo = Split-Path -Parent $PSScriptRoot
if (-not (Get-Command pac -ErrorAction SilentlyContinue)) { throw 'Instala Power Platform CLI. Consulta docs/01-setup-vscode.md.' }
$CirceHelp = (& pac copilot init --help 2>&1 | Out-String)
# --help exits 1 because --name is missing, so check the help text, not the exit code.
if ($CirceHelp -notmatch 'authoring-mode') { throw 'Esta versión de PAC no anuncia authoring-mode. Actualiza y revisa la ayuda.' }
if ((Test-Path -LiteralPath $ProjectDir) -and (Get-ChildItem -LiteralPath $ProjectDir -Force | Select-Object -First 1)) { throw 'El directorio de destino no está vacío. Usa otro o clona el agente existente.' }
# pac splits --instructions at each line break ('Parse failed on: <second line>'), so pass a single line.
$CirceInstructions = ((Get-Content -Raw -Encoding UTF8 (Join-Path $CirceRepo 'demo/agent/instructions.md')) -replace '\s*\r?\n\s*', ' ').Trim()
$CirceArgs = @('copilot','init','--name',$Name,'--publisher-prefix','circe','--schema-name',$SchemaName,'--authoring-mode','cli-copilot','--project-dir',$ProjectDir,'--instructions',$CirceInstructions)
if ($Deploy) {
    if ([string]::IsNullOrWhiteSpace($Environment) -or $Environment -match 'TU_|ID_REAL|<') { throw 'Indica el entorno real de demo con -Environment.' }
    Write-Host "Se creará Circe y su solución en el entorno indicado: $Environment"
    $CirceArgs += @('--environment',$Environment)
} else { Write-Host 'Scaffold local. No crea recursos en Dataverse.' }
& pac @CirceArgs
if ($LASTEXITCODE -ne 0) { throw "PAC terminó con código $LASTEXITCODE. Conserva los archivos para revisar el error antes de reintentar." }
Write-Host 'Workspace creado por PAC. Completa conocimiento y skill según docs/03-demo-paso-a-paso.md.'
