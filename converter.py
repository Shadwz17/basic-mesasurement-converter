import os


def cleanscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    cleanscreen()
    print("-- Measurement Converter --")
    print("Choose an option:\n")
    opt = input("1. CM to M\n2.M to KM\n3.KM to M\n4.M to CM\n99. Exit\n")

    match opt:
        case "1":
            cleanscreen()
            num = int(input("How many cm a meters?\n"))
            resultado = cm_m(num)
            print(resultado)

        case "2":
            cleanscreen()
            num = int(input("How many meters a km?\n"))
            resultado = m_km(num)
            print(resultado)

        case "3":
            cleanscreen()
            num = int(input("How many km to meters?\n"))
            resultado = km_m(num)
            print(resultado)

        case "4":
            cleanscreen()
            num = int(input("How many meters to cm?\n"))
            resultado = m_cm(num)
            print(resultado)

        case "99":
            pass

        case default:
            print("Invalid option")


def cm_m(num):
    return num / 100


def m_km(num):
    return num / 1000


def km_m(num):
    return num * 1000


def m_cm(num):
    return num * 100


start()
