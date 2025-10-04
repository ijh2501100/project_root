def greet(name):
    return f"안녕하세요, {name}님!"

def show_age(name, age):
    return f"{name}님은 {age}세입니다."

def main():
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    print(greet(name))
    print(show_age(name, age))

if __name__ == "__main__":
    main()