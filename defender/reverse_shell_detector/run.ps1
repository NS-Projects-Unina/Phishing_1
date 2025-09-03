# Custom "Reverse Shell" Detector for Windows

param(
    # Processes to exclude from detection
    [string[]]$ExcludedProcesses = @("explorer.exe", "svchost.exe", "System"),
    # Destination ports to watch for reverse shells
    [int[]]$WatchPorts = @(4444, 5555, 6666),
    # Path to write the detection log
    [string]$LogPath = "C:\Logs\ReverseShellDetection.csv",
    # Interval between scans in seconds
    [int]$IntervalSeconds = 10
)

# Prompt user for AutoKill option
$autoKillResponse = Read-Host "Vuoi abilitare l'autokill dei processi sospetti? (S/N)"
$AutoKill = $false
if ($autoKillResponse -match '^[sS]') {
    $AutoKill = $true
    Write-Host "AutoKill abilitato: i processi sospetti verranno terminati." -ForegroundColor Yellow
} else {
    Write-Host "AutoKill disabilitato: i processi sospetti non verranno terminati automaticamente." -ForegroundColor Green
}

# Ensure log directory exists
$logDir = Split-Path $LogPath
if (!(Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force }

Write-Host "Avvio monitoraggio reverse shell. Controllo ogni $IntervalSeconds secondi..." -ForegroundColor Cyan

while ($true) {
    # Retrieve active network connections on specified ports
    $connections = Get-NetTCPConnection | Where-Object {
        $_.State -eq 'Established' -and $WatchPorts -contains $_.RemotePort
    }

    # Collect suspicious entries for this cycle
    $suspicious = @()
    foreach ($conn in $connections) {
        try {
            $proc = Get-Process -Id $conn.OwningProcess -ErrorAction Stop
        } catch {
            continue
        }
        if ($ExcludedProcesses -notcontains $proc.ProcessName) {
            $entry = [PSCustomObject]@{
                Time         = Get-Date
                ProcessName  = $proc.ProcessName
                PID          = $proc.Id
                LocalAddress = "$($conn.LocalAddress):$($conn.LocalPort)"
                RemoteAddress= "$($conn.RemoteAddress):$($conn.RemotePort)"
            }
            $suspicious += $entry

            # Log to CSV
            $entry | Export-Csv -Path $LogPath -Append -NoTypeInformation

            # Auto kill if user opted in
            if ($AutoKill) {
                try {
                    Stop-Process -Id $proc.Id -Force -ErrorAction Stop
                    Write-Host "[KILLED] $($proc.ProcessName) PID $($proc.Id)" -ForegroundColor Red
                } catch {
                    Write-Host "[ERROR] Impossibile terminare PID $($proc.Id): $_" -ForegroundColor Magenta
                }
            } else {
                Write-Host "[ALERT] $($proc.ProcessName) PID $($proc.Id) connesso a $($conn.RemoteAddress):$($conn.RemotePort)" -ForegroundColor Yellow
            }
        }
    }

    if ($suspicious.Count -gt 0) {
        Write-Host "Trovate $($suspicious.Count) connessioni sospette. Log aggiornato in $LogPath." -ForegroundColor Yellow
    } else {
        Write-Host "Nessuna connessione sospetta rilevata in questo ciclo." -ForegroundColor Green
    }

    # Wait before next iteration
    Start-Sleep -Seconds $IntervalSeconds
}
