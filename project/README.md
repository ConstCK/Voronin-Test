BackEnd:

Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/Voronin-Test.git
Создайте виртуальное окружение (python -m venv venv) и активируйте его (venv\scripts\activate)
Установите все зависимости при помощи pip install -r requirements.txt в терминале
Создайте файл .env в каталоге проекта и пропишите в нем SECRET_KEY = Сгенерированный ключ
и другие Ваши переменные по шаблону из файла .env.example
Ключ для Django можно сгенерировать по пути https://djecrety.ir/
Запустите сервер из каталога проекта (python manage.py runserver)

EndPoints:
http://127.0.0.1:8000/api/books - Список всех книг при GET запросе
http://127.0.0.1:8000/api/books - Создание новой книги при POST запросе
http://127.0.0.1:8000/api/books/<:id> - Получение, Изменение, Удаление книги при GET, PATCH/PUT, DELETE запросе.
