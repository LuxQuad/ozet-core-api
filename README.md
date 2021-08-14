<div id="header" align="center">
  <h1>Esume Core API</h1>
  <div id="ci-cd">
      <a href="https://circleci.com/gh/LuxQuad/ozet-core-api/tree/develop">
        <img src="https://circleci.com/gh/LuxQuad/ozet-core-api/tree/develop.svg?style=shield&circle-token=36c9a40ddbf32c1d59030908ef15af6f6c1a05d5" alt="circleci"/>
      </a>
      <a href="https://codecov.io/gh/LuxQuad/ozet-core-api">
        <img src="https://codecov.io/gh/LuxQuad/ozet-core-api/branch/develop/graph/badge.svg?token=XNFZWYXC91" alt="codecov" />
      </a>
      <a href="#" target="_blank"><img src="https://img.shields.io/github/issues-pr-closed/LuxQuad/ozet-core-api" alt="GitHub closed pull requests" /></a>
  </div>
  <div id="project-logo">
    <a href="https://github.com/BartKim-J/pretty-readme" >
      <img src="https://user-images.githubusercontent.com/36470472/128664018-103bff8e-6be3-4996-9bbd-41d82a7d48d8.png" width="200px" height="200px" alt="project-logo"/>
    </a>
  </div>
  <div id="main">
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/Python%203.7%20|%203.8%20-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="python" /></a>
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white" alt="docker" /></a>
  </div>
  <div id="sub">
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/Fast%20API-009688?style=flat&logo=FastAPI&logoColor=white" alt="django" /></a>
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/PostgresQL-4479A1?style=flat&logo=PostgresQL&logoColor=white" alt="mysql" /></a>
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=Redis&logoColor=white" alt="redis" /></a>
  </div>
</div>

> :warning: esume logo 나오면 이미지 교체 예정

## Getting Started

아래는 `Esume Core API` 를 실행하기 위한 가이드 입니다.

### Prerequisites

---
아래 사항들이 설치 및 선행 되어 있어야 합니다.
* #### [Docker Desktop](https://www.docker.com/products/docker-desktop) (example)
    * Mac 설치
        ```
        $ (설치 명령어)
        ```
### Installing

---
아래는 프로젝트를 설치하는 방법입니다.
1. #### 레포지토리 설치 (example)
    ```
    $ git clone https://github.com/LuxQuad/esume-core-api.git 
    $ cd esume-core-api
    ```
2. #### 환경 설치
    ```
    $ pip install -r -requirements.txt
    ```

## Testing
하단의 스크립트를 실행하면 테스트 코드가 작동합니다.
```
$ pytest
```
아래와 같이 테스트가 진행됩니다.
```
(테스트 중)
```
```
(테스트 결과)
```

## Running
아래는 프로젝트를 실질적으로 실행하는 방법에 대해 설명합니다.

> Running Admin URL(http://127.0.0.1:8000) 
> 
> 

* ### [Django](https://docs.djangoproject.com/ko/2.1/intro/tutorial01/#the-development-server) (example)
    ```
    $ python manage.py runserver
    ```
    ```
    (실행 결과)
    ```

* ### [Gunicorn](https://docs.gunicorn.org/en/stable/) (example)
    ```
    $ gunicorn service.main:app
    ```
    ```
    ...
    (실행 결과)
    ```

## Workflow
현재 Workflow 는 기본적으로 [Git Flow](https://techblog.woowahan.com/2553/) 를 사용하고 있습니다.
> * `master` : 제품으로 출시될 수 있는 브랜치
> * `develop` : 다음 출시 버전을 개발하는 브랜치
> * `feature` : 기능을 개발하는 브랜치
> * `release` : 이번 출시 버전을 준비하는 브랜치
> * `hotfix` : 출시 버전에서 발생한 버그를 수정 하는 브랜치
> * `fix` : 기존에 발생한 버그를 수정하는 브랜치
>
>
> <div align="center"> <img src="https://user-images.githubusercontent.com/36470472/128487175-e5d28ce3-b5b7-48f2-914d-4b9383277986.png" width="600" alt="git-flow" /></div>

## Directory Structure(example)
```
.
├── app
│        ├── crud
│        ├── database
│        ├── grpc
│        │       ├── protos
│        │       └── protos_python
│        ├── middleware
│        ├── models
│        ├── routers
│        │       ├── health
│        │       ├── items
│        │       ├── sentry
│        │       └── users
│        ├── schemas
│        └── test
│            └── api
├── docker
│        ├── postgresql
│        └── redis
├── nginx
└── script
         └── grpc


```
