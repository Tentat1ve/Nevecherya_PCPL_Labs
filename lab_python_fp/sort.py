def sort_by_abs_descending(data):
    return sorted(data, key=abs, reverse=True)

def sort_by_abs_descending_lambda(data):
    return sorted(data, key=lambda x: abs(x), reverse=True)

def sort_strings_ignore_case(data):
    return sorted(data, key=str.lower)


if __name__ == '__main__':
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    
    result = sort_by_abs_descending(data)
    print("Без lambda:", result)
    
    result_with_lambda = sort_by_abs_descending_lambda(data)
    print("С lambda:", result_with_lambda)
    
    strings = ["яблоко", "Банан", "апельсин", "Вишня"]
    sorted_strings = sort_strings_ignore_case(strings)
    print("Строки без учета регистра:", sorted_strings)