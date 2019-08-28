migrations: 
	docker-compose run app python3 manage.py makemigrations
migrate: 
	docker-compose run app python3 manage.py migrate
flake8:
	docker-compose run --rm app flake8 .

# swagger-docs:
# 	docker-compose run --service-ports docs
