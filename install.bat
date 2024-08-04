@echo off
REM Copyright (c) 2024 ParamXploit (Param)
REM This is free software, licensed under the MIT License.
REM See /LICENSE for more information.

REM Check for Python installation
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.10 or higher from https://www.python.org.
    exit /b 1
)

REM Upgrade pip and install Python packages
echo Upgrading pip and installing Python packages...
pip install --upgrade pip
pip install -r requirements.txt

REM Install Nmap
echo Installing Nmap...
if not exist "%ProgramFiles%\Nmap" (
    powershell -Command "Invoke-WebRequest -Uri 'https://nmap.org/dist/nmap-7.93-setup.exe' -OutFile 'nmap-setup.exe'"
    start /wait nmap-setup.exe /S
    del nmap-setup.exe
)

REM Install Nikto
echo Installing Nikto...
if not exist "%ProgramFiles%\Nikto" (
    powershell -Command "Invoke-WebRequest -Uri 'https://cirt.net/nikto/nikto-2.1.6.zip' -OutFile 'nikto.zip'"
    powershell -Command "Expand-Archive -Path 'nikto.zip' -DestinationPath '%ProgramFiles%'"
    del nikto.zip
)

REM Install Git
echo Installing Git...
if not exist "%ProgramFiles%\Git" (
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe' -OutFile 'git-setup.exe'"
    start /wait git-setup.exe /VERYSILENT /NORESTART
    del git-setup.exe
)

REM Clone the ParamXploit repository
echo Cloning ParamXploit repository...
if not exist "%CD%\ParamXploit" (
    git clone https://github.com/yourusername/ParamXploit.git
)

REM Create a symbolic link for the main script
echo Creating symbolic link...
mklink "%ProgramFiles%\ParamXploit\paramxploit.py" "%CD%\ParamXploit\paramxploit.py"

REM Clone additional tools
echo Cloning dirsearch...
git clone --depth 1 https://github.com/maurosoria/dirsearch.git "%USERPROFILE%\.local\share\dirsearch"

echo Installation complete. You can now run ParamXploit by executing paramxploit.py from the ParamXploit directory.
