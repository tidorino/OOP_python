from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    USERNAME = 'Hero'
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_hero_initialization(self):

        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_battle_check_enemy_hero_username_if_equal_to_hero_username_expect_to_raise(self):

        enemy = Hero(self.USERNAME, 5, 20, 30)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__when_hero_health_is_negative_expect_to_raise(self):
        enemy = Hero('Alex', 5, 20, 30)
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__when_enemy_health_is_equal_to_zero_expect_to_raise(self):
        enemy_username = 'Enemy'
        enemy = Hero(enemy_username, 3, 0, 30)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(ex.exception))

    def test_battle__zero_or_negative_health_for_hero_and_enemy_return_draw(self):
        enemy = Hero('Alex', self.LEVEL, self.HEALTH, self.DAMAGE)

        actual_result = self.hero.battle(enemy)
        expected_health = self.HEALTH - (self.LEVEL * self.DAMAGE)

        self.assertEqual('Draw', actual_result)

        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle__return_win_message_when_enemy_health_is_equal_to_zero_or_negative(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10

        enemy = Hero('Alex', enemy_level, enemy_health, enemy_damage)

        result = self.hero.battle(enemy)
        enemy_expected_health = enemy_health - (self.LEVEL * self.DAMAGE)
        hero_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        hero_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        hero_expected_health = self.HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual('You win', result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(hero_expected_level, self.hero.level)
        self.assertEqual(hero_expected_damage, self.hero.damage)

        self.assertEqual(hero_expected_health, self.hero.health)

    def test_battle__return_lose_message_when_hero_health_is_equal_to_zero_or_negative(self):
        hero_level, hero_health, hero_damage = 5, 100, 10
        hero = Hero('Hero', hero_level, hero_health, hero_damage)

        enemy = Hero('Enemy', self.LEVEL, self.HEALTH, self.DAMAGE)

        result = hero.battle(enemy)
        hero_expected_health = hero_health - (self.LEVEL * self.DAMAGE)
        enemy_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.HEALTH - (hero_level * hero_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual('You lose', result)
        self.assertEqual(hero_expected_health, hero.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_info__returns_proper_string(self):

        # result = self.hero.__str__()
        result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
            f"Health: {self.HEALTH}\n" \
            f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
