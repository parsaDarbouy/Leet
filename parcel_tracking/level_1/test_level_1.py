import unittest

from solution import ParcelTrackingSystem


class TestLevel1(unittest.TestCase):
    def setUp(self):
        self.sys = ParcelTrackingSystem()

    def test_register_new_parcel(self):
        self.assertTrue(self.sys.register_parcel("pkg-1"))

    def test_register_duplicate_returns_false(self):
        self.sys.register_parcel("pkg-1")
        self.assertFalse(self.sys.register_parcel("pkg-1"))

    def test_unknown_parcel_count_and_events(self):
        self.assertEqual(self.sys.get_event_count("missing"), -1)
        self.assertIsNone(self.sys.get_events("missing"))

    def test_registered_parcel_starts_empty(self):
        self.sys.register_parcel("pkg-1")
        self.assertEqual(self.sys.get_event_count("pkg-1"), 0)
        self.assertEqual(self.sys.get_events("pkg-1"), [])

    def test_add_event_pushes_in_order(self):
        self.sys.register_parcel("pkg-1")
        self.assertTrue(self.sys.add_event("pkg-1", "PICKED_UP"))
        self.assertTrue(self.sys.add_event("pkg-1", "IN_TRANSIT"))
        self.assertTrue(self.sys.add_event("pkg-1", "DELIVERED"))
        self.assertEqual(self.sys.get_event_count("pkg-1"), 3)
        self.assertEqual(
            self.sys.get_events("pkg-1"),
            ["PICKED_UP", "IN_TRANSIT", "DELIVERED"],
        )

    def test_add_event_unknown_parcel(self):
        self.assertFalse(self.sys.add_event("pkg-2", "DELIVERED"))
        self.assertEqual(self.sys.get_event_count("pkg-2"), -1)

    def test_duplicate_register_does_not_clear_events(self):
        self.sys.register_parcel("pkg-1")
        self.sys.add_event("pkg-1", "PICKED_UP")
        self.sys.register_parcel("pkg-1")
        self.assertEqual(self.sys.get_events("pkg-1"), ["PICKED_UP"])

    def test_multiple_parcels_are_independent(self):
        self.sys.register_parcel("a")
        self.sys.register_parcel("b")
        self.sys.add_event("a", "X")
        self.sys.add_event("a", "Y")
        self.sys.add_event("b", "Z")
        self.assertEqual(self.sys.get_event_count("a"), 2)
        self.assertEqual(self.sys.get_event_count("b"), 1)
        self.assertEqual(self.sys.get_events("a"), ["X", "Y"])
        self.assertEqual(self.sys.get_events("b"), ["Z"])

    def test_get_events_returns_a_copy(self):
        self.sys.register_parcel("pkg-1")
        self.sys.add_event("pkg-1", "A")
        events = self.sys.get_events("pkg-1")
        events.append("MUTATED")
        self.assertEqual(self.sys.get_events("pkg-1"), ["A"])


if __name__ == "__main__":
    unittest.main()
