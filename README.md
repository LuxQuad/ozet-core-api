# **Esume Core API** - [![CircleCI](https://circleci.com/gh/LuxQuad/esume-api/tree/master.svg?style=svg&circle-token=e8cf4faab2b5a1b40b12f998fa72789c566eb35e)](https://circleci.com/gh/LuxQuad/esume-api/tree/master) [![Python](https://img.shields.io/badge/python-3.7.4-brightgreen.svg)]() [![FastAPI](https://img.shields.io/badge/FastAPI-0.1.4-brightgreen.svg)]() [![Docker](https://img.shields.io/badge/docker_engine-20.1.2-brightgreen.svg)]() 

# **Convention** 
---
## **Version(Tag) Convention**
* Version 관리는 `<major>.<minor>.<number>.<datetime>` 형태로 관리된다.
    * `<major>` 는 상호 API 및 전체적인 부분에 대한 호환성을 의미하며 이 version이 다를 경우 호환성을 보장 받을 수 없다.
    * `<minor>` 는 API 버전을 뜻하며 이는 상호 호환성을 보장 받거나 상호 송수신자간에 동의가 이루어진 변경사항에 대한 version 표기다.
    * `<number>` 는 admin 및 back-office, worker, task등의 전반적인 변경사항에 대한 version 표기이며 back-end 내에서의 version을 의미한다.
    * `<datetime>` 은 tag가 생성된 즉, 배포된 날짜를 표기한다.


## **Git Convention**
* ### Common
    * **master는 local로 pull 하지 않는다.**
        * **또한 local에서 바로 push 될 수 없다.**
            * **따라서 작업자는 dev를 기본 branch로 작업한다.**
            * 수정사항에 대한 반영은 dev를 master에 Pull Request 하는 것을 기본으로 한다.
                * master에 반영된 사항에 대한 deploy 작업은 관리자에 의해 처리된다.
    * **remote 에 push 된 사항에 대해 reset을 시도하지 않는다.**
        * 이미 반영된 사항에 대해 수정 및 롤백이 필요한 경우에는 `rebase`를 사용하여 *history* 가 기록되게 한다.

* ### Merge
    * 기본적으로 Merge 를 할때에는 `non-forward` 를 원칙으로 한다.
        * 기타 편의에 따라 무시될 수 있다.
    
* ### Branch
    * branch를 생성할때 "<`type`>/<`object`>/<`sub-object`>/<...>" 형태로 작성한다.
        * `type` - `feat`, `fix`, `bug`, `iss`, `instant` 등등..
        * 기타 편의에 따라 무시될 수 있다. 
    * `dev` branch 에서의 직접 작업은 지양한다.
        * 기타 편의에 따라 무시될 수 있다. 
    * 각 branch는 **한가지의 목적성**을 가지고 작업이 수행 되어야 한다.

* ### Commit
    * 기본적으로 commit은 **한글 작성**을 원칙으로 한다.
    
* ### Pull Request
    * **master에 요청된 Pull Request에 대해 관리자의 동의 없이 작업자는 Approve 및 Merge 할 수 없다.**
    * dev 까지는 자유롭게 Merge 및 Pull Request 를 해도 상관없으며 여부에 따라 Pull Request 을 통해 1-2차로 코드 리뷰를 진행할 수 있다.

## **Code Convention**
* ### Common
    * `snake_case` 를 기반으로 하며, `class` 와 같은 경우에는 `CamelCase` 를 기본으로 적용한다.
    * 기본적으로 `PEP8` 을 준수한다.
        * 기타 편의에 따라 무시될 수 있다.
