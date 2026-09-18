import unittest

from solution import ParcelTrackingSystem


class TestLevel4(unittest.TestCase):
    def setUp(self):
        self.sys = ParcelTrackingSystem()

    def test_undo_empty(self):
        self.assertFalse(self.sys.undo())

    def test_failed_ops_are_not_undone(self):
        self.assertFalse(self.sys.add_event("p1", "A"))
        self.assertFalse(self.sys.assign_courier("p1", "ann"))
        self.assertTrue(self.sys.register_parcel("p1"))
        self.assertFalse(self.sys.register_parcel("p1"))
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_event_count("p1"), -1)
        self.assertFalse(self.sys.undo())

    def test_undo_add_event(self):
        self.sys.register_parcel("p1")
        self.sys.add_event("p1", "A")
        self.sys.add_event("p1", "B")
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_events("p1"), ["A"])
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_events("p1"), [])

    def test_undo_register_removes_parcel(self):
        self.sys.register_parcel("p1")
        self.sys.add_event("p1", "A")
        self.sys.undo()
        self.sys.undo()
        self.assertEqual(self.sys.get_event_count("p1"), -1)
        self.assertIsNone(self.sys.get_events("p1"))
        self.assertNotIn("p1", self.sys.get_top_parcels(5))

    def test_undo_assign_restores_previous(self):
        self.sys.register_parcel("p1")
        self.sys.assign_courier("p1", "ann")
        self.sys.assign_courier("p1", "bob")
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_courier("p1"), "ann")
        self.assertEqual(self.sys.get_courier_parcels("ann"), ["p1"])
        self.assertEqual(self.sys.get_courier_parcels("bob"), [])
        self.assertTrue(self.sys.undo())
        self.assertIsNone(self.sys.get_courier("p1"))
        self.assertEqual(self.sys.get_courier_parcels("ann"), [])

    def test_undo_register_clears_assignment(self):
        self.sys.register_parcel("p1")
        self.sys.assign_courier("p1", "ann")
        self.sys.undo()  # unassign
        self.sys.undo()  # unregister
        self.assertEqual(self.sys.get_courier_parcels("ann"), [])
        self.assertIsNone(self.sys.get_courier("p1"))

    def test_undo_courier_event(self):
        self.sys.add_courier_event("ann", "SHIFT_START")
        self.sys.add_courier_event("ann", "BREAK")
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_courier_event_count("ann"), 1)
        self.assertTrue(self.sys.undo())
        self.assertEqual(self.sys.get_courier_event_count("ann"), -1)

    def test_ranking_after_undo_event(self):
        self.sys.register_parcel("a")
        self.sys.register_parcel("b")
        self.sys.add_event("b", "X")
        self.sys.add_event("b", "Y")
        self.assertEqual(self.sys.get_top_parcels(2), ["b", "a"])
        self.sys.undo()
        self.sys.undo()
        self.assertEqual(self.sys.get_top_parcels(2), ["a", "b"])


if __name__ == "__main__":
    unittest.main()
