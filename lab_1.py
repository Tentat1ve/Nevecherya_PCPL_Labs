import sys
import math

def get_coef(index, prompt):
    while True:
        try:
            if index < len(sys.argv) and sys.argv[index] != "invalid":
                coef_str = sys.argv[index]
                coef = float(coef_str)
                return coef
            else:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
                return coef
        except (ValueError, IndexError):
            print("Ошибка: введите действительное число")
            if index < len(sys.argv):
                sys.argv[index] = "invalid"

def get_roots(a, b, c):
    if a == 0:
        return ('Error', "Коэффициент A не может быть равен 0")
    
    D = b*b - 4*a*c
    print(f"Дискриминант D = {D}")
    
    if D < 0:
        return ('NoRoots',)
    
    t1 = (-b + math.sqrt(D)) / (2*a)
    t2 = (-b - math.sqrt(D)) / (2*a)
    
    print(f"Корни вспомогательного уравнения: t1 = {t1:.4f}, t2 = {t2:.4f}")
    
    result = []
    
    if t1 > 0:
        root1 = math.sqrt(t1)
        root2 = -math.sqrt(t1)
        result.extend([root1, root2])
        print(f"t1 > 0: корни x1 = {root1:.4f}, x2 = {root2:.4f}")
    elif t1 == 0:
        result.append(0.0)
        print("t1 = 0: корень x = 0")
    
    if t2 > 0 and t2 != t1:
        root3 = math.sqrt(t2)
        root4 = -math.sqrt(t2)
        result.extend([root3, root4])
        print(f"t2 > 0: корни x3 = {root3:.4f}, x4 = {root4:.4f}")
    elif t2 == 0 and t1 != 0:
        result.append(0.0)
        print("t2 = 0: корень x = 0")
    
    result = sorted(list(set(result)))
    
    if not result:
        return ('NoRoots',)
    elif len(result) == 1:
        return ('OneRoot', result[0])
    elif len(result) == 2:
        return ('TwoRoots', result[0], result[1])
    elif len(result) == 3:
        return ('ThreeRoots', result[0], result[1], result[2])
    else:
        return ('FourRoots', result[0], result[1], result[2], result[3])

def print_roots(roots_tuple):
    match roots_tuple:
        case ('FourRoots', root1, root2, root3, root4):
            print(f'Действительные корни: {root1:.6f}, {root2:.6f}, {root3:.6f}, {root4:.6f}')
        case ('ThreeRoots', root1, root2, root3):
            print(f'Действительные корни: {root1:.6f}, {root2:.6f}, {root3:.6f}')
        case ('TwoRoots', root1, root2):
            print(f'Действительные корни: {root1:.6f}, {root2:.6f}')
        case ('OneRoot', root):
            print(f'Действительный корень: {root:.6f}')
        case ('NoRoots',):
            print('Нет действительных корней')
        case ('Error', message):
            print(f'Ошибка: {message}')

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
        
    roots = get_roots(a, b, c)
    print_roots(roots)

if __name__ == "__main__":
    main()