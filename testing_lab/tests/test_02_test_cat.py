from testing_lab.app.test_cat import Cat

from unittest import TestCase, main

"""
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping

"""


class CatTest(TestCase):

    # def test_eat__expect_size_to_increase(self)
    def test_cat_size_is_increased_after_eating(self):
        cat = Cat('Molly')
        self.assertEqual(0, cat.size)

        cat.eat()
        self.assertEqual(1, cat.size)

    # def test_eat__expect_fed_to_be_true(self)
    def test_cat_is_fed_after_eating(self):
        cat = Cat('Molly')
        self.assertFalse(cat.fed)
        # Is Equal :self.assertEqual(False, cat.fed)

        cat.eat()
        self.assertEqual(True, cat.fed)
        # IsEqual: self.assertTrue(cat.fed)

    # def test_eat__when_fed_is_true_expect_to_raise(self)
    def test_cat_cannot_eat_if_is_fed_raises(self):

        cat = Cat('Molly')
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    # def test_sleep__when_fed_is_false_expect_to_raise(self)
    def test_cat_cannot_sleep_if_not_fed_raises(self):
        cat = Cat('Molly')
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('Molly')
        cat.eat()

        cat.sleep()
        self.assertFalse(cat.sleepy)

    def test_cat_is_sleepy_after_eat(self):
        cat = Cat('Molly')
        self.assertFalse(cat.sleepy)

        cat.eat()
        self.assertTrue(cat.sleepy)


if __name__ == '__main__':
    main()
