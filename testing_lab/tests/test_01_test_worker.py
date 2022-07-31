from testing_lab.app.test_worker import Worker

from unittest import TestCase, main

"""
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values

"""


class TestWorker(TestCase):

    def test_worker_is_initialized_correctly(self):
        worker = Worker('Moni', 100, 10)

        self.assertEqual('Moni', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_workers_energy_increased_after_rest(self):
        # Arrange
        worker = Worker('Moni', 100, 10)

        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        # Arrange
        worker = Worker('Moni', 100, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_work_with_negative_energy_raises(self):
        # Arrange
        worker = Worker('Moni', 100, -3)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_workers_money_increased_after_work(self):
        # Arrange
        worker = Worker('Moni', 100, 10)

        self.assertEqual(0, worker.money)
        # Act
        worker.work()

        # Assert
        self.assertEqual(100, worker.money)

        # Act
        worker.work()
        # Assert
        self.assertEqual(200, worker.money)

    def test_workers_energy_is_decreased_after_working(self):
        # Arrange
        worker = Worker('Moni', 100, 10)

        self.assertEqual(10, worker.energy)
        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker('Moni', 100, 10)

        actual_result = worker.get_info()
        expected_result = 'Moni has saved 0 money.'

        # Act
        worker.get_info()

        # Assert
        self.assertEqual(expected_result, actual_result)

        worker.work()

        actual_result = worker.get_info()
        expected_result = 'Moni has saved 100 money.'

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()


