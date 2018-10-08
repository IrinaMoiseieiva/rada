from unittest import TestCase
from unittest.mock import MagicMock

from rada_package_moiseieiva.rada_models import Deputat


class TestDeputat(TestCase):

    def test_init(self):

            with self.assertRaises(TypeError) as e:

                dep = Deputat()

            self.assertEqual(e.exception.args[0],

                            "__init__() missing 5 required positional arguments: 'weight', 'height', 'last_name', 'first_name', and 'age'")

            dep = Deputat(60, 180, 'Vaskiv', 'Taras', 28)

            self.assertEqual(dep.age, 28)

            self.assertEqual(dep.first_name, 'Taras')

            self.assertEqual(dep.last_name, 'Vaskiv')

            self.assertEqual(dep.weight, 60)

            self.assertEqual(dep.height, 180)

            self.assertNotEqual(dep.height, 185)

