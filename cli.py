from src.repository import StudentRepository
from src.service import StudentService
from src.constants import (
    MENU_TITLE, MENU_ADD, MENU_VIEW, MENU_UPDATE, MENU_DELETE,
    MENU_SORT, MENU_TOP, MENU_EXIT, PROMPT_CHOICE, MSG_NO_STUDENTS,
    MSG_INVALID_CHOICE, MSG_SHUTDOWN, MSG_ID_NOT_NUMBER,MSG_NO_TOP_STUDENTS,
    MSG_AGE_GRADE_ERROR, DISPLAY_HEADER, DISPLAY_TOP_HEADER,
    PROMPT_STUDENT_ID, PROMPT_REMOVE_ID, PROMPT_NAME, PROMPT_AGE, PROMPT_GRADE
)


def main():
    repo = StudentRepository()
    service = StudentService(repo)

    while True:
        print(MENU_TITLE)
        print(MENU_ADD)
        print(MENU_VIEW)
        print(MENU_UPDATE)
        print(MENU_DELETE)
        print(MENU_SORT)
        print(MENU_TOP)
        print(MENU_EXIT)

        choice = input(PROMPT_CHOICE)

        if choice == "1":
            while True:
                try:
                    s_id = int(input(PROMPT_STUDENT_ID))
                    break
                except ValueError:
                    print(MSG_ID_NOT_NUMBER)
            
            name = input(PROMPT_NAME)
            try:
                age = int(input(PROMPT_AGE))
                grade = float(input(PROMPT_GRADE))
                service.add_student(s_id, name, age, grade)
            except ValueError:
                print(MSG_AGE_GRADE_ERROR)

        elif choice == "2":
            students = service.get_all_students()
            if not students:
                print(MSG_NO_STUDENTS)
            else:
                print(DISPLAY_HEADER)
                for s in students:
                    print(f"ID: {s.student_id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

        elif choice == "3":
            while True:
                try:
                    s_id = int(input(PROMPT_STUDENT_ID))
                    break
                except ValueError:
                    print(MSG_ID_NOT_NUMBER)
            service.update_student(s_id)

        elif choice == "4":
            while True:
                try:
                    s_id = int(input(PROMPT_REMOVE_ID))
                    break
                except ValueError:
                    print(MSG_ID_NOT_NUMBER)
            service.delete_student(s_id)

        elif choice == "5":
            service.sort_students()
            students = service.get_all_students()
            if students:
                print(DISPLAY_HEADER)
                for s in students:
                    print(f"ID: {s.student_id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

        elif choice == "6":
            top = service.get_top_students()
            if not top:
                print(MSG_NO_TOP_STUDENTS)
            else:
                print(DISPLAY_TOP_HEADER)
                for s in top:
                    print(f"{s.name}: {s.grade}")

        elif choice == "7":
            print(MSG_SHUTDOWN)
            break

        else:
            print(MSG_INVALID_CHOICE)


if __name__ == "__main__":
    main()