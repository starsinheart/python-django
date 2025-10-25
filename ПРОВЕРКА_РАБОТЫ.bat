@echo off
echo ========================================
echo    ПРОВЕРКА РАБОТЫ САЙТА STUD
echo ========================================
echo.

echo Переход в директорию проекта...
cd /d "%~dp0STUD"

echo.
echo Проверка запуска сервера...
echo.

echo Запуск сервера в фоновом режиме...
start /b python manage.py runserver 127.0.0.1:8000

echo.
echo Ожидание 10 секунд для запуска сервера...
timeout /t 10 /nobreak >nul

echo.
echo Проверка доступности сайта...
ping -n 1 127.0.0.1 >nul

if %errorlevel% equ 0 (
    echo Сайт доступен!
    echo Открытие браузера...
    start http://127.0.0.1:8000/
) else (
    echo Сайт недоступен!
    echo Проверьте настройки сети
)

echo.
echo Для остановки сервера нажмите любую клавишу...
pause

echo Остановка сервера...
taskkill /f /im python.exe 2>nul

