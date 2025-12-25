import unittest
from rk2 import UniversitySystem, Course, Teacher, TeacherCourse

class TestUniversitySystem(unittest.TestCase):
    def setUp(self):
        self.system = UniversitySystem()
        self.courses = [
            Course(1, "Математический анализ"),
            Course(2, "Физика"),
            Course(3, "Программирование"),
        ]
        
        self.teachers = [
            Teacher(1, "Абрамов", 50000, 1),
            Teacher(2, "Антонов", 60000, 1),
            Teacher(3, "Борисов", 55000, 2),
            Teacher(4, "Алексеев", 45000, 3),
            Teacher(5, "Смирнов", 70000, 3),
        ]
        
        self.teacher_courses = [
            TeacherCourse(1, 1),
            TeacherCourse(2, 1),
            TeacherCourse(3, 2),
            TeacherCourse(4, 3),
            TeacherCourse(5, 3),
            TeacherCourse(1, 3), 
        ]
        self.system.load_data(self.courses, self.teachers, self.teacher_courses)
    
    def test_query_1_teachers_starting_with_a(self):
        result = self.system.query_1_teachers_starting_with_a()
        expected = [
            ("Абрамов", "Математический анализ"),
            ("Алексеев", "Программирование"),
            ("Антонов", "Математический анализ"),
        ]
        self.assertEqual(len(result), 3, "Должно быть 3 преподавателя на 'А'")
        self.assertListEqual(result, expected, "Результаты не совпадают с ожидаемыми")
        for surname, _ in result:
            self.assertTrue(surname.startswith('А'), f"Фамилия {surname} должна начинаться с 'А'")
    
    def test_query_2_min_salary_per_course(self):
        result = self.system.query_2_min_salary_per_course()
        expected = [
            ("Программирование", 45000),
            ("Физика", 55000),
            ("Математический анализ", 50000),
        ]
        self.assertEqual(len(result), 3, "Должно быть 3 курса")     
        self.assertEqual(set(result), set(expected), "Минимальные зарплаты не совпадают")
        salaries = [salary for _, salary in result]
        self.assertEqual(salaries, sorted(salaries), "Результаты должны быть отсортированы по зарплате")
    
    def test_query_3_all_teacher_course_m2m(self):
        result = self.system.query_3_all_teacher_course_m2m()
        
        expected = [
            ("Абрамов", "Математический анализ"),
            ("Абрамов", "Программирование"),  
            ("Алексеев", "Программирование"),
            ("Антонов", "Математический анализ"),
            ("Борисов", "Физика"),
            ("Смирнов", "Программирование"),
        ]
        
        self.assertEqual(len(result), 6, f"Должно быть 6 связей, получено {len(result)}")
        
        self.assertListEqual(result, expected, "Связи не совпадают с ожидаемыми")
        
        surnames = [surname for surname, _ in result]
        self.assertEqual(surnames, sorted(surnames), "Результаты должны быть отсортированы по фамилии")
        
        abramov_count = sum(1 for surname, _ in result if surname == "Абрамов")
        self.assertEqual(abramov_count, 2, "У Абрамова должно быть 2 связи")

    def test_empty_data(self):
        empty_system = UniversitySystem()
        empty_system.load_data([], [], [])        
        self.assertEqual(empty_system.query_1_teachers_starting_with_a(), [])
        self.assertEqual(empty_system.query_2_min_salary_per_course(), [])
        self.assertEqual(empty_system.query_3_all_teacher_course_m2m(), [])

if __name__ == '__main__':
    unittest.main()