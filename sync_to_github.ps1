$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $PSScriptRoot

git rev-parse --is-inside-work-tree *> $null
if ($LASTEXITCODE -ne 0) {
    throw "A pasta do Seu Treino não é um repositório Git."
}

git remote get-url origin *> $null
if ($LASTEXITCODE -ne 0) {
    throw "O repositório remoto origin não está configurado."
}

$changes = git status --porcelain --untracked-files=all
if (-not $changes) {
    exit 0
}

git add --all
if ($LASTEXITCODE -ne 0) {
    throw "Não foi possível preparar as alterações do Seu Treino."
}

git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    exit 0
}
if ($LASTEXITCODE -ne 1) {
    throw "Não foi possível verificar as alterações preparadas."
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto-save: $timestamp" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
if ($LASTEXITCODE -ne 0) {
    throw "Não foi possível salvar as alterações em um commit."
}

git push origin main
if ($LASTEXITCODE -ne 0) {
    throw "O commit local foi criado, mas não foi possível enviá-lo ao GitHub."
}
