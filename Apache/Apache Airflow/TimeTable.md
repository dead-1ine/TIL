# TimeTable

현재의 `schedule_interval`은 Cron Expression과 `timedelta`로만 표현할 수 있기 때문에 **공휴일을 제외한 영업일에만 작업**과 같이 스케줄 중간중간에 구멍이 뚫려 있는 복잡한 형태의 스케줄을 정의할 수 없다.

AIP-39에서 이러한 문제를 해결하기 위해 복잡한 시간을 표현할 수 있는 `TimeTable`이라는 새로운 클래스가 도입되었다. 

참고로, Cron Expression은 여전히 널리 쓰이기에 사라지지 않고 계속 유지될 예정이다. 사용자들은 상황에 맞게 `schedule_interval`에 Cron Expression 혹은 `TimeTable`객체를 사용하면 된다.

---

- Class Timetable

```python
class Timetable(Protocol):
    def next_dagrun_info(
        self,
        *,
        last_automated_data_interval: Optional[DataInterval],
        restriction: TimRestriction,
    ) -> Optional[DagRunInfo]:
        """
        스케줄러가 이 함수를 호출해 가장 마지막에 처리된 `data_interval`을 확인하고,
        이에 따라 Dag가 실행되어야 하는 다음 스케줄(`DagRun`)을 반환한다.
        
        :param last_automated_data_interval: 
        	이미 실행된 스케줄 중 가장 마지막에 실행된 스케줄에서 처리된 `data_interval`(manual run 제외)
        
        :param restriction: 
        	DAG 스케줄을 결정할 때 고려해야 할 제약사항을 담고 있다.
        	DAG를 정의할 때 설정하는 `start_date`, `end_date`, `catchup` 등의 정보가 담겨 있다.
        """
```

스케줄러는 일정한 간격으로 `Timetable`의 `next_dagrun_info`를 poke하여 DAG의 다음 스케줄이 필요한지 확인한다. 이 함수에서 마지막으로 실행된 DAG 스케줄에서 처리된 데이터의 범위(`data_interval`)을 보고, 바로 다음에 실행되어야 할 DAG 스케줄을 반환하면 스케줄러가 그 시간에 DAG를 실행하게 된다.

기존과는 달리 DAG의 마지막 실행날짜가 아닌 DAG에서 처리한 데이터의 범위(`date_interval`)를 기반으로 다음 DAG가 실행될 스케줄을 결정하게 되고, 스케줄 시점을 파이썬 코드로 작성할 수 있기 때문에 DAG의 스케줄 시점을 자유롭게 설정할 수 있다.

---

- Class DagRunInfo

```python
class DagRunInfo(NamedTuple):
    run_date: DateTime
    """
    DAG가 실행되어야 하는 스케줄 중 가장 빠른 시점을 나타낸다.
    만약 None이라면 DAG의 실행 스케줄이 아직 결정되지 않았다는 뜻이다.
    """
    data_interval: DataInterval
    """
    DAG가 실행될 때 처리해야 하는 데이터의 기간을 표현한다. (start, end)
    """
```

DAG의 스케줄 정보를 나타내는 `DagRunInfo` 클래스이다. 스케줄러가 `TimeTable`에 다음 스케줄을 물어보면 이 클래스가 반환된다. `run_date`는 DAG가 실행되어야 할 다음 스케줄을 알려주고, `data_interval`은 해당 스케줄에서 처리해야 할 데이터 기간의 범위를 표현한다.

DAG가 실행되어야 하는 시점(`run_date`)과 처리해야 하는 데이터의 범위(`date_interval`)가 명확하게 분리되어 있는 것을 확인할 수 있다.

---

## 새로운 인터페이스가 좋은 것은 알겠는데, 기존과 차별화된 점은 무엇일까?

### 1. 정해진 시점의 데이터를 기록하는 스냅샷을 찍고 싶다.

스냅샷을 생성할 때는 특정 시점의 데이터를 기록하는 것이기 때문에 `data_interval`의 개념이 필요 없다. 이 경우 `data_interval_start`, `data_interval_end` 그리고 `run_date` 모두 같은 날짜가 된다.

### 2. 스케줄 간격과 처리해야 하는 데이터의 기간이 다르다.

