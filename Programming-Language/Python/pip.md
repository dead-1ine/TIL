# PIP(Python Installs Packages)

- Python 패키지를 설치하고 관리하는 패키지 매니저

    

### PIP 사용법

------

requirements.txt로 패키지 관리하기

- 설치된 모든 패키지 보기

    ```
    $ pip list
    
    Package                       Version
    ----------------------------- -----------
    alabaster                     0.7.12
    alembic                       1.0.11
    appnope                       0.1.0
    ```

- 현재 설치된 패키지가 명시된 requirements.txt 파일 생성

    ```
    $ pip freeze > requirements.txt
    ```

- 명시된 package를 설치

    ```
    pip install -r requirements.txt 
    ```

- requirements 문법

    - `==`: 정확한 버전으로 설치
    - `>=`: 해당 버전 이상으로 설치
    - `>=3.*`: 3 이상의 아무 버전 설치
    - `#`: 주석