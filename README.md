# TODOAPP

* Note: This app is tested on python 3.5.2, hence docs are as per same version

## Installation

Requires PostGreSQL & Python

```sh
git clone https://github.com/bhaveshAn/todo-task.git

cd todo-task

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt
```

## Running the Application

1. Create `stayabode` database in PostGreSQL

```sh
sudo -u postgres psql
```

```sql
CREATE USER john WITH PASSWORD 'start';
CREATE DATABASE stayabode WITH OWNER john;
```

2. Run the DataBase Server

```sh
sudo service postgresql start
```

3. Migrate Database

```sh
python manage.py migrate
```

4. Create Super User

```sh
python manage.py createsuperuser
```

5. Run the application server

```sh
python manage.py runserver
```
