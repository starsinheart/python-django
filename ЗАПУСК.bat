@echo off
chcp 65001 >nul
echo ========================================
echo    ЗАПУСК ПРОЕКТА STUD
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
echo Удаление старой базы данных (если есть)...
if exist db.sqlite3 del /f /q db.sqlite3

echo.
echo Применение миграций...
python manage.py migrate

if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось применить миграции!
    echo Попробуйте запустить команды вручную:
    echo cd STUD
    echo python manage.py migrate
    pause
    exit /b 1
)

echo.
echo Миграции применены успешно!
echo.

echo Создание суперпользователя...
echo ВНИМАНИЕ: Введите данные для администратора системы
echo.
python manage.py createsuperuser

if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось создать суперпользователя!
    echo Попробуйте создать суперпользователя вручную:
    echo python manage.py createsuperuser
    pause
    exit /b 1
)

echo.
echo ========================================
echo    ПРОЕКТ ГОТОВ К РАБОТЕ!
echo ========================================
echo.
echo Откройте браузер и перейдите по адресу:
echo http://127.0.0.1:8000/
echo.
echo Админ-панель: http://127.0.0.1:8000/admin/
echo.
echo Для остановки сервера нажмите Ctrl+C
echo.
pause

echo Запуск сервера разработки...
python manage.py runserver
