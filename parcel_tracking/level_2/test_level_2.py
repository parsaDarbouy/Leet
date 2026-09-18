import unittest

from solution import ParcelTrackingSystem


class TestLevel2(unittest.TestCase):
    def setUp(self):
        self.sys = ParcelTrackingSystem()

    def test_level1_still_works(self):
        self.assertTrue(self.sys.register_parcel("p"))
        self.assertTrue(self.sys.add_event("p", "SCAN"))
        self.assertEqual(self.sys.get_event_count("p"), 1)
        self.assertEqual(self.sys.get_events("p"), ["SCAN"])

    def test_empty_system(self):
        self.assertEqual(self.sys.get_top_parcels(3), [])

    def test_k_non_positive(self):
        self.sys.register_parcel("a")
        self.assertEqual(self.sys.get_top_parcels(0), [])
        self.assertEqual(self.sys.get_top_parcels(-1), [])

    def test_rank_by_count_then_id(self):
        self.sys.register_parcel("b")
        self.sys.register_parcel("a")
        self.sys.register_parcel("c")
        self.sys.add_event("b", "SCAN")
        self.sys.add_event("b", "SCAN")
        self.sys.add_event("c", "SCAN")
        self.assertEqual(self.sys.get_top_parcels(2), ["b", "c"])
        self.assertEqual(self.sys.get_top_parcels(10), ["b", "c", "a"])

    def test_zero_event_parcels_included(self):
        self.sys.register_parcel("z")
        self.sys.register_parcel("m")
        self.assertEqual(self.sys.get_top_parcels(2), ["m", "z"])

    def test_tie_break_lexicographic(self):
        for pid in ("b", "a", "c"):
            self.sys.register_parcel(pid)
            self.sys.add_event(pid, "X")
        self.assertEqual(self.sys.get_top_parcels(3), ["a", "b", "c"])

    def test_ranking_updates_after_new_events(self):
        self.sys.register_parcel("b")
        self.sys.register_parcel("a")
        self.sys.register_parcel("c")
        self.sys.add_event("b", "SCAN")
        self.sys.add_event("b", "SCAN")
        self.sys.add_event("c", "SCAN")
        self.sys.add_event("a", "SCAN")
        self.assertEqual(self.sys.get_top_parcels(3), ["b", "a", "c"])


if __name__ == "__main__":
    unittest.main()
