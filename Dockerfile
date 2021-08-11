FROM python:3.7

WORKDIR /service

# Install Project
ADD    ./app              /service/app
ADD    ./docker           /service/docker
ADD    ./nginx            /service/nginx
ADD    ./tests            /service/tests
ADD    ./.github          /service/.github
ADD    ./.misc            /service/.misc
ADD    ./pytest.ini       /service/pytest.ini

# Install Package
RUN    pip install -r .misc/requirements/prod.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:service", "--host", "0.0.0.0", "--port", "8000", "--env-file", ".misc/env/prod.env"]