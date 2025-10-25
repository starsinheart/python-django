@echo off
echo ========================================
echo    ПОЛНОЕ ПЕРЕСОЗДАНИЕ ПРОЕКТА STUD
echo ========================================
echo.

echo Переход в директорию проекта...
cd /d "%~dp0STUD"

echo.
echo Остановка всех процессов Python...
taskkill /f /im python.exe 2>nul
taskkill /f /im pythonw.exe 2>nul

echo.
echo Удаление базы данных...
if exist db.sqlite3 del /f /q db.sqlite3

echo.
echo Удаление всех миграций...
if exist account\migrations\*.py del /f /q account\migrations\*.py
if exist my_site\migrations\*.py del /f /q my_site\migrations\*.py

echo.
echo Создание пустых файлов миграций...
echo # Generated manually > account\migrations\__init__.py
echo # Generated manually > my_site\migrations\__init__.py

echo.
echo Создание миграций заново...
python manage.py makemigrations

echo.
echo Применение миграций...
python manage.py migrate

echo.
echo Создание суперпользователя...
python manage.py createsuperuser

echo.
echo Запуск сервера...
python manage.py runserver

