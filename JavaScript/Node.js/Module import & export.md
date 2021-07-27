##### Module import & export
- module.exports
- require()
![][image-1]

![][image-2]

##### 노드 내장 객체
- global
	> 브라우저의 window같은 역할
	> 모든 파일에서 접근 가능
	> window처럼 생략 가능  

- console
	- console.time - timeEnd

- 타이머 메서드
	- setTimeout

- __filename, __dirname
	> Node는 사용자의 폴더에 접근 가능하다.
	- __filename : 현재 파일 경로
	- __dirname : 현재 폴더 경로__

- process
- OS
	-  path.join(__dirname, ‘..’, ‘var.js’);__

[image-1]:	file:///.file/id=6571367.90844131
[image-2]:	file:///var/folders/yv/qg5rt_fs4bb614p_f10b2c1w0000gn/T/TemporaryItems/NSIRD_screencaptureui_uHUeWl/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-07-26%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.09.58.png width=500 height=500