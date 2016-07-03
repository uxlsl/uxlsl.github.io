from django.test import TestCase
from .models import Genre


class TGenre(TestCase):

    def test_parent(self):
        rock = Genre.objects.create(name="Rock")
        rock_child = Genre.objects.create(name="Hard Rock", parent=rock)

        self.assertEqual(rock_child.parent, rock)
        self.assertEqual(1, rock_child.get_level())
        rock_child1 = Genre.objects.create(name="siblings", parent=rock)
        self.assertIn(rock_child1, rock_child.get_siblings())
        self.assertIn(rock_child1, rock.get_children())


