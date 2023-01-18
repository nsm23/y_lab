# Учебный проект компании Ylab university
API для проекта Меню ресторана. Учебный проект Ylab. 


<p>Начало работы:
<p>1. Склонируйте репозиторий "y_lab"</p>
<b>git clone git@github.com:nsm23/y_lab.git</b>
<p>------------------------------------------------------------</p>
<p>2. Создайте вирутальное окружение</p>
<b>python -m venv venv</b>
<p><b>source venv/bin/activate</b></p>
<p>------------------------------------------------------------</p>
<p>3. Установите зависимости</p>
<b>pip install -r requirements.txt</b>
<p>------------------------------------------------------------</p>
<p>4. Перейдите в директорию "menuapp/"</p>
<b>cd app/</b>
<p>------------------------------------------------------------</p>
<p>5. *В файле database.py указываем данные для подключения к базе данных по следующей схеме (для PostgreSQL):
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname",
где user, password - данные для подключения к базе данных, host:port - имя и порт сервера базы данных, dbname - название базы данных.</p>
<p>------------------------------------------------------------</p>
<p>6. *Запустите приложение</p>
<b>uvicorn main:app --reload</b>

