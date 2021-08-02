### Git 정리

1. add, commit 수정 및 변경

	-  Add 취소
		```Terminal
			git reset HEAD fileName
		```
		- fileName이 없다면 전체 취소

	- Commit 취소 및 변경
		- commit을 취소하고 해당 파일들을 staged 상태로 디렉터리에 보존
			`git reset --soft HEAD^`
		- commit을 취소하고 해당 파일들을 unstaged 상태로 디렉터리에 보존
			`git reset --mixed HEAD^`
			`git reset HEAD^`
		- 마지막 2개의 commit을 취소
			`git reset HEAD~2`
		- commit을 취소하고 해당 파일들을 unstaged 상태로 디렉터리에서 삭제
			`git reset --hard HEAD^`

		- Commit Message 변경하기
			`git commit --amend`

	- Push 취소하기
		이 명령을 사용하면 자신의 local 내용을 remote에 강제로 덮어쓰기하기 때문에 주의해야 함
		`git reflog`
		`git log -g`
	\- 