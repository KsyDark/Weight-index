::Убиваем процесс программы
taskkill /f /im "Индекс веса.exe"
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --noconsole --icon=ves.ico "Индекс веса.py"
:: Запускаем программу после компиляции
cd dist
start "Расчёт" "Индекс веса.exe"
