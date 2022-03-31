# Siamese Neural Networks

> One-shat learning 분야의 논문이다.

Siamese Network는 다루어야 하는 클래스의 종류가 매우 많고 ,특정 클래스에 대한 사진을 대량으로 구할 수 없을 때 머신러닝을 활용하여 그 클래스를 구분해내기 위하여 고안된 네트워크이다.

### One-shot learning

기존 딥러닝 모델은 인간처럼 소량의 데이터만으로는 학습할 수 없다. 이와 반대로 딥러닝 모델이 소량의 데이터로 학습할 수 있게 하는 것을 **Few-shot learning**이라고 하며, **One-shot learning**은 few-shot learning의 극단적인 예시이다.

즉, 한 장의 데이터만으로 학습을 할 수 있게 만드는 것이다.



### 모델링

샴 네트워크는 두 사진을 입력으로 받아 이미지를 벡터화 시킨 후, 두 벡터간의 유사도(similarity in [0, 1])를 반환하는 네트워크이다. Network는 해당 이미지의 특징을 hard-crafted features가 아닌 data에서 직접 학습할 수있으므로 주어진 similarity를 최적화할 수 있는 양질의 feature를 추출해준다.

샴 네트워크는 하나의 이미지를 하나의 벡터로 변환할 수 있는 weight를 가지고 있다.
아래의 그림과 같이 이미지를 입력으로 받아 convolution 연산을 거쳐 하나의 벡터로 이미지를 인코딩한다.

![스크린샷 2022-03-31 오후 10.25.14](/Users/yangws/Library/Application Support/typora-user-images/스크린샷 2022-03-31 오후 10.25.14.png)