$root = "C:\Users\syedr\OneDrive\Documents\PR1"
$backendDir = Join-Path $root "backend"
$frontendDir = Join-Path $root "frontend"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$backendDir'; python -m uvicorn app.main:app --host 127.0.0.1 --port 8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$frontendDir'; npm run dev"

Write-Host "SmartHire is starting..."
Write-Host "Frontend: http://127.0.0.1:5173/"
Write-Host "Backend docs: http://127.0.0.1:8000/docs"
