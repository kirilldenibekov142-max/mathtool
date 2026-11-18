import sys
import math
MAX_VALUE = 10000

def print_help():
    print ("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print ("\n Использование:")
    print ("    python mathtool.py                         вывод справки")
    print ("    python mathtool.py --help                  вывод справки")
    print ("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print ("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print (f"\n Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_VALUE}.")

def parse_arguments(args):
    # Если запуск без параметров или с --help
    if len(args) == 0 or args[0] == "--help":
        print_help()
        sys.exit(0)

    if args[0] != "solve":
        print("ОШИБКА: неизвестная команда", file=sys.stderr)
        sys.exit(1)

    if len(args) == 1:
        a_str = input ("Введите коэффициент A: ")
        b_str = input("Введите коэффициент B: ")
        c_str = input("Введите коэффициент C: ")
        return a_str, b_str, c_str
    elif len(args) == 7:
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            print("ОШИБКА: неизвестный параметр", file=sys.stderr)
            sys.exit(1)
        return args[2], args[4], args[6]
    else:
        print("ОШИБКА: неверный набор параметров", file=sys.stderr)
        sys.exit(1)

def convert_to_int(a_str, b_str, c_str):
    try:
        return int(a_str), int(b_str), int(c_str)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)

def validate_range(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)

def solve(a, b, c):
    if a == 0:
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {x:.3f}")
            sys.exit(0)
        else:
            # А = 0 и B = 0 — это не уравнение!
            print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
            sys.exit(1)
    else:
        print("Уравнение квадратное")
        d = b * b - 4 * a * c
        print(f"D = {d}")
        
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif d == 0:
            x = -b / (2 * a)
            print(f"x = {x:.3f}")
        else:
            print ("Действительных корней нет")
        sys.exit(0)

def main():
    a_str, b_str, c_str = parse_arguments(sys.argv[1:])
    a, b, c = convert_to_int(a_str, b_str, c_str)
    validate_range(a, b, c)
    solve(a, b, c)
if __name__ == "__main__":
    main()