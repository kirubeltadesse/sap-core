:: Install choco .exe and add choco to PATH
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

:::: Dev tools
choco install wsl2 git slack -fy
choco install docker -fy
choco install docker-desktop


:::: Text editors / IDEs
choco install vscode -fy

:::: Removing uninstalled package
::choco uninstall wsl git slack docker vscode -fy
