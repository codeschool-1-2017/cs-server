import pytest
from codeschool.sparta.models import organize_groups 

class TestGroups:
    def test_organize_groups_example(self):
        users = {'john': 10, 'paul': 9, 'george': 8, 'ringo': 6}
        assert organize_groups(users, 2) == [['john', 'ringo'], ['paul', 'george']] 