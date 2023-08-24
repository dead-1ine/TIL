- 알아봐야 함
    - [ ] `pip install scan` → `ERROR: Could not find a version that satisfies the requirement scann`
- History
    - 23.08.24:
        1. ScaNN Script를 Faiss로 변경
        2. ECR 사용법 적용 서두르기

## 상황

------

### 1. SageMaker Notebook Instance 생성 시 기존에 사용하던 Kernel을 찾을 수 없다는 에러 발견

- 기존에 사용하던 Platform Identifier인 `notebook-al2-v1` 에 포함된 kernel 중 `conda_amazonei_tensorflow2_p36` 이 없어짐

### 2. `pip install scann` 시 에러 발생

```bash
(python3) sh-4.2$ conda activate test-scann-py310

(test-scann-py310) sh-4.2$ python --version
Python 3.10.12

(test-scann-py310) sh-4.2$ pip install scann
ERROR: Could not find a version that satisfies the requirement scann (from versions: none)
ERROR: No matching distribution found for scann
```

### References

------

- SageMaker Platform Identifier 별 Kernel 정보

    [Amazon Linux 2 vs Amazon Linux notebook instances - Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-al2.html)

- Github - google-research/scann

    

- PyPI

    [scann](https://pypi.org/project/scann/)

    [tensorflow](https://pypi.org/project/tensorflow/)

- ScaNN Source Build Directly

    [How to Install Google Scalable Nearest Neighbors (ScaNN) on Mac](https://eugeneyan.com/writing/how-to-install-scann-on-mac/)

    [Bazel](https://bazel.build/)