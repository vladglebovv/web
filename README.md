# bd_spbu
## Первый запуск<br/>
### Команды для первого запуска приложения:<br/>
docker-compose build<br/>
docker-compose up -d<br/>
docker-compose exec web python myshop3/manage.py makemigrations<br/>
docker-compose exec web python myshop3/manage.py migrate<br/>
docker-compose exec web python myshop3/manage.py createsuperuser<br/>


Адрес главной страницы http://0.0.0.0:8000<br/>
Панель администратора http://0.0.0.0:8000/admin<br/>


Для завершения работы <br/>
docker-compose down<br/>


### Дальнейшие запуски<br/>
Запустить<br/>
docker-compose up -d<br/>


Завершить<br/>
docker-compose down<br/>

