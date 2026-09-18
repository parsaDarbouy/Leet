# Level 2 — Rank parcels

Keep every Level 1 method. Add ranking.

## New method

### `get_top_parcels(k: int) -> list[str]`

Return up to `k` registered parcel ids, ordered by:

1. **Higher event count first**
2. If counts are equal, **lexicographically smaller** `parcel_id` first

Rules:

- `k <= 0` → `[]`
- If there are fewer than `k` parcels, return all of them (still sorted)
- Parcels with **0 events** still participate
- Unknown / unregistered ids never appear

## Example

```python
sys = ParcelTrackingSystem()
sys.register_parcel("b")
sys.register_parcel("a")
sys.register_parcel("c")
sys.add_event("b", "SCAN")
sys.add_event("b", "SCAN")
sys.add_event("c", "SCAN")
# counts: a=0, b=2, c=1

sys.get_top_parcels(2)   # ["b", "c"]
sys.get_top_parcels(10)  # ["b", "c", "a"]
sys.get_top_parcels(0)   # []

sys.add_event("a", "SCAN")
# counts: a=1, b=2, c=1  → tie a vs c, "a" < "c"
sys.get_top_parcels(3)   # ["b", "a", "c"]
```

## Run tests

```bash
python3 -m unittest test_level_2.py -v
```
