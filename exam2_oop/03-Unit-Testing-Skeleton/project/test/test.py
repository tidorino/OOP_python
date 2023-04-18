from unittest import TestCase

from project.robot import Robot


class RobotTest(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('r', 'Military', 20, 30.00)

    def test_init__if_valid_category(self):
        allowed_category = ['Military', 'Education', 'Entertainment', 'Humanoids']
        with self.assertRaises(ValueError) as ex:
            self.robot.category = 'None'
        self.assertEqual(f"Category should be one of '{allowed_category}'", str(ex.exception))

    def test_init__correct(self):
        self.assertEqual('r', self.robot.robot_id)
        self.assertEqual(20, self.robot.available_capacity)
        self.assertEqual(30.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

