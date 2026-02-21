# Flask Docker App - Генератор паролей

https://flask-docker-app-nhwy.onrender.com/

Простое и легковесное веб-приложение на Python с использованием Flask, упакованное в Docker-контейнер. Для изучения Docker и создания переносимых приложений.

---

## Возможности
- **Минималистичное приложение Flask**
- **Docker-окружение**: Гарантирует стабильную работу на любой платформе.
- **Кроссплатформенность**: Легко переносится между Linux и Windows

---

## Требования 🛠
- **Linux/Ubuntu** или **Windows**
- **Docker** 
- **Git**

---

## Установка и запуск ⚙️

### 1. Клонирование репозитория
Клонирование с GitHub:

```bash
git clone https://github.com/Wlwool/flask-docker-app.git
cd flask-docker-app
```

## Создание виртуального окружения
```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux
venv\Scripts\activate     # Для Windows
```

Зависимости
```commandline
pip install -r requirements.txt
```

### 2.Сборка Docker образа для приложения Flask:

```bash
docker build -t flask-app .
```

### 3. Запуск контейнера
Запуск Flask-приложения в контейнере:

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

### 4. Доступ к приложению
Перейдите по адресу:
http://localhost:5000

---

## Запуск на Windows 🖥️
### Шаг 1: Установка Docker Desktop
Скачайте и установите Docker Desktop с официального сайта Docker.

### Шаг 2: Клонирование и сборка
После установки Docker Desktop:

```bash
Копировать код
git clone https://github.com/Welzewool/flask-docker-app.git
cd flask-docker-app
docker build -t flask-app .
```

### Шаг 3: Запуск и доступ
Запустите контейнер:

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

Перейдите в браузере по адресу http://localhost:5000.

## Обновление проекта 🔄
Чтобы обновить проект, выполнить:

```bash
git add .
git commit -m "Описание изменений"
git push origin main
```

Для Windows:

```bash
git pull origin main
docker build -t flask-app .
docker run -d -p 5000:5000 --name flask-container flask-app
```

---

## Запуск с docker-compose
Запуск приложения одной командой:

```bash
docker-compose up --build
```

Приложение станет доступно по адресу:
http://localhost:5000

### Остановка приложения
Чтобы остановить приложение:
```bash
docker-compose down
```

```commandline
http://localhost:5000
```


---

# Планы
- Добавить дополнительные маршруты и логику в файл app.py.
- Для улучшения безопасности использовать SSL/TLS при развертывании приложения

# Лицензия

- Проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.
