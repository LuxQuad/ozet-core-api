FROM python:3.7

WORKDIR /service

# Install Package
ADD    ./requirements.txt   /service/
RUN    pip install -r requirements.txt

# Install Project
ADD    ./app              /service/app
ADD    ./tests            /service/tests
ADD    ./.misc            /service/.misc
ADD    ./pytest.ini       /service/pytest.ini

EXPOSE 8000

CMD ["uvicorn", "app.main:service", "--host", "0.0.0.0", "--port", "8000", "--env-file", ".misc/env/prod.env"]