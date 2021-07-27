> “데이터 군을 저장하는 클래스들을 표준화한 설계”

- 인터페이스의 종류
	- List
		- 순서가 있는 데이터의 집합
		- 데이터의 중복을 허용한다
		- (ArrayList, LinkedList, Stack, Vector 등)
	- Set
		- 순서를 유지하지 않는 데이터의 집합
		- 데이터의 중복을 허용하지 않는다.
		- (HashSet, TreeSet 등)
	- Map
		- 키와 값의 쌍으로 이루어진 데이터의 집합
		- 순서는 유지되지 않음
		- 키는 중복을 허용하지 않고, 값은 중복을 허용한다.
		- (HashMap, TreeMap, Hashtable, Properties 등)

- Collection 인터페이스
> - 메서드 정리
- `boolean add(Object o), addAll(Collection c)
	`- 지정된 객체(o) 또는 Collection의 객체들을 Collection에 추가한다.
- `void clear() 
	`- Collection의 모든 객체를 삭제한다.
- `boolean contains(Object o), containsAll(Collection c) 
	`- 지정된 객체(o) 또는 Collection의 객체들이 Collection에 포함되어 있는지 확인한다.
- `boolean equals(Object o)
	`- 동일한 Collection인지 비교한다.
- `int hashCode()
	`- Colletion의 hash code를 반환한다.
- `boolean isEmpty() 
	`- Collection이 비어있는지 확인한다.
- `Iterator iterator()
	`- Collection의 Iterator를 얻어서 반환한다.
- `boolean remove(Object o)
	`- 지정된 객체를 삭제한다.
- `boolean removeAll(Collection c)`
	- 지정된 Collection에 포함된 객체들을 삭제한다.
- `boolean retainAll(Colletion c)`
	- retain : 유지하다.
	- 지정된 Collection에 포함된 객체만을 남기고 다른 객체들은 Collection에서 삭제한다.
	- 이 작업으로 인해 Collection에 변화가 있다면 true, 아니면 false를 반환
- `int size()
	`- Collection에 저장된 객체의 개수를 반환한다.
- `Object[] toArray()`
	- Collection에 저장된 객체를 객체배열로 반환한다.
- `Object[] toArray(Object a)`
	- 지정된 배열에 Collection의 객체를 저장해서 반환한다.