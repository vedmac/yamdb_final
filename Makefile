start:
	docker-compose up -d

collectstatic:
	docker-compose exec web python manage.py collectstatic --noinput

migration:
	docker-compose exec web python manage.py migrate --noinput

filldb:
	docker-compose exec web python manage.py loaddata fixture.json

createsuperuser:
	docker-compose run web python manage.py createsuperuser

stop:
	docker-compose down