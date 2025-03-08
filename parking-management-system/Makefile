run:
	docker-compose up --build -d

stop:
	docker-compose down

migrate:
	docker exec -it parking_backend alembic upgrade head

logs:
	docker-compose logs -f
