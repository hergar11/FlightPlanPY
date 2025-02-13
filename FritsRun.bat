@echo off
setlocal

REM Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"
    if %errorlevel% neq 0 (
        echo Failed to download or install Python.
        exit /b 1
    )
    echo Python installed successfully.
) else (
    echo Python is installed.
)
REM Install python Dependencies
echo Installing python dependencies...

pip install --upgrade pip

pip install -r %~dp0PythonDependencies\dependencies.txt --no-input

echo End of Installing python dependencies.
REM CleanUp
echo Press Enter to exit...
pause >nul