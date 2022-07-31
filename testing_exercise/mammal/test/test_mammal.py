from project.mammal import Mammal

from unittest import TestCase, main


class MammalTest(TestCase):

    def test_mammal_is_initialized_correctly(self):
        mammal = Mammal('Niko', 'hippo', 'huu')

        self.assertEqual('Niko', mammal.name)
        self.assertEqual('hippo', mammal.type)
        self.assertEqual('huu', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal('Niko', 'hippo', 'huu')

        actual_result = mammal.make_sound()
        expected_result = f"{mammal.name} makes {mammal.sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        mammal = Mammal('Niko', 'hippo', 'huu')

        actual_result = mammal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, actual_result)

    def test_info__returns_proper_string(self):
        mammal = Mammal('Niko', 'hippo', 'huu')
        actual_result = mammal.info()
        expected_result = f"{mammal.name} is of type {mammal.type}"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
