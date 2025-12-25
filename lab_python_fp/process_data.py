import json
import sys
import os
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from sort import sort_strings_ignore_case

path = "data_light.json"

try:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Ошибка загрузки JSON: {e}")
    sys.exit(1)

@print_result
def f1(arg):
    job_names = list(Unique(field(arg, 'job-name'), ignore_case=True))
    return sort_strings_ignore_case(job_names)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]

if __name__ == '__main__':
    print("\nЗапуск обработки данных...")
    with cm_timer_1():
        result = f4(f3(f2(f1(data))))
    