<#
.SYNOPSIS
  Deja el equipo listo para practicar desde cero: borra workspaces locales de práctica,
  regenera los paquetes de la skill y lista los agentes de práctica del entorno.

.DESCRIPTION
  No borra nada en el tenant por sí solo. Los agentes de práctica (circe_compras_pNN)
  se listan para que los borres desde el portal o con Claude Code, revisando antes el
  comando. Cada pasada nueva usa un nombre distinto, así que no hace falta esperar.

.EXAMPLE
  ./scripts/Reset-Practice.ps1 -Environment $CirceEnvironment            # todas las pasadas
  ./scripts/Reset-Practice.ps1 -Environment $CirceEnvironment -Run p03   # solo una
#>
[CmdletBinding(SupportsShouldProcess)]
param(
  [Parameter(Mandatory)][string]$Environment,
  [string]$Run,
  [switch]$IncludeStage
)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot
$live = Join-Path $root 'live-agents'

$targets = @()
if (Test-Path $live) {
  $targets = Get-ChildItem $live -Directory | Where-Object {
    ($Run -and $_.Name -eq $Run) -or (-not $Run -and ($_.Name -like 'p*' -or ($IncludeStage -and $_.Name -eq 'circe-live')))
  }
}
foreach ($t in $targets) {
  if ($PSCmdlet.ShouldProcess($t.FullName, 'Borrar workspace local')) { Remove-Item $t.FullName -Recurse -Force; Write-Host "Borrado local: $($t.Name)" }
}
Remove-Item (Join-Path $root 'build') -Recurse -Force -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "Regenerando paquetes de la skill..." -ForegroundColor Cyan
$env:PYTHONUTF8 = 1
[Console]::OutputEncoding = [Text.Encoding]::UTF8   # Python writes UTF-8; without this the console garbles accents
Push-Location $root; python scripts/build-kit.py | Out-Host; Pop-Location

Write-Host ""
Write-Host "Agentes de práctica que siguen en el entorno:" -ForegroundColor Cyan
$list = pac copilot list --environment $Environment 2>&1
$hits = $list | Select-String -Pattern 'circe_compras'
if ($hits) { $hits | ForEach-Object { Write-Host "  $($_.Line.Trim())" } } else { Write-Host '  ninguno' }
Write-Host ""
Write-Host "Para borrarlos: portal de Copilot Studio, o en Claude Code:" -ForegroundColor Cyan
Write-Host '  "Borra los agentes circe_compras_pNN del entorno con pac copilot-studio delete. Enséñame antes la ayuda del comando y cada comando, y espera mi OK."'