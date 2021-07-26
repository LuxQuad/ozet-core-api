FROM python:3.7

WORKDIR /service

# Setup Env
ADD    ./prod.env       /service/prod.env
ADD    ./prod.env       /service/.env

# Install Package
ADD    ./requirements.txt   /service/
RUN    pip install -r requirements.txt

# Install Project
ADD    ./app            /service/app

EXPOSE 8000

CMD ["uvicorn", "app.main:service", "--host", "0.0.0.0", "--port", "8000", "--env-file", "prod.env"]