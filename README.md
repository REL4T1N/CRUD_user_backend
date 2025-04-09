# CRUD_user_backend
 special for oleg
📦 User Management API
Простой REST API на FastAPI для управления пользователями: регистрация, авторизация, обновление, удаление и получение информации. Поддерживает работу с куками и CORS для взаимодействия с фронтендом (например, на Vite).

🛠️ Используемые технологии
FastAPI

SQLAlchemy

CORS Middleware

Cookie-based аутентификация

Pydantic для валидации

SQLite (зависит от твоей настройки БД)

requirements.txt для зависимостей

🚀 Установка и запуск
📂 Клонирование репозитория
bash
Копировать
Редактировать
git clone <URL-репозитория>
cd <название-папки-проекта>
🧪 Установка зависимостей
💻 Linux / macOS:
bash
Копировать
Редактировать
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🪟 Windows (CMD):
cmd
Копировать
Редактировать
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🪟 Windows (PowerShell):
powershell
Копировать
Редактировать
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
⚙️ Запуск FastAPI сервера
Linux / macOS:
bash
uvicorn main:app --reload
Windows:
cmd
uvicorn main:app --reload
По умолчанию приложение будет доступно по адресу: http://127.0.0.1:8000

📄 Структура проекта (упрощённая)
bash
├── main.py                  # Точка входа FastAPI-приложения
├── routes/
│   └── users.py             # Все маршруты, связанные с пользователями
├── services/
│   └── users_service.py     # Логика обработки данных пользователей
├── schemas/                 # Pydantic-схемы
├── dependencies.py          # Подключение БД
├── requirements.txt         # Список зависимостей

🔗 Полезные URL
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

⚠️ Примечания
Для взаимодействия с фронтендом (например, React + Vite) необходимо запускать его на http://localhost:5173 (можно изменить в main.py, параметр allow_origins).

В коде предусмотрена возможность монтирования статических файлов (например, если фронт будет собран и размещён внутри проекта). Чтобы активировать — раскомментируй строку с app.mount(...) в main.py.
