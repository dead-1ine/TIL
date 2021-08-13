
## JVM (Java Virtual Machine)
> 어떠한 OS 환경이라도 JVM이 설치되어 있다면 자바 파일을 실행할 수 있다.
> 
> - 역할
> 
>   - Java Application을 클래스 로더를 통해 읽어 들여 자바 API와 함께 실행하는 것이다.
>   - JVM은 자바와 OS 사이에서 중개자 역할을 수행하며, OS에 독립적인 플랫폼을 갖게 한다.
>   - 즉, OS의 메모리 영역에 직접 접근하지 않고 JVM이라는 가상 머신을 이용해 간접적으로 접근한다.
>   - 자바에서는 JVM의 Garbage Collector가 메모리를 자동으로 관리해준다.
> 
> - 자바 프로그램의 실행 과정
> 
>   1. 프로그램이 실행되면 JVM은 OS로부터 해당 프로그램이 필요로 하는 메모리를할당 받는다.(JVM은 이 메모리를 용도에 맞게 여러 영역으로 나누어 관리한다.)
>   2. javac가 .java를 읽어들여 .class로 변환시킨다.
>   3. 클래스 로더를 통해 .class 파일들을 JVM으로 로딩한다.
>   4. 로딩된 .class 파일들은 Execution engine을 통해 해석된다.
>   5. 해석된 .class는 RuntimeDataArea에 배치되고 수행이 이루어지게 된다.
> 
>   ![jvm][image-1]
> 
> ### 자바 실행과정 프로그램
> 
>   - Java Complier : 자바 소스코드를 Byte Code(.class)로 변환하는 역할을 한다.
>   - Class Loader : 자바 Byte Code를 읽어 JVM의 Execution Engine이 사용할 수 있도록 RuntimeDataArea에 적재한다.
>   - Execution Engine : 클래스를 실행하는 역할을 한다. Execution Engine은 메모리에 적재된 ByteCode를 실제로 JVM 내부에서 기계가 실행할 수 있는 형태로 변경한다. 이 때 두 가지 방식을 사용한다.
> 	1. Interpreter : 명령어를 그때그때 실행한다.
> 	2. JIT (Just In Time) : Interpreter의 단점을 보완하기 위해 도입된 컴파일러이다. Interpreter 방식으로 실행하다가 적절한 시점에서 바이트코드 전체를 컴파일하여 NativeCode로 변경하고, 이후 더 이상 Interpreting 하지 않고 NativeCode로 직접 실행하는 방식이다. NativeCode는 Cache에 보관하기 때문에 한 번 컴파일된 코드를 빠르게 실행한다.
>   - RuntimeDataArea : 프로그램을 수행하기 위해 OS에서 할당받는 메모리 영역이다. RuntimeDataArea는 5개의 영역으로 나눌 수 있다. 이 중 PC Register, JVM Stack, Native Method Stack은 스레드마다 하나씩 생성되며 Heap, Method Area는 모든 스레드가 고용해서 사용한다.
> 
>   ![runtimearea][image-2]
> 
>   - PC Register : 스레드가 시작될 때 생성된다. PC Register는 스레드가 어떤 명령어로 실행되어야 할 지에 대한 기록을 하는 부분으로, 현재 수행중인 JVM 명령의 주소를 갖는다.
>   - Stack Area : 프로그램 실행과정에서 임시로 할당되었다가 메소드를 빠져나가면 바로 소멸되는 특성의 데이터를 저장하기 위한 영역이다. 지역변수, 매개변수, 메소드 정보, 연산 중 발생하는 
> 
> 	  





## Garbage Collector

> 동적으로 할당한 메모리 영역 중 사용하지 않는 영역을 탐지하여 해제하는 기능
> 
> ##### "Heap영역에서 참조되고 있는 Object를 마킹하고, 참조가 없어 마킹되지 않는 Object를 제거하는 역할"

> - GarbageCollector 과정(Mark & Sweep)
>   - GC가 Stack의 모든 변수를 스캔하면서 각각 어떤 객체를 참조하고 있는지 찾아 마킹한다.
>   - Reachable Object가 참조하고 있는 객체도 찾아 마킹한다.
>   - 마킹되지 않은 객체를 Heap에서 제거한다.
> - 언제 발생할까 ?
> 	  

### Java의 특징

> - 객체지향 언어
> - 자동 메모리 관리 (GC)
> - 멀티 쓰레드 지원
> - 풍부한 라이브러리 
> - 운영체제에 독립적 (JVM)

[image-1]:	https://hanul-dev.netlify.app/static/58da7d76d6a2d6b85b78337a837a6c07/fcda8/jvm.png
[image-2]:	https://hanul-dev.netlify.app/static/b894198e3c298b9515496a43c1abf1f5/fc778/runtimearea.png