import unittest
from set_covering import set_covering


class SetCoveringTest(unittest.TestCase):
    def test_case_one(self):
        states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
        stations = {}
        stations['kone'] = set(["id", "nv", "ut"])
        stations['ktwo'] = set(["wa", "id", "mt"])
        stations['kthree'] = set(["or", "nv", "ca"])
        stations['kfour'] = set(["nv", "ut"])
        stations['kfive'] = set(["ca", "az"])

        print(set_covering(states_needed, stations))


if __name__ == '__main__':
    unittest.main()
