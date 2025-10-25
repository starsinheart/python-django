@echo off
echo ========================================
echo    ИСПРАВЛЕНИЕ БАЗЫ ДАННЫХ STUD
echo ========================================
echo.

echo Переход в директорию проекта...
cd /d "%~dp0STUD"

echo.
echo Остановка всех процессов Python...
taskkill /f /im python.exe 2>nul
taskkill /f /im pythonw.exe 2>nul

echo.
echo Ожидание 3 секунды...
timeout /t 3 /nobreak >nul

echo.
echo Удаление базы данных...
if exist db.sqlite3 (
    del /f /q db.sqlite3
    echo База данных удалена
) else (
    echo База данных не найдена
)

echo.
echo Удаление файлов миграций...
if exist account\migrations\*.py (
    del /f /q account\migrations\*.py
    echo Миграции account удалены
)

if exist my_site\migrations\*.py (
    del /f /q my_site\migrations\*.py
    echo Миграции my_site удалены
)

echo.
echo Создание новых миграций...
python manage.py makemigrations account
python manage.py makemigrations my_site

echo.
echo Применение миграций...
python manage.py migrate

echo.
echo Создание суперпользователя...
python manage.py createsuperuser

echo.
echo ========================================
echo    БАЗА ДАННЫХ ИСПРАВЛЕНА!
echo ========================================
echo.
echo Запуск сервера...
python manage.py runserver

