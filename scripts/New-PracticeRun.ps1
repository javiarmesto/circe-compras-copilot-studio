<#
.SYNOPSIS
  Prepara una pasada de práctica nueva: nombre y schema únicos, carpeta de workspace,
  registro de ensayo y los prompts de Claude Code con los valores ya puestos.

.DESCRIPTION
  Cada pasada crea un agente distinto (Circe Compras P01, P02...), así no dependes de
  borrar el anterior ni de esperar a que Dataverse lo libere. Con -Stage prepara los
  valores definitivos de la sesión (Circe Compras / circe_compras).

.EXAMPLE
  $CirceEnvironment = 'https://TU_ORGANIZACION.crm4.dynamics.com'
  ./scripts/New-PracticeRun.ps1 -Environment $CirceEnvironment
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory)][string]$Environment,
  [switch]$Stage
)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot
$state = Join-Path $root 'practice\runs.json'
New-Item -ItemType Directory (Join-Path $root 'practice') -Force | Out-Null
$runs = @(); if (Test-Path $state) { $runs = @(Get-Content $state -Raw | ConvertFrom-Json) }

if ($Stage) {
  $id = 'stage'; $name = 'Circe Compras'; $schema = 'circe_compras'; $dir = './live-agents/circe-live'
} else {
  $n = @($runs | Where-Object { $_.id -like 'p*' }).Count + 1
  $id = 'p{0:D2}' -f $n
  $name = "Circe Compras P{0:D2}" -f $n
  $schema = "circe_compras_p{0:D2}" -f $n
  $dir = "./live-agents/$id"
}
$run = [pscustomobject]@{ id = $id; name = $name; schema = $schema; projectDir = $dir; environment = $Environment; created = (Get-Date -Format s) }
ConvertTo-Json -InputObject @($runs + $run) -Depth 3 | Set-Content $state -Encoding utf8

$reg = Join-Path $root "evidence\tenant\registro-$id-$(Get-Date -Format yyyy-MM-dd).md"
New-Item -ItemType Directory (Split-Path $reg) -Force | Out-Null
Copy-Item (Join-Path $root 'templates\registro-ensayo.md') $reg -Force

$env:CirceEnvironment = $Environment
$env:CirceRunName = $name; $env:CirceRunSchema = $schema; $env:CirceRunDir = $dir

Write-Host ""
Write-Host "Pasada $id preparada" -ForegroundColor Cyan
Write-Host "  Agente:    $name"
Write-Host "  Schema:    $schema"
Write-Host "  Workspace: $dir"
Write-Host "  Registro:  $reg"
Write-Host ""
Write-Host "Prompt para Claude Code (creación, paso 3 de docs/03):" -ForegroundColor Cyan
@"
Vamos a crear el agente "$name" en el entorno $Environment desde este repo.
Usa scripts/New-Circe.ps1 con -Deploy -Environment $Environment -ProjectDir $dir, y nombre "$name" con schema $schema.
Si el script no admite nombre o schema como parámetros, usa directamente pac copilot init --name "$name" --schema-name $schema --publisher-prefix circe --authoring-mode cli-copilot --environment $Environment --project-dir $dir --instructions con el contenido de demo/agent/instructions.md.
Antes de ejecutar nada, enséñame el comando exacto y espera mi OK.
Después: explícame el workspace, confirma que settings.mcs.yml usa una plantilla cliagent-, inicializa git dentro de $dir y haz commit "scaffold inicial".
"@ | Write-Host