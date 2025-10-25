@echo off
echo ========================================
echo    ПРОСТОЙ ЗАПУСК ПРОЕКТА STUD
echo ========================================
echo.

echo Переход в директорию проекта...
cd /d "%~dp0STUD"

echo.
echo Удаление старой базы данных...
if exist db.sqlite3 del db.sqlite3

echo.
echo Применение миграций...
python manage.py migrate

echo.
echo Создание суперпользователя...
python manage.py createsuperuser

echo.
echo Запуск сервера...
python manage.py runserver

