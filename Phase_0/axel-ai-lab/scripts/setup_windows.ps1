$ErrorActionPreference = "Stop"

Write-Host "Checking Python..."

if (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonCommand = "py"
    $PythonArgs = @("-3.13")
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCommand = "python"
    $PythonArgs = @()
}
else {
    throw "Python was not found. Install Python 3.13 or newer first."
}

& $PythonCommand @PythonArgs -c @"
import sys

required = (3, 13)

if sys.version_info < required:
    raise SystemExit(
        f"Python 3.13+ required. Found {sys.version.split()[0]}"
    )

print(f"Python {sys.version.split()[0]} detected.")
"@

Write-Host ""
Write-Host "Creating virtual environment..."

& $PythonCommand @PythonArgs -m venv .venv

Write-Host ""
Write-Host "Installing Axel AI Lab..."

& ".\.venv\Scripts\python.exe" `
    -m pip install --upgrade pip

& ".\.venv\Scripts\python.exe" `
    -m pip install -e ".[dev,tools]"

if (-not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "Creating .env from .env.example..."

    Copy-Item `
        ".env.example" `
        ".env"
}

Write-Host ""
Write-Host "Setup complete."
Write-Host ""
Write-Host "Activate with:"
Write-Host ".\.venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "Then run:"
Write-Host "axel-ai-lab --verbose"