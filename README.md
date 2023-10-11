# test-menu-project

### Установка и запуск:
Клонируйте репозиторий:
```commandline
git clone https://github.com/evgen4ikrus/test-menu-project.git
```
Перейдите в директорию проекта:
```commandline
cd test-menu-project/
```
Создайте и активируйте виртуальное окружение:
```commandline
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости:
```commandline
pip install -r requirements.txt
```
Примените миграции БД:
```commandline
python3 manage.py migrate
```
Запустите веб-приложение:
```commandline
python3 manage.py runserver
```
Проверьте работу веб-приложения перейдя по [ссылке](http://127.0.0.1:8000/admin/) в панель администратора.

### Тестовые данные
Для тестирования работы веб-приложения, наполните базу данных тестовыми данными:
```commandline
python3 manage.py loaddata db_test_data.json
```