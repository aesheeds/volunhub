import unittest
from unittest.mock import patch
from parser import State


class TestState(unittest.TestCase):

    @patch('builtins.input', side_effect=[
                            "bachelor",
                            "CS",
                            "C++",
                            "None",
                            "Anywhere",
                            3
                        ])
    def test_create_account_sets_data_correctly(self, mock_input):
        state = State()
        state.create_account()

        self.assertEqual(state.data["degree"], "bachelor")
        self.assertEqual(state.data["major"], "CS")
        self.assertEqual(state.data["skills"], "C++")
        self.assertEqual(state.data["experience"], "None")
        self.assertEqual(state.data["location"], "Anywhere")
        self.assertEqual(state.data["job_type"], 3)
