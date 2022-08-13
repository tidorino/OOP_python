from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_init(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_init__if_size_is_negative_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -2
        self.assertEqual('Size must be positive number!', str(ex.exception))

    def test_hire_worker__if_worker_is_already__hire_raise(self):
        self.plantation.workers = ['worker1']
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('worker1')
        self.assertEqual('Worker already hired!', str(ex.exception))

    def test_hire_worker__add_workers_name_to_workers_list(self):
        self.plantation.workers = ['worker1']
        result = self.plantation.hire_worker('worker2')
        expected = 'worker2 successfully hired.'
        self.assertEqual(expected, result)

    def test_len__with_plants_in_plants_dict(self):
        count_of_plants = 2
        worker = 'worker1'
        self.plantation.plants = {'worker1': ['pl1', 'pl1']}
        self.assertEqual(count_of_plants, len(self.plantation.plants[worker]))

    def test_len__with_no_plants_in_plants_dict(self):
        count_of_plants = 0
        worker = 'worker1'
        self.plantation.hire_worker(worker)

        self.assertEqual(count_of_plants, len(self.plantation.plants))

    def test_planting__if_worker_is_not_hired_expect_to_raise(self):
        self.plantation.workers = ['worker2']
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('worker1', 'plant1')
        self.assertEqual('Worker with name worker1 is not hired!', str(ex.exception))

    def test_planting_when_plantation_is_full_expect_to_raise(self):
        self.plantation.workers = ['worker2']
        self.plantation.plants = {'worker2': 'plant2'}
        worker = 'worker1'
        plant = 'plant1'
        self.plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(worker, plant)
        self.assertEqual('The plantation is full!', str(ex.exception))

    def test_planting_add_plant_worker_if_worker_hired(self):
        self.plantation.workers = ['worker2']
        self.plantation.plants = {'worker2': []}
        plant = 'plant2'
        worker = 'worker2'
        result = self.plantation.planting(worker, plant)
        expected = f'worker2 planted {plant}.'
        self.assertEqual(expected, result)

    def test_planting_add_plant_to_worker(self):
        plant = 'plant2'
        worker = 'worker2'
        self.plantation.hire_worker(worker)

        result = self.plantation.planting(worker, plant)
        expected = f"{worker} planted it's first {plant}."
        self.assertEqual(expected, result)
        self.assertEqual({worker: [plant]}, self.plantation.plants)

    def test_str__info_without_workers_added(self):
        expected = f"""Plantation size: {self.plantation.size}
"""
        result = str(self.plantation)
        self.assertEqual(expected, result)

    def test_str__info_without_plants_added(self):
        self.plantation.size = 1
        worker = 'worker1'
        self.plantation.hire_worker(worker)
        result = str(self.plantation)
        expected = f"Plantation size: {self.plantation.size}\nworker1"
        self.assertEqual(expected, result)

    def test_str__info_with_plants_and_workers_added(self):
        self.plantation.size = 1
        worker = 'worker1'
        self.plantation.hire_worker(worker)
        plant = 'plant1'
        self.plantation.planting(worker, plant)
        result = str(self.plantation)
        expected = f"Plantation size: {self.plantation.size}\n{worker}\n{worker} planted: {plant}"

        self.assertEqual(expected, result)

    def test_repr_with_no_workers(self):
        self.plantation.size = 1
        result = repr(self.plantation)
        expected = f"Size: {self.plantation.size}\nWorkers: "
        self.assertEqual(expected, result)

    def test_repr_with_workers(self):
        self.plantation.size = 1
        worker = 'worker1'
        self.plantation.hire_worker(worker)
        self.assertEqual([worker], self.plantation.workers)
        result = repr(self.plantation)
        expected = f"Size: {self.plantation.size}\nWorkers: {worker}"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
