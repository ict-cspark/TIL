# CLI (Command Line interface)

---

`~` : **홈 디렉토리** (현재 로그인된 사용자의 홈 폴더를 의미)

`/` :  **루트 디렉토리** (모든 파일과 폴더를 담고 있는 최상위 폴더)



**절대 경로** : 어떤 위치에서도 접근할 수 있는 경로 (모든 경로를 전부 작성) ex) A/B/F 

**상대 경로** : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 경로 ex) ./F (현재폴더)  ex) ../B/F (상위폴더)

`.` : 현재 작업하는 위치

`..` : 현재 작업하는 위치의 상위 위치(상위폴더/부모폴더)

---

## 터미널 명령어

## 파일 생성

**touch** : 파일 생성 명령어

```bash
$ touch 파일명
```

---

## 폴더 생성

**mkdir** : 폴더 생성 명렁어

```bash
$ mkdir 폴더명

$ mkdir '폴더명을 띄어쓰고 싶을 때 따옴표로 작성' 

$ mkdir 폴더의경로를/상대경로로/지정할수있음
```

---

## 파일/폴더의 목록 확인

**ls** : 현재 위치의 폴더/파일의 목록을 보고 싶을 때 사용하는 명령어

```bash
$ ls -a : 접근 가능한 모든 폴더/파일 확인

$ ls -l : 자세한 정보까지 확인하고 싶을 때

$ ls
```

---

## 파일/폴더 이동하기

**mv** : 폴더/파일을 다른 위치로 이동하거나 이름 변경할 때 사용

```bash
$ mv 이동하려는파일명 이동하는위치

$ mv 이름변경하려는파일명 변경하려는 이름
```

---

## 현재 위치 이동하기

**cd** : 현재 위치를 이동하기 위한 명령어

```bash
$ cd 이동할위치

$ cd .. : 이전 디렉토리

$ cd ~ : 홈 디렉토리

$ cd  / : 루트 디렉토리
```

---

## 폴더/파일 삭제

**rm** : 폴더/파일 삭제하는 명령어

```bash
$ rm 삭제하려는파일명

$ rm -r 삭제하려는폴더명

$ rm -rf 폴더명 : 폴더 무조건(강제) 삭제

주의 : 휴지통 개념이 없음 즉, 되 살 릴 수 없 다!
```

---

## 폴더/파일 열기

**start** : 폴더/파일을 여는 명령어

``` bash
$ start 폴더/파일명
```

---

## 꿀 같은 단축키

+ 위, 아래 방향키 : 과거의 작성한 명령어를 조회

+ tab 키 : 자동완성

+ ctrl + l : 화면 클리어

+ ctrl + insert : 복사

+ shift + insert : 붙여넣기

+ ctrl + 좌우방향키 : 커서 맨앞, 맨뒤 이동