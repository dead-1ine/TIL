# Collaborative Filtering

다른 유저의 추천 데이터들을 바탕으로 시스템을 구현한다. 사용자들의 데이터를 바탕으로 추천을 구축하는데, 하위 항목으로 아이템 기반 필터링과 유저 기반 필터링으로 구분된다.

- **유저 기반 필터링의 경우**, 추천을 받을 사용자(A)와 유사한 타 사용자(B)를 추천 리스트를 통해 찾아내고 B가 좋아하는 목록 중 아직 A가 경험한 적 없는 아이템을 추천해준다.
- **아이템 기반 필터링의 경우**, 아이템들에 대해 사용자들의 선호도를 기반으로 유사한 아이템을 찾아 추천하는 기법이다. User A/C/D를 통해 유사한 Item 두 가지가 검증되어 해당 아이템을 추천하는 기법이다.

하지만, CF는 **콜드 스타트**라는 문제점을 갖고 있다. 기본적으로 타 사용자들의 데이터를 기반으로 추천하기 때문에 신상품과 같은 아무도 추천 데이터를 쌓지 않는 아이템은 추천받을 수 없다. 데이터가 생길때까지 기다리는 수 밖에 없고 그동안은 추천 리스트에 오르지 못한다는 것이다.