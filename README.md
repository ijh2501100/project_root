# project_root
# Python GitHub 과제

## 1. 과제 개요
- VS Code에서 Python 프로젝트를 생성하고 Git/GitHub을 활용하여 버전 관리 및 저장소 연동을 실습한다.  
- commit 메시지 규칙:  
  - 첫 번째: `ADD: ...`  
  - 이후 기능 추가: `MODIFY: ...`  
  - 코드 수정: `FIX: ...`  

---

## 2. 프로젝트 폴더 구조
```
project_root/
 ├─ src/
 │   └─ app.py
 ├─ doc/
 │   └─ images/
 │       ├─ capture1.png
 │       └─ capture2.png
 └─ README.md
```

---

## 3. 수행 과정
1. **src/app.py 작성 및 첫 commit**
   - commit 메시지: `ADD: app.py`  
   - 기능: 
   [def greet(name):
    return f"안녕하세요, {name}님!"

   def main():
    name = input("이름을 입력하세요: ")
    print(greet(name))

   if __name__ == "__main__":
    main()]  

2. **두 번째 commit**
   - commit 메시지: `MODIFY` 
   - 수정/추가한 내용: 
   [def show_age(name, age):
    return f"{name}님은 {age}세입니다."
    age = input("나이를 입력하세요: ")
    print(greet(name))
    print(show_age(name, age))]  

3. **세 번째 commit**
   - commit 메시지:`FIX`
   - 수정/추가한 내용: 
   [except ValueError:
        return "나이는 숫자로 입력해주세요."]  

---

## 4. 캡처 이미지
- `capture.png` → commit 완료 상태 화면  
- `capture2.png` → GitHub push → pull 후 VS Code 화면  

예시:  
![첫번째 캡처](doc/images/capture1.png)  
![두번째 캡처](doc/images/capture2.png)  

---

## 5. GitHub Repository URL
- URL: [https://github.com/ijh2501100/project_root.git]  

---

## 6. 느낀 점 (선택 사항)
- 이번 과제를 하면서 배운 점:  
- Git/GitHub을 활용하며 어려웠던 점:  
- 앞으로 더 해보고 싶은 것:  
