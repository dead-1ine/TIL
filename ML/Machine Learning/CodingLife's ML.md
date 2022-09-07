
### 머신러닝의 분류(가장 대표적인 것들만)
- 기계학습
	- 지도학습 supervised learning
		- 분류 classfication
		- 회귀 regression
	- 비지도학습 unsupervised learning
		- 군집화 clustering
		- 변환 transform
		- 연관 association
	- 강화학습 reinforcement learning

### 지도학습
> “정답이 있는 데이터를 활용해 학습시켜 모델을 만드는 방식”
> - 분류
>   - 전형적인 지도학습이다.
>   - 주어진 데이터를 정해진 label에 따라 분류하는 문제를 말함
>   - label == tag == target == class
> - 회귀
>   - 어떤 데이터들의 예측 변수(Predictor variable)라 불리는 특성을 기준으로, 연속된 값(그래프)을 예측하는 문제
>   - 주로 어떤 패턴이나 트렌드, 경향을 예측할 때 사용된다.

### 비지도학습
> “무언가에 대한 관찰을 통해 새로운 의미나 관계를 밝혀내는 것”
> “정답이 없는 데이터를 비슷한 특징끼리 군집화하여 새로운 데이터에 대한 결과를 예측하는 방식”
>
> - 군집화
> - 변환
> - 연관

### 강화학습 Reinforcement Learning
> “행동에 대한 보상을 받으며 학습하여 어떤 환경 안에서 선택 가능한 행동들 중 보상을 최대화하는 행동 또는 행동 순서를 선택하는 방식”
> “즉, 어떤 환경 안에서 정의된 주체(agent)가 현재의 상태(state)를 관찰하여 선택할 수 있는 행동(action)들 중에서 가장 최대의 보상(reward)을 가져다주는 행동이 무엇인지를 학습하는 것
>
> - Agent -> Action -> Environment -> State -> [Reward]



### 경사 하강법 (gradient descent)

---

- 함수 값이 낮아지는 방향으로 독립 변수 값을 변형시켜가면서 최종적으로 최소 함수 값을 갖도록 하는 독립 변수 값을 찾는 방법

$$
Xi+1 = Xi - 이동거리 * 기울기의 부호
$$

