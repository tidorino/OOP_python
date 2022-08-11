from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_init__wrong_name_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = 'team123'
        self.assertEqual('Team Name can contain only letters!', str(ex.exception))

    def test_init_correct(self):
        self.assertEqual('Team', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_add_members__if_not_add_in_members_dict(self):
        self.team.members = {'mem1': 12, 'mem2': 13}
        membs = {'mem3': 12, 'mem4': 13}
        result = self.team.add_member(**membs)
        expected = {'mem1': 12, 'mem2': 13, 'mem3': 12, 'mem4': 13}

        self.assertEqual('Successfully added: mem3, mem4', result)
        self.assertEqual(expected, self.team.members)

    def test_remove_member_if_exist_delete_it_from_dict(self):
        self.team.members = {'mem1': 12, 'mem2': 13}
        result = self.team.remove_member('mem1')
        expected = 'Member mem1 removed'
        self.assertEqual(expected, result)
        self.assertEqual({'mem2': 13}, self.team.members)

    def test_remove_member_if_not_exist_in_dict(self):
        self.team.members = {'mem1': 12, 'mem2': 13}
        result = self.team.remove_member('mem3')
        expected = 'Member with name mem3 does not exist'
        self.assertEqual(expected, result)
        self.assertEqual({'mem1': 12, 'mem2': 13}, self.team.members)

    def test_gt__if_team_members_are_more_than_other_team_members(self):
        self.team.members = {'mem1': 12, 'mem2': 13}
        team = Team('Other')
        team.members = {'mem3': 12}
        self.assertEqual(True, self.team > team)
        self.assertEqual(False, self.team < team)

    def test_len__return_numb_members(self):
        self.team.members['mem1'] = 12
        self.team.members['mem2'] = 13
        self.assertEqual(2, len(self.team))

    def test_add__new_team(self):
        self.team.members['mem1'] = 12
        self.team.members['mem2'] = 13

        other_team = Team('Other')
        other_team.members['mem3'] = 11

        result = self.team + other_team
        self.assertEqual('TeamOther', result.name)
        expected = {
            'mem1': 12,
            'mem2': 13,
            'mem3': 11
        }
        self.assertEqual(expected, result.members)

    def test_str__returns_members_sorted_by_descending_order_by_age(self):
        self.team.members = {'mem1': 12, 'mem2': 13, 'mem3': 11}
        result = str(self.team)
        expected = 'Team name: Team\n' \
                   'Member: mem2 - 13-years old\n' \
                   'Member: mem1 - 12-years old\n' \
                   'Member: mem3 - 11-years old'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
