# AWS SecretsManager

Secrets Manager는 코드의 암호를 포함해 하드 코딩된 자격 증명을 Secrets Manager에서 프로그래밍 방식으로 보안 암호를 검색하도록 하는 API 호출로 바꿀 수 있다.

이렇게 하면 보안 암호가 코드에 더 이상 존재하지 않기 때문에 코드를 검사하는 누군가에 의해 보안 암호가 손상되지 않도록 방지할 수 있다.

또한, 사용자가 지정한 일정에 따라 Secrets Manager가 자동으로 보안 암호를 교체하도록 구성할 수 있다.

따라서 단기 보안 암호로 장기 보안 암호를 교체할 수 있어 손상 위험이 크게 줄어든다.





# 기본적인 AWS Secrets Manager 시나리오

1. 데이터베이스 관리자가 MyCustomApp이라는 애플리케이션에서 사용할 수 있도록 인력 데이터베이스에 대한 자격 증명 세트를 생성한다. 또한 관리자는 이 애플리케이션에서 인력 데이터베이스에 엑세스하는 데 필요한 권한을 사용하여 이러한 자격 증명을 구성한다.
2. 데이터베이스 관리자가 Secrets Manager에서 자격 증명을 MyCustomAppCreds라는 보안 암호로 저장한다. 그런 다음 Secrets Manager는 자격 증명을 암호화하여 보안 암호 내에 보호되는 보안 암호 텍스트로 저장한다.
3. MyCustomApp에서 데이터베이스에 엑세스하는 경우 이 애플리케이션은 Secrets Manager에 MyCustomAppCreds라는 보안 암호를 쿼리한다.
4. Secrets Manager는 이 보안 암호를 검색하고 보호되는 보안 암호 텍스트의 암호를 해독해 보안(TLS를 통한 HTTPS) 채널을 통해 클라이언트 앱에 보안 암호를 반환한다.
5. 이 클라이언트 애플리케이션은 응답에서 자격 증명, 연결 문자열 및 기타 필요한 정보를 구문 분석한 다음 이러한 정보를 사용해 데이터베이스 서버에 엑세스한다.



# 사용법

1. 키 등록(Key, Value Format)
2. Python 환경에서는 boto3 Library를 활용하여 Secrets Manager API를 사용

```python
# AWS Secrets Manager에 접근하여 API를 호출하는 최소한의 로직
import json
import boto3

def get_secret(secret_name: str):
    region_name = "ap-northeast-2"
    profile_name = "aws_default_profile"
    # Create a Secrets Manager Client
    session = boto3.session(region_name=region_name, profile_name=profile_name)
    sm = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = sm.get_secret_value(
    	SecretId=secret_name
    )
    secret = get_secret_value_response['SecretString']
    return json.loads(sercret)

get_secret("secret_name_on_your_service") # Return Type is dict
```

3. boto3를 통해 전달받은 response를 활용하여 암호값을 사용



### TODO

---

1. Glue에서의 사용법(Connector 생성 시 SecretsManager 설정법)