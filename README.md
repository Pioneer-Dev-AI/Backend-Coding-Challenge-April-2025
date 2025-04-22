## Backend Role Coding Challenge April 2025

### Prerequisites
- Python 3.x
- Docker and Docker Compose
- Make

### Setting up a virtual environment
- Create a virtual environment in your project directory:
  ```bash
  python -m venv .venv
  ```

- Activate the virtual environment:
  ```bash
  # Windows
  .venv\Scripts\activate

  # MacOS/Linux
  source .venv/bin/activate
  ```

### Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### Database Setup
1. Start PostgreSQL using Docker:
   ```bash
   docker-compose up -d
   ```

2. Seed the database:
   ```bash
   make run-seed
   ```

### Running the Application
Start the FastAPI server in development mode:
```bash
make run-dev
```

### Environment Variables
Create a `.env` file in the project root with the following variables:

| Variable     | Description                  | Required | Default |
|--------------|------------------------------|----------|---------|
| DATABASE_URL | PostgreSQL connection string | Yes      | -       |