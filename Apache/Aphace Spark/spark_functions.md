* lag
> `lag(col: ColumnOrName, offset: int = 1, default = Optional[Any] = None) -> col`
> - Window function: 지정한 `col`의 `offset`만큼 전에 해당하는 row의 col을 반환한다. 만약 이전 값이 없다면 null을 반환하며, `default`를 사용하여 null을 대신하여 특정한 값을 지정할 수 있다.

* lead
> `lead(col: ColumnOrName, offset: int = 1, default: Optional[Any] = None) -> col`
- Window function: row 단위로 동작하며, 전달한 window를 기준으로 `offset`만큼 뒤에 해당하는 row의 `col` 값을 반환한다. 만약 값이 없다면 null을 반환하며, `default`를 사용하여 null을 대신해 기본값을 지정할 수 있다.

* first
> `first(col: ColumnOrName, ignorenulls: bool = False) -> col`
> - Aggregation function: group에 속한 `col`의 첫번째 값을 반환

* slice
> `slice(x: ColumnOrName, start: Union[ColumnOrName, int], length: Union[ColumnOrName, int]) -> col`
> - `x`는 배열이며, `start`를 기준 인덱스로 설정하고 `lenght`까지 `x`의 요소들을 반환한다.

* array_position
> `array_position(col: ColumnOrName, value: Any) -> col`
> - `col`은 배열이며, 배열 내의 값들 중 맨 처음 존재하는 `value`에 해당하는 index를 반환한다. 만약 배열 내에 `value`가 존재하지 않는다면 0을 반환한다.	
* exists
> `exists(col: ColumnOrName, f: Callable[[pyspark.sql.column.Column], pyspark.sql.column.Column]) -> col`
> - `col`을 기준으로 `f`에 따라 true나 false를 반환한다.