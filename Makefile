.PHONY: build run stop clean test lint seed

# Docker compose commands
build:
	docker-compose build

run:
	docker-compose up

stop:
	docker-compose down

# Clean up Docker resources
clean:
	docker-compose down -v
	docker system prune -f

# Development commands
install:
	pip install -r requirements.txt

lint:
	pip install flake8
	flake8 app/

run-server:
	uvicorn app.main:app

# Database commands
seed:
	docker-compose exec web python -m app.seed

run-seed:
	python -m app.seed

# Help command
help:
	@echo "Available commands:"
	@echo "  make build      - Build Docker containers"
	@echo "  make run        - Run the application with Docker Compose"
	@echo "  make stop       - Stop running containers"
	@echo "  make clean      - Remove containers, volumes, and prune system"
	@echo "  make install    - Install Python dependencies locally"
	@echo "  make lint       - Run code linting"
	@echo "  make seed       - Seed the database (Docker)"
	@echo "  make run-seed   - Seed the database (Local)" 