from components import questions
from components import variables


quiz = False
choice = ["y", "n"]

print("\n\033[0;31;40m ---------------------------------------------------\n")
print("                    Marvel Quiz                      \n")
print("            Which Marvel character are you?          \n")
print("\n---------------------------------------------------\033[m\n")

while quiz is False:
    questions.result(variables.answer)
    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("====== see ya! =======")
        exit()
    elif choice == "y":
        variables.Hulk = 0
        variables.IronMan = 0
        variables.CaptainAmerica = 0
        variables.AntMan = 0
        variables.DocStrange = 0
    quiz = False
