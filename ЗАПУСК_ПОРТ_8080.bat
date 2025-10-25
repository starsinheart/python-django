@echo off
echo ========================================
echo    ЗАПУСК САЙТА STUD НА ПОРТУ 8080
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

echo.
echo Создание суперпользователя...
python manage.py createsuperuser

echo.
echo ========================================
echo    САЙТ ГОТОВ К РАБОТЕ!
echo ========================================
echo.
echo Открытие браузера через 5 секунд...
echo Адрес сайта: http://127.0.0.1:8080/
echo.
echo Для остановки сервера нажмите Ctrl+C
echo.

timeout /t 5 /nobreak >nul

echo Открытие браузера...
start http://127.0.0.1:8080/

echo.
echo Запуск сервера на порту 8080...
python manage.py runserver 127.0.0.1:8080

