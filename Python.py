# 파일 경로
file_path = "grades.txt"

# 성적 입력 함수
def input_grades():
    grades = {}
    subjects = ["국어", "수학", "영어", "사회", "과학", "한국사"]
    for subject in subjects:
        grade = int(input(f"{subject} 성적을 입력하세요: "))
        grades[subject] = grade
    return grades

# 평균 계산 함수
def calculate_average(grades):
    return sum(grades.values()) / len(grades)

# 성적 파일 저장 함수
def save_grades(name, grades, average):
    with open(file_path, "a") as f:
        f.write(f"{name}\t{grades['국어']}\t{grades['수학']}\t{grades['영어']}\t{grades['사회']}\t{grades['과학']}\t{grades['한국사']}\t{average:.1f}\n")
    print("성적이 저장되었습니다.")

# 성적 조회 함수
def find_grades(name):
    with open(file_path, "r") as f:
        for line in f:
            data = line.strip().split("\t")
            if data[0] == name:
                grades = {
                    "국어": int(data[1]),
                    "수학": int(data[2]),
                    "영어": int(data[3]),
                    "사회": int(data[4]),
                    "과학": int(data[5]),
                    "한국사": int(data[6]),
                }
                average = float(data[7])
                print(f"{name}의 성적: {grades}, 평균: {average:.1f}")
                return True
        print(f"{name}의 성적을 찾을 수 없습니다.")
        return False

# 프로그램 시작
print("성적 기록 프로그램을 시작합니다.")

while True:
    choice = input("성적을 입력하시겠습니까? 조회하시겠습니까? (I: 입력, F: 조회, Q: 종료) ")
    if choice.upper() == "I":
        name = input("이름을 입력하세요: ")
        grades = input_grades()
        average = calculate_average(grades)
        save_grades(name, grades, average)
    elif choice.upper() == "F":
        name = input("성적을 조회할 학생의 이름을 입력하세요: ")
        if not find_grades(name):
            continue
    elif choice.upper() == "Q":
        break
    else:
        print("잘못된 입력입니다.")

print("성적 기록 프로그램을 종료합니다.")
