import unittest

from solution import HitCounter


class TestHitCounter(unittest.TestCase):
    def test_leetcode_example(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        self.assertEqual(counter.getHits(301), 3)

    def test_no_hits(self):
        counter = HitCounter()
        self.assertEqual(counter.getHits(1), 0)

    def test_multiple_hits_same_timestamp(self):
        counter = HitCounter()
        counter.hit(5)
        counter.hit(5)
        counter.hit(5)
        self.assertEqual(counter.getHits(5), 3)
        self.assertEqual(counter.getHits(304), 3)
        self.assertEqual(counter.getHits(305), 0)

    def test_inclusive_window_edge(self):
        counter = HitCounter()
        counter.hit(1)
        self.assertEqual(counter.getHits(300), 1)
        self.assertEqual(counter.getHits(301), 0)

    def test_sliding_window(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        counter.hit(301)
        self.assertEqual(counter.getHits(301), 4)
        counter.hit(302)
        self.assertEqual(counter.getHits(302), 4)

    def test_all_hits_expired(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(303), 0)

    def test_query_between_hits(self):
        counter = HitCounter()
        counter.hit(10)
        self.assertEqual(counter.getHits(15), 1)
        counter.hit(20)
        self.assertEqual(counter.getHits(319), 1)
        self.assertEqual(counter.getHits(320), 0)


if __name__ == "__main__":
    unittest.main()
