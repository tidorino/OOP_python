from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(4)

    def test_initialization_if_correct(self):
        self.assertEqual(4, self.plantation.size)
        self.assertEqual([], self.plantation.workers)
        self.assertEqual({}, self.plantation.plants)

    def test_initialization_if_size_less_than_0(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation = Plantation(-1)
        self.assertEqual('Size must be positive number!', str(ex.exception))

    def test_initialization_if_size_equal_or_more_than_0(self):
        plantation = Plantation(0)
        self.assertEqual(0, plantation.size)

    def test_hire_worker__if_worker_already_hired_expect_to_raise(self):
        worker = 'Worker'
        plantation = Plantation(1)
        plantation.workers = [worker]
        self.assertTrue(worker in plantation.workers)

        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker(worker)
        self.assertEqual('Worker already hired!', str(ex.exception))

    def test_hire_worker__if_worker_not_yet_hired(self):
        worker = 'Worker'
        self.assertFalse(worker in self.plantation.workers)

        result = self.plantation.hire_worker(worker)
        self.assertEqual(len(self.plantation.workers), 1)
        self.assertEqual(f'{worker} successfully hired.', result)

    def test_len__add_length_of_each_planted_plant_in_plant_counter(self):
        plant_count = 1
        plantation = Plantation(1)
        plantation.plants['Worker'] = ['plant']
        self.assertEqual(plantation.__len__(), 1)
        result = plantation.__len__()
        self.assertEqual(plant_count, result)

    def test_len__plant_counter_does_not_change_if_plant_not_in_plants_dict(self):
        plant_count = 0
        plantation = Plantation(1)
        plantation.plants['Plant'] = []
        self.assertEqual(plantation.__len__(), plant_count)
        result = plantation.__len__()
        self.assertEqual(plant_count, result)

    def test_len__(self):
        plantation = Plantation(2)
        plantation.plants['Worker1'] = ['carrot1']
        plantation.plants['Worker2'] = ['carrot2']
        self.assertEqual(plantation.__len__(), 2)

    def test_planting__worker_not_hired_expect_to_raise(self):
        worker = 'Worker'

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(worker, 'Plant')
        self.assertEqual(f'Worker with name Worker is not hired!', str(ex.exception))

    def test_planting__check_if_plantation_is_full(self):
        worker = 'Worker'
        plantation = Plantation(1)
        plantation.workers = [worker]
        plantation.plants[worker] = ['plant']
        self.assertTrue(worker in plantation.workers)

        with self.assertRaises(ValueError) as ex:
            plantation.planting(worker, 'Carrot')
        self.assertEqual('The plantation is full!', str(ex.exception))

    def test_planting__check_if_worker_is_hired_add_plant(self):
        worker = 'Worker'
        plant = 'Carrot'
        plantation = Plantation(1)
        plantation.workers = [worker]
        plantation.plants[worker] = []

        result = plantation.planting(worker, plant)
        self.assertEqual(f'Worker planted Carrot.', result)

    def test_planting__add_worker_and_plant_to_plantation_if_worker_not_in_list(self):
        worker = 'Worker'
        plant = 'Carrot'
        plantation = Plantation(1)
        plantation.workers = [worker]

        result = plantation.planting(worker, plant)
        self.assertEqual(f"Worker planted it's first Carrot.", result)

    def test_str__get_info(self):
        worker = 'Worker'
        plantation = Plantation(2)
        plantation.workers = [worker]
        plantation.plants[worker] = ['plant', 'carrot']
        result = plantation.__str__()
        expected_result = f'Plantation size: 2\nWorker\nWorker planted: plant, carrot'
        self.assertEqual(expected_result, result)

    def test_repr__get_info(self):
        worker = 'Worker'
        plantation = Plantation(1)
        plantation.workers = [worker]
        plantation.plants[worker] = ['plant', 'carrot']
        result = plantation.__repr__()
        expected_result = f'Size: 1\nWorkers: Worker'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
