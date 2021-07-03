FROM python:3

WORKDIR /app

# Setup Env
ADD    ./prod.env       /app/prod.env
ADD    ./prod.env       /app/.env

# Install Package
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

# Install Project
ADD    ./gunicorn       /app/gunicorn/

CMD ["gunicorn", "main:app", "-c", "gunicorn/prod.py"]
