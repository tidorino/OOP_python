from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train('Train', 30)

    def test_init(self):
        self.assertEqual('Train', self.train.name)
        self.assertEqual(30, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add__if_train_no_free_capacity_expected_to_raise(self):
        self.train = Train('train', 2)
        self.train.passengers = ['passenger1', 'passenger2']
        with self.assertRaises(ValueError) as ex:
            self.train.add('passenger3')
        self.assertEqual('Train is full', str(ex.exception))

    def test_add__if_passenger_already_on_train_expected_to_raise(self):
        self.train = Train('train', 2)
        self.train.passengers = ['passenger2']
        with self.assertRaises(ValueError) as ex:
            self.train.add('passenger2')
        self.assertEqual('Passenger passenger2 Exists', str(ex.exception))

    def test_add__passenger(self):
        self.train = Train('train', 2)
        self.train.passengers = ['passenger1']
        result = self.train.add('passenger2')
        expected = 'Added passenger passenger2'
        self.assertEqual(expected,  result)

    def test_remove__if_passenger_not_on_train_expected_to_raise(self):
        self.train = Train('train', 2)
        self.train.passengers = ['passenger2']
        with self.assertRaises(ValueError) as ex:
            self.train.remove('passenger1')
        self.assertEqual('Passenger Not Found', str(ex.exception))

    def test_remove__passenger(self):
        self.train = Train('train', 2)
        self.train.passengers = ['passenger1']
        self.train.add('passenger2')
        result = self.train.remove('passenger1')
        expected = 'Removed passenger1'
        self.assertEqual(expected,  result)


if __name__ == '__main__':
    main()