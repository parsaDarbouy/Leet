import unittest

from solution import ParcelTrackingSystem


class TestLevel3(unittest.TestCase):
    def setUp(self):
        self.sys = ParcelTrackingSystem()

    def test_unassigned_registered_parcel(self):
        self.sys.register_parcel("p1")
        self.assertIsNone(self.sys.get_courier("p1"))
        self.assertEqual(self.sys.get_courier_parcels("ann"), [])

    def test_unknown_parcel_courier(self):
        self.assertIsNone(self.sys.get_courier("missing"))
        self.assertFalse(self.sys.assign_courier("missing", "ann"))

    def test_assign_and_list_sorted(self):
        self.sys.register_parcel("p2")
        self.sys.register_parcel("p1")
        self.assertTrue(self.sys.assign_courier("p2", "ann"))
        self.assertTrue(self.sys.assign_courier("p1", "ann"))
        self.assertEqual(self.sys.get_courier("p1"), "ann")
        self.assertEqual(self.sys.get_courier_parcels("ann"), ["p1", "p2"])

    def test_reassign_moves_parcel(self):
        self.sys.register_parcel("p1")
        self.sys.register_parcel("p2")
        self.sys.assign_courier("p1", "ann")
        self.sys.assign_courier("p2", "ann")
        self.sys.assign_courier("p2", "bob")
        self.assertEqual(self.sys.get_courier("p2"), "bob")
        self.assertEqual(self.sys.get_courier_parcels("ann"), ["p1"])
        self.assertEqual(self.sys.get_courier_parcels("bob"), ["p2"])

    def test_reassign_same_courier_is_idempotent(self):
        self.sys.register_parcel("p1")
        self.sys.assign_courier("p1", "ann")
        self.assertTrue(self.sys.assign_courier("p1", "ann"))
        self.assertEqual(self.sys.get_courier_parcels("ann"), ["p1"])

    def test_courier_events_independent_of_parcels(self):
        self.assertTrue(self.sys.add_courier_event("ann", "SHIFT_START"))
        self.assertEqual(self.sys.get_courier_event_count("ann"), 1)
        self.assertEqual(self.sys.get_courier_parcels("ann"), [])
        self.assertEqual(self.sys.get_courier_event_count("zoe"), -1)

    def test_assignment_creates_courier_with_zero_events(self):
        self.sys.register_parcel("p1")
        self.sys.assign_courier("p1", "ann")
        self.assertEqual(self.sys.get_courier_event_count("ann"), 0)

    def test_ranking_unchanged_by_assignment(self):
        self.sys.register_parcel("b")
        self.sys.register_parcel("a")
        self.sys.add_event("b", "X")
        self.sys.assign_courier("a", "ann")
        self.assertEqual(self.sys.get_top_parcels(2), ["b", "a"])


if __name__ == "__main__":
    unittest.main()
