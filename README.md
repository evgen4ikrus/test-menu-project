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
Загрузите тестовые данные в БД:
```commandline
python3 manage.py loaddata test_db_data.json
```
Запустите веб-приложение:
```commandline
python3 manage.py runserver
```
Проверьте работу веб-приложения перейдя по [ссылке](http://127.0.0.1:8000/admin/) в панель администратора.
