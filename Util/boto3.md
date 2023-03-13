- Client와 Resource의 차이

    Client는 botocore를 wrapping한 클래스이며 Resource와 비교했을 땐 보다 하위레벨의 인터페이스이다.(참고로 botocore는 aws cli를 코드로 wrapping한 인터페이스이다.)

    Resource는 Client를 wrapping한 클래스이며 이에 따라 Client보다 상위레벨의 인터페이스이다.

    기능 자체는 Client가 당연히 더 많다. 이에 따라 Resource보다 세밀한 코드 작성이 가능하다.

- boto3.session이란

    Session은 client나 resource를 생성할 수 있도록 자격 증명에 대한 ‘상태’를 저장하고 있는 객체이다.

    ```python
    import boto3
    session = boto3.Session(profile_name='brandi-ad-prd')
    s3 = session.client('s3')
    ```

    Session은 설정 상태를 저장하고 client, resource를 통해 서비스에 접근하기 위한 권한을 부여하기 위해 사용한다.

- boto3의 AWS Credentials를 확인하는 순서

    1. boto3.client, resource, session 함수에 자격증명 관련 내용을 매개변수로 코드상에서 전달
    2. 인스턴스에 선언된 환경 변수에 접근
    3. 공유 자격증명 파일(~/.aws/credentials)
    4. AWS 구성 파일(~/.aws/config)
    5. AssumeRole(임시 자격증명) 호출(~/.aws/config)
    6. boto2 구성 파일(/etc/boto.cfg 또는 ~/.boto)
    7. IAM Role이 구성된 Amazon EC2 인스턴스의 인스턴스 메타 데이터 서비스

- References:

    - https://dev-navill.tistory.com/12
    - https://velog.io/@city7310/boto3가-자격-증명-정보를-얻어내는-구조
    - https://tech.cloud.nongshim.co.kr/2021/03/12/boto3가-aws의-자격증명credentials을-확인하는-순서-from-python/