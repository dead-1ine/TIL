# 정말 기초적인 iOS

##### Storyboard

- Storyboard란 앱의 흐름을 나타내며, 시각적으로 화면을 구성하는 곳입니다.
	- 앱의 전반적인 형태와 앱의 화면 전환, 다양한 Object들을 관리해주는 곳입니다.
	AppDelegate.swift
	SceneDelegate.swift
### AppDelegate.swift

> "앱 전체의 실행 흐름을 컨트롤하는 객체로 앱이 처음 실행되거나 종료될 때 등으로 활성화될 때 호출되는 메서드로 구성되어 있다."
>
> - 앱 델리게이트 객체의 메소드 (각 메소드들은 그에 맞는 상태 변화에 따라 호출됨)
> - `application(_:willFinishiLaunchingWithOptions:)` : 앱이 구동되어 필요한 초기 실행 과정이 완료되기 직전에 호출되는 메소드
> - `application(_:didFinishiLaunchingWithOptions:)` : 앱이 사용자에게 화면으로 표시되기 직전에 호출되는 메소드 (앱이 실행된 후에 진행할 커스터마이징이나 초기화를 위한 코드를 작성하면 된다.)
> - `applicationDidBecomeActive(_:)` : 실행된 앱이 포그라운드, 즉 화면 전면에 표시될 때 호출되는 메소드 (앱이 Inactive 상태에 들어가면서 일시 중지된 작업이 있다면 이를 재시작하는 코드를 작성하면 된다.)
> - `applcationDidEngerBackground(_:)` : 앱이 백그라운드 상태에 진입했을 때 호출되는 메소드
> - `applicationWillTerminate(_:)` : 앱이 종료되기 직전에 호출되는 메소드 (사용자 데이터 등을 종료 전 한번 더 저장해두는 것이 좋다.)

##### ViewController.swift
> “도구 모음, 탐색 모음 및 응용프로그램 보기에 대한 보기 관리 기능을 제공합니다. 또한 UIViewController 클래스는 장치 방향이 변경될 때 모달 보기 및 회전 보기를 지원합니다.”

#### Main.storyboard



### Interface Builder - Storyboard와 Swift를 연결한다.

> 1. @IBOutlet
>
>    값에 접근하기 위한 변수
>
> 2. @IBAction
>
>    Event가 일어난 경우 호출되는 Func
>
>    
>
>    @ : 컴파일러에게 어떤 속성을 가진다고 전달하는 역할의 예약어

### Application의 실행 과정

> 1. main() 함수가 실행된다.
> 2. main() 함수는 다시 UIApplicationMain() 함수를 호출한다.
> 3. UIApplicationMain() 함수는 앱의 본체에 해당하는 UIApplication 객체를 생성한다.
> 4. UIApplication 객체는 Info.plist 파일을 바탕으로 앱에 필요한 데이터와 객체를 로드한다.
> 5. AppDelegate 객체를 생성하고 UIApplication 객체와 연결한다.
> 6. 이벤트 루프를 만드는 등 실행에 필요한 준비를 진행한다.
> 7. 실행 완료 직전, 앱 
> 8. 델리게이트의 application(_:didFinsishLaunchingWithOptions:) 메서도를 호출한다.

> ### iOS 앱 생명 주기
>
> ![스크린샷 2021-08-09 오후 12.43.25](/Users/dead_line/Library/Application Support/typora-user-images/스크린샷 2021-08-09 오후 12.43.25.png)



### iOS에서 앱이 가질 수 있는 상태값

| 상태        | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| Not Running | 앱이 시작되지 않았거나 실행되었지만 시스템에 의해 종료된 상태를 나타낸다. |
| Inactive    | 앱이 전면에서 실행 중이지만, 아무런 이벤트를 받지 않고 있는 상태를 나타낸다. |
| Active      | 앱이 전면에서 실행 중이며, 이벤트를 받고 있는 상태를 나타낸다. |
| Background  | 앱이 백그라운드에 있지만 여전히 코드가 실행되고 있는 상태를 나타낸다. <br />대부분의 앱은 Suspended 상태로 이행하는 도중에 일시적으로 이 상태에 진입하지만, 파일 다운로드나 업로드, 연산 처리 등 여분의 실행 시간이 필요한 앱일 경우 특정 시간 동안이 상태로 남아 있게 되는 경우도 있다. |
| Suspended   | 앱이 메모리에 유지되지만 실행되는 코드가 없는 상태이다. <br />메모리가 부족한 상황이 오면 iOS 시스템은 포그라운드에 있는 앱의 여유 메모리 공간을 확보하기 위해 Suspended 상태에 있는 앱들을 특별한 알림 없이 정리합니다. |



### Passing Data - 데이터를 넘겨주는 방법 6가지

> 1. Instance Property
>
>    - Property - 클래스에 속해있는 변수
>
>      - 접근 가능한 property에 데이터를 대입하고, navigation으로 push하여 데이터를 전달한다.
>
>      ```Swift
>      //MARK:- 1. 프로퍼티를 이용한 Data 전달
>      @IBAction func first(_ sender: Any) {
>        guard let vc = storyboard?.instantiateViewController(identifier: "secondViewController") as? SecondViewController else { return }
>        
>        vc.text = self.propertyTextField.text ?? ""
>        
>        // 이 프로퍼티에 접근해서 데이터를 저장했다고 그 자체로 저장되는 것이 아니라,
>        // 정확한 데이터의 전달은 이후 push에서 발생함
>        self.navigationController?.pushViewController(vc, animated: true)
>      }
>      ```
>
>      ```Swift
>      // 받는 ViewController
>      class SecondViewController: UIViewController {
>        @IBOutlet weak var textLabel: UILabel!
>        var text: String = ""
>        
>        override func viewDidLoad() {
>          super.viewDidLoad()
>          
>          self.textLabel.text = text
>        }
>      }
>      ```
>
> 2. Segueway
>
>    - .xib 파일 : XML 포맷으로 저장되는 Interface Builder파일의 줄임말
>    - 화면 내 들어갈 UI 요소와 크기 및 속성등은 XML 포맷으로 저장된다.
>    - Xcode 내에서 프로젝트를 컴파일할 때 소스코드를 컴파일하는 과정에서 이러한 .xib 파일들이 같이 컴파일된다.
>    - -> 이렇게 컴파일된 Interface Builder 파일은 '.nib' 파일로 저장된다.
>    - 즉, 스토리보드에 있는 각각의 View는 개별 nib 파일이다.
>
>    - Segue의 Destination이 ThirdViewController라면, ThirdViewController 형태로 vc에 할당하고, 접근하여 데이터를 전달하는 방식의 코드
>
>    ```Swift
>    override func prepare(for segue: UIStoryboardSegue, sender: Any) {
>      if segue.destination is ThirdViewController {
>        let vc = segue.destination as? ThirdViewController
>        vc?.text = self.segueTextField.text ?? ""
>      }
>    }
>    ```
>
> 3. Instance
>
> 4. Delegate
>
> 5. Closure
>
> 6. Notification


### DispatchQueue
- Async
- Sync
- Qos : 우선순위
- DispatchGroup
- main의 sync 에러에 대한 내용
----
# 차후에 정리해야 할 목록
> - @objc
> - 각각의 변수, 함수 등에 적용하여 Objective-c의 접근을 가능하게 해줌
> - @objcMembers
> - Class에 적용되며, Class 내의 함수, 변수 등 Objective-C에서 접근할 수 있게 함

