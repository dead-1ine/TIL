# What is Docker ?

Docker는 컨테이너 기반의 오픈소스 가상화 플랫폼이다.

다양한 프로그램, 실행 환경을 컨테이너로 추상화하고 동일한 인터페이스를 제공하여 프로그램의 배포 및 관리를 단순하게 해준다.

백엔드 프로그램, 데이터베이스 서버, 메시지 큐 등 어떤 프로그램도 컨테이너로 추상화할 수 있다.



## Container

컨테이너는 격리된 공간에서 프로세스가 동작하는 기술이다.

기존의 방식인 OS 가상화를 사용하는 대표적인 가상머신은 VMWare와 VirtualBox이다.
이 가상머신은 호스트 OS 위에 게스트 OS 전체를 가상화하여 사용하는 방식이다.

이 방식은 여러가지의 OS를 가상화할 수 있고 비교적 사용법이 간단하지만 무겁고 느려서 운영환경에서 사용할 수 없다.

이러한 상황을 개선하기 위해 CPU의 가상화 기술(HVM)을 이용한 KVM(Kernel-based Virtual Machine)과 반가상화(Paravirtualization)방식의 Xen이 등장한다. 이러한 방식은 게스트 OS가 필요하긴 하나 전체 OS를 가상화하는 방식이 아니기에 호스트형 가상화 방식에 비해 성능이 뛰어나다.

하지만, 전가상화나 반가상화는 추가적인 OS 설치를 통해 가상화하기에 결국 성능에 대한 문제가 있었고, 이를 개선하기 위해 프로세스를 격리하는 방식이 등장한다.

리눅스에서는 이 방식을 리눅스 컨테이너라 하고, 단순히 프로세스를 격리하기 때문에 가볍고 빠르게 동작한다. CPU나 메모리는 프로세스가 필요한 만큼만 추가로 사용하며 성능적으로도 거의 손실이 없는 것이 장점이다.

하나의 서버에 여러 개의 컨테이너를 실행하면 서로 영향을 미치지 않고 독립적으로 실행되어 마치 가벼운 VM을 사용하는 느낌을 준다.

실행중인 컨테이너에 접속하여 명령어를 입력할 수 있고, `apt-get`이나 `yum`으로 패키지를 설치할 수도 있으며, 여러 개의 프로세스를 백그라운드로 실행할 수도 있다. 또한, CPU나 메모리 사용량을 제한할 수 있고 호스트의 특정 포트와 연결하거나 호스트의 특정 디렉토리를 내부 디렉토리인 것처럼 사용할 수도 있다.

도커에서 가장 중요한 개념은 컨테이너와 이미지라는 개념이다.

이미지는 컨테이너 실행에 필요한 파일과 설정값 등을 포함하고 있는 것으로, 상태값을 가지지 않고 변하지 않는다.

컨테이너는 이미지를 실행한 상태라고 볼 수 있으며, 추가되거나 변하는 값은 컨테이너에 저장된다.

같은 이미지에서 여러 개의 컨테이너를 생성할 수 있으며, 컨테이너의 상태가 바뀌거나 컨테이너가 삭제되더라도 이미지는 변하지 않고 그대로 남아있다.



## Docker가 핫한 이유

도커는 완전히 새로운 기술이 아니다. 하지만 컨테이너, 오버레이 네트워크, 유니온 파일 시스템 등의 이미 존재하는 기술을 잘 조합하고 사용하기 쉽게 만든 것이 없었으며, 사용자들이 원하는 기능을 간단하지만 획기적인 아이디어로 구현하여 인기를 끌었다.

도커 이미지는 컨테이너를 실행하기 위한 모든 정보를 가지고 있어 용량이 보통 수백MB에 이른다. 처음 이미지를 다운받을 때는 크게 부담되지 않지만 기존 이미지에 파일 하나를 추가했다고 수백MB를 다시 다운받는다면 매우 비효율적일 수 밖에 없다.

도커는 이런 문제를 해결하기 위해 레이어(layer)라는 개념을 사용하고 유니온 파일 시스템을 이용하여 여러 개의 레이어를 하나의 파일 시스템으로 사용할 수 있게 한다. 이미지는 여러 개의 읽기 전용 레이어로 구성되고, 파일이 추가도ㅚ거나 수정되면 새로운 레이어가 생성된다.

컨테이너를 생성할 때도 레이어 방식을 사용하는데, 기존 이미지 레이어 위에 읽기/쓰기 레이어를 추가한다. 이미지 레이어는 그대로 사용하면서 컨테이너가 실행중에 생성하는 파일이나 변경된 내용은 읽기/쓰기 레이어에 저장되므로 여러 개의 컨테이너를 생성해도 최소한의 용량만 사용한다.

가상화의 특성상 이미지 용량이 크고 여러 대의 서버에 배포하는 것을 감안하면 단순한 방법이지만 굉장히 영리한 설계로 보인다.



## Docker File

도커는 이미지를 만들기 위해 `Docker File`이라는 파일에 자체 DSL(Domain-specific language)언어를 이용하여 이미지 생성 과정을 작성할 수 있다. 

이러한 방법은 굉장히 간단하면서도 유용한 아이디어이다. 서버에 어떠한 프로그램을 설치하려고 의존성 패키지를 이것저것 설치하고 설정 파일을 만들었던 경험이 있다면 더 이상 이러한 과정을 블로깅하거나 메모장에 작성하는 것이 아닌 `Docker File`로 관리하면 된다.

도커 이미지의 용량은 보통 수백메가에서 수기가가 넘는 경우도 흔하다. 이렇게 큰 용량의 이미지를 서버에 저장하고 관리하는 것은 쉽지 않은 일인데, 도커는 Docker Hub를 통해 공개 이미지를 무료로 관리해준다. (하루에도 엄청난 용량의 이미지가 전 세계에서 다운로드 될텐데 트래픽 비용 등을 Docker에서 감당한다.)



## Command & API

도커 클라이언트의 명령어는 정말 잘 만들어져 있다.

대부분의 명령어는 직관적이고 사용하기 쉬우며 컨테이너의 복잡한 시스템 구성을 이해하지 못하더라도 편하게 사용할 수 있다.

또한 HTTP 기반의 REST API도 지원하여 확장성이 굉장히 좋고 훌륭한 Third Party 툴이 나오기 좋은 환경이다.

