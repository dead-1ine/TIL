# stash

> Git에서 제공하는 임시 저장소 기능으로, 작업중인 내용을 잠시 저장해두었다가 필요할 때 다시 불러올 수 있게 해준다.

- 활용 상황: 
    - 현재 작업 중인 내용이 아직 커밋할 만큼 완료되지 않았지만, 다른 브랜치로 체크아웃해야 할 경우 혹은 다른 작업을 해야 할 경우

1. `git stash save | stash ` : 현재 작업중인 내용을 임시 저장소에 저장하고, 작업 디렉토리를 깨끗한 상태로 되돌린다.
2. `git stash list`: 현재 저장된 stash 목록을 출력한다.
3. `git stash apply`: 가장 최근에 저장된 stash를 다시 적용한다.
4. `git stash pop`: 가장 최근에 저장된 stash를 다시 적용하고, 해당 stash를 목록에서 삭제한다.
5. `git stash drop`: 가장 최근에 저장된 stash를 목록에서 삭제한다.
6. `git stash clear`: 모든 stash를 삭제한다.



또한, `stash apply, pop, drop` 명령어에 stash의 이름을 지정하여 특정 stash를 다룰 수 있다. 예를 들어, `git stash apply stash@{1}`명령은 `stash@{1}`에 해당하는 stash를 적용한다.

`git stash`명령은 수정된 추적 파일과 스테이징된 변경 사항만 저장하며, 새로운 파일(추적되지 않은 파일)은 기본적으로 저장하지 않는다. 새 파일을 stash하려면 `git stash save --include-untracked` 또는 `git stash -u`를 사용하면 된다.

마지막으로, stash는 브랜치 간에 이동시킬 수 없다. 즉, stash는 해당 브랜치에서만 접근이 가능하며, 다른 브랜치로 체크아웃한 경우 해당 stash를 볼 수 없다.