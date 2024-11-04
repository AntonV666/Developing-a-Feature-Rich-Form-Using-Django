Документация по установке и запуску приложения

Установка

1. Клонируйте репозиторий
   
   git clone <url-репозитория>
   cd <имя_папки_репозитория>
   

2. Создайте виртуальное окружение
   
   python -m venv .venv
   

3. Активируйте виртуальное окружение
   - На Windows:
     
     .venv\Scripts\activate
     
   - На macOS/Linux:
     
     source .venv/bin/activate
     

4. Установите зависимости
   
   pip install django
   

5. Создайте базу данных
   
   python manage.py makemigrations
   python manage.py migrate
   

6. Создайте суперпользователя (для администрирования)
   
   python manage.py createsuperuser
   

7. Запустите сервер разработки
   
   python manage.py runserver
   

8. Откройте приложение в браузере
   Перейдите по адресу http://127.0.0.1:8000/.
