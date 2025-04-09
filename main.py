from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routes.users import user_router

app = FastAPI()

# Настройка CORS для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Порт Vite по умолчанию
    allow_credentials=True,  # Разрешаем куки
    allow_methods=["*"],  # Разрешаем все HTTP-методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Подключение маршрутов пользователей
app.include_router(user_router)

# Монтирование статических файлов
# app.mount("/", StaticFiles(directory="./backend/static", html=True), name="static")