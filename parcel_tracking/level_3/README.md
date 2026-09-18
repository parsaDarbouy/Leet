# Level 3 — Couriers

Keep Level 1 and Level 2. Add courier assignment and courier-only events.

A parcel starts **unassigned**. Assignment may be changed. Courier events are a separate list from parcel events.

## New methods

### `assign_courier(parcel_id: str, courier_id: str) -> bool`

- Set the parcel’s current courier (overwrite if it already had one).
- Return `True` on success.
- Return `False` if the parcel is unknown.

### `get_courier(parcel_id: str) -> str | None`

- Current courier id.
- `None` if the parcel is unknown **or** registered but unassigned.

### `get_courier_parcels(courier_id: str) -> list[str]`

- Parcel ids **currently** assigned to that courier.
- Sorted lexicographically.
- `[]` if the courier has no current parcels (including unknown courier).

Reassignment moves the parcel: it must leave the previous courier’s list.

### `add_courier_event(courier_id: str, event: str) -> bool`

- Append a courier-level event (does not require any parcels).
- Always succeeds and returns `True` (creates the courier’s event log if needed).

### `get_courier_event_count(courier_id: str) -> int`

- Number of courier events.
- `0` if that courier exists only because of assignment or an empty log created by `add_courier_event`.
- `-1` if this `courier_id` has never been used in `assign_courier` **and** never received `add_courier_event`.

## Example

```python
sys = ParcelTrackingSystem()
sys.register_parcel("p1")
sys.register_parcel("p2")
sys.assign_courier("p1", "ann")     # True
sys.assign_courier("p2", "ann")     # True
sys.get_courier("p1")               # "ann"
sys.get_courier_parcels("ann")      # ["p1", "p2"]

sys.assign_courier("p2", "bob")     # True  (moved)
sys.get_courier_parcels("ann")      # ["p1"]
sys.get_courier_parcels("bob")      # ["p2"]

sys.add_courier_event("ann", "SHIFT_START")
sys.get_courier_event_count("ann")  # 1
sys.get_courier_event_count("zoe")  # -1

sys.assign_courier("missing", "ann")  # False
```

## Run tests

```bash
python3 -m unittest test_level_3.py -v
```
