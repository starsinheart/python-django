@echo off
echo ========================================
echo    ЗАПУСК САЙТА STUD С БРАУЗЕРОМ
echo ========================================
echo.

echo Переход в директорию проекта...
cd /d "%~dp0STUD"

echo.
echo Остановка процессов Python...
taskkill /f /im python.exe 2>nul
taskkill /f /im pythonw.exe 2>nul

echo.
echo Ожидание 3 секунды...
timeout /t 3 /nobreak >nul

echo.
echo Удаление старой базы данных...
if exist db.sqlite3 del /f /q db.sqlite3

echo.
echo Применение миграций...
python manage.py migrate

if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось применить миграции!
    pause
    exit /b 1
)

echo.
echo Создание суперпользователя...
python manage.py createsuperuser

if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось создать суперпользователя!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    САЙТ ГОТОВ К РАБОТЕ!
echo ========================================
echo.
echo Открытие браузера через 5 секунд...
echo Адрес сайта: http://127.0.0.1:8000/
echo.
echo Для остановки сервера нажмите Ctrl+C
echo.

timeout /t 5 /nobreak >nul

echo Открытие браузера...
start http://127.0.0.1:8000/

echo.
echo Запуск сервера...
python manage.py runserver 127.0.0.1:8000

