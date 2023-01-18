# Учебный проект компании Ylab university
# API для проекта Меню ресторана. Учебный проект Ylab. 


# Начало работы:
1.* Склонируйте репозиторий `ylab_project`
```bash
git@github.com:nsm23/y_lab.git
```
2.* Создайте вирутальное окружение
```bash
python -m venv venv
source venv/bin/activate
```
3.* Установите зависимости
```bash
pip install -r requirements.txt
```
4.* Перейдите в директорию menuapp/
```bash
cd app/
```
5.* В файле database.py указываем данные для подключения к базе данных по следующей схеме (для PostgreSQL):
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname",
где user, password - данные для подключения к базе данных, host:port - имя и порт сервера базы данных, dbname - название базы данных.
```
* Запустите приложение
```bash
 uvicorn main:app --reload
```
