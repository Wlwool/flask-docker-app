# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY flask_app/ /app/

# Указываем порт, который будет открыт
EXPOSE 5000

# Указываем команду для запуска приложения
CMD ["python", "app.py"]
