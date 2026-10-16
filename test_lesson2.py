import unittest

from lesson2 import element_types, insert_rating, numbered_words, season_for_month, swap_neighbors


class Lesson2Tests(unittest.TestCase):
    def test_types(self):
        self.assertEqual(element_types([1, None, "a", True]), ["int", "NoneType", "str", "bool"])

    def test_swap(self):
        self.assertEqual(swap_neighbors([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])
        self.assertEqual(swap_neighbors([]), [])

    def test_seasons(self):
        self.assertEqual(season_for_month(12), "winter")
        self.assertEqual(season_for_month(4), "spring")
        self.assertEqual(season_for_month(8), "summer")
        self.assertEqual(season_for_month(10), "autumn")
        with self.assertRaises(ValueError):
            season_for_month(13)

    def test_words(self):
        self.assertEqual(numbered_words("   one    exceptionallylong  "), ["1. one", "2. exceptiona"])
        self.assertEqual(numbered_words(""), [])

    def test_rating(self):
        original = [7, 5, 3, 3, 2]
        self.assertEqual(insert_rating(original, 3), [7, 5, 3, 3, 3, 2])
        self.assertEqual(insert_rating(original, 8), [8, 7, 5, 3, 3, 2])
        self.assertEqual(insert_rating(original, 1), [7, 5, 3, 3, 2, 1])
        self.assertEqual(original, [7, 5, 3, 3, 2])
        with self.assertRaises(ValueError):
            insert_rating(original, 0)


if __name__ == "__main__":
    unittest.main()
