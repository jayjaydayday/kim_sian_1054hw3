from components import variables
import webbrowser as wb


def result(status):
    # Question 1
    print("\n---------------------------------------------------\n")
    print("\033[0;33;40mWhat musical style do you prefer?\n")
    q1 = input("rap, rock, jazz, heavy metal:\033[m ")

    if q1 == "rap":
        variables.Hulk += 1

    elif q1 == "rock":
        variables.IronMan += 1

    elif q1 == "jazz":
        variables.CaptainAmerica += 1

    elif q1 == "heavy metal":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 2
    print("\n---------------------------------------------------\n")
    print("\033[0;33;40mWhat food do you prefer?\n")
    q2 = input("taco, cheeseburger, vegetable, candy:\033[m ")

    if q2 == "taco":
        variables.Hulk += 1

    elif q2 == "cheeseburger":
        variables.IronMan += 1

    elif q2 == "vegetable":
        variables.CaptainAmerica += 1

    elif q2 == "candy":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 3
    print("\n---------------------------------------------------\n")
    print("\033[0;33;40mIn your free time, what you prefer to do?\n")
    q3 = input("bowling, video game, dancing, play drums:\033[m ")

    if q3 == "bowling":
        variables.Hulk += 1

    elif q3 == "video game":
        variables.IronMan += 1

    elif q3 == "dancing":
        variables.CaptainAmerica += 1

    elif q3 == "play drums":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 4
    print("\n---------------------------------------------------\n")
    print("\033[0;33;40mWhich vehicle do you prefer?\n")
    q4 = input("monster truck, lamborghini, harley-davidson, hotwheels:\033[m ")

    if q4 == "monster truck":
        variables.Hulk += 1

    elif q4 == "lamborghini":
        variables.IronMan += 1

    elif q4 == "harley-davidson":
        variables.CaptainAmerica += 1

    elif q4 == "hotwheels":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n\033[m---------------------------------------------------\n")

    # Question 5
    print("\n---------------------------------------------------\n")
    print("\033[0;33;40mWhere would you prefer to travel on vacation?\n")
    q5 = input("Thailand, Monaco, Hawaii, San Francisco:\033[m ")

    if q5 == "Thailand":
        variables.Hulk += 1

    elif q5 == "Monaco":
        variables.IronMan += 1

    elif q5 == "Hawaii":
        variables.CaptainAmerica += 1

    elif q5 == "San Francisco":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Result
    print("\n---------------------------------------------------\n")
    if variables.Hulk >= 3:
        answer = variables.Hulk
        print("\033[0;30;42mYou are Hulk\033[m")
        wb.open("https://www.marvel.com/characters/hulk-bruce-banner")

    elif variables.IronMan >= 3:
        answer = variables.IronMan
        print("\033[0;37;41mYou are Iron Man\033[m")
        wb.open("https://www.marvel.com/characters/iron-man-tony-stark")

    elif variables.CaptainAmerica >= 3:
        answer = variables.CaptainAmerica
        print("\033[0;37;44mYou are Captain America\033[m")
        wb.open("https://www.marvel.com/characters/captain-america-steve-rogers")

    elif variables.AntMan >= 3:
        answer = variables.AntMan
        print("\033[0;31;43mYou are Ant-Man\033[m")
        wb.open("https://www.marvel.com/characters/ant-man-scott-lang")

    else:
        answer = variables.DocStrange
        print("\033[0;30;47mYou are strange, Doctor Strange\033[m")
        wb.open("https://www.marvel.com/characters/doctor-strange-stephen-strange")
