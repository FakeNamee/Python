import unittest
from Function import Traffic_light
from Function import My_Class
from Function import define_the_day
from Function import check_predicate
from Function import quarter_position
from Function import sum_of_numbers


class Test_for_function(unittest.TestCase):
    # Создаем тестовый случай
    def teste_qual(self):
        '''создаем сам тест'''
        '''используем функцию assertEqual'''
        self.assertEqual(define_the_day(7), "it's weekend!")

    def teste_not_qual(self):

        self.assertNotEqual(define_the_day(5), "it's weekend!")

    def test_true(self):
        '''используем функцию assertTrue'''
        res = check_predicate([1, 3, 7])
        self.assertTrue(res)

    def test_traffic_light(self):
        objectName = Traffic_light()
        # assertIsInstance() to check if obj is instance of class
        self.assertIsInstance(objectName, Traffic_light)

    def test_traffic_light_not(self):
        objectNamenew = Traffic_light()
        # assertIsInstance() to check if obj is instance of class
        self.assertNotIsInstance(objectNamenew, My_Class)

    def test_quarter_position(self):
        '''используем функцию quarter_position'''
        self.assertIn(quarter_position(4, -4), [1, 2, 3, 4])

    def test_TypeError(self):

        with self.assertRaises(TypeError):
            sum_of_numbers()

    def test_traffic_light_is(self):
        objectName = Traffic_light()
        objectName2 = objectName
        # assertIsInstance() to check if obj is instance of class
        self.assertIs(objectName, objectName2)

    def test_traffic_light_is_note(self):
        newobjectName = Traffic_light()
        newobjectName2 = Traffic_light()
        # assertIsInstance() to check if obj is instance of class
        self.assertIsNot(newobjectName2, newobjectName)

    def test_quarter_position_is_not_none(self):

        self.assertIsNotNone(quarter_position(4, -4))


# print(sum_of_numbers(7))
if __name__ == '__main__':
    unittest.main()