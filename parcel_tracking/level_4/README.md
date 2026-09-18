# Level 4 — Undo

Keep Levels 1–3. Add undo of the **last successful mutating** call.

## New method

### `undo() -> bool`

Revert the most recent **successful** mutation. Return `True` if something was undone, `False` if there is nothing to undo.

Mutations (push these on a history stack only when they succeed):

| Call | Undo |
| --- | --- |
| `register_parcel` → `True` | Forget the parcel entirely (events, assignment) |
| `add_event` → `True` | Pop that parcel’s last event |
| `assign_courier` → `True` | Restore the previous courier (`None` if it was unassigned). The parcel must move back on courier lists. |
| `add_courier_event` → `True` | Pop that courier’s last event |

Do **not** record failed calls (`False` from register/add_event/assign) or any `get_*` / `get_top_parcels`.

If undoing a register removes a parcel that was assigned, it also leaves that courier’s parcel list. Courier event logs are only removed if you later undo the operations that created them; after a parcel is unregistered by undo, `get_courier` / `get_events` for that id behave as unknown.

## Example

```python
sys = ParcelTrackingSystem()
sys.register_parcel("p1")
sys.add_event("p1", "A")
sys.add_event("p1", "B")
sys.undo()                       # True, pops "B"
sys.get_events("p1")             # ["A"]
sys.undo()                       # True, pops "A"
sys.undo()                       # True, unregisters p1
sys.get_event_count("p1")        # -1
sys.undo()                       # False

sys.register_parcel("p1")
sys.assign_courier("p1", "ann")
sys.assign_courier("p1", "bob")
sys.undo()                       # back to ann
sys.get_courier("p1")            # "ann"
sys.get_courier_parcels("bob")   # []
sys.get_courier_parcels("ann")   # ["p1"]
```

## Run tests

```bash
python3 -m unittest test_level_4.py -v
```
