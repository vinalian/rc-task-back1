@echo off
setlocal

rem Путь к виртуальной среде (venv)
set venv_path=venv

rem Проверяем, существует ли виртуальная среда
if not exist %venv_path% (
    echo Создание новой виртуальной среды...
    python -m venv %venv_path%
)

rem Активируем виртуальную среду
call %venv_path%\Scripts\activate

rem Устанавливаем зависимости из req.txt
pip install -r req.txt

rem Запускаем python скрипт
python run.py

rem Деактивируем виртуальную среду
deactivate
