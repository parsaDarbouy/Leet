# Level 1 — Register parcels, push events, get state

Implement `ParcelTrackingSystem` in `solution.py`.

A parcel must be **registered** before you can push events onto it. Events are stored in insertion order (a list: `add_event` is a push/append).

## Methods

### `register_parcel(parcel_id: str) -> bool`

- Create a parcel with an empty event list and no courier.
- Return `True` if it was new.
- Return `False` if `parcel_id` is already registered (do not reset it).

### `add_event(parcel_id: str, event: str) -> bool`

- Append `event` to that parcel’s history.
- Return `True` on success.
- Return `False` if the parcel was never registered (do not create it).

### `get_event_count(parcel_id: str) -> int`

- Number of events on that parcel.
- Return `-1` if the parcel is unknown.

### `get_events(parcel_id: str) -> list[str] | None`

- Copy of the event list in order.
- Return `None` if the parcel is unknown.
- Return `[]` if it is registered but has no events yet.

## Example

```python
sys = ParcelTrackingSystem()
sys.register_parcel("pkg-1")          # True
sys.add_event("pkg-1", "PICKED_UP")   # True
sys.add_event("pkg-1", "IN_TRANSIT")  # True
sys.get_event_count("pkg-1")          # 2
sys.get_events("pkg-1")               # ["PICKED_UP", "IN_TRANSIT"]

sys.add_event("pkg-2", "DELIVERED")   # False  (never registered)
sys.get_event_count("pkg-2")          # -1
sys.get_events("pkg-2")               # None

sys.register_parcel("pkg-1")          # False  (already exists)
sys.get_event_count("pkg-1")          # still 2
```

## Run tests

```bash
python3 -m unittest test_level_1.py -v
```
