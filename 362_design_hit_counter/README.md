# 362. Design Hit Counter

Medium. Design a counter for hits in a 300-second window.

Source: [AlgoMonster walkthrough](https://algo.monster/liteproblems/362)

## Problem

Track hits and answer how many arrived in the past 5 minutes (300 seconds).

Timestamps are in seconds. Calls arrive in chronological order (timestamps are non-decreasing). Several hits may share the same timestamp.

### `HitCounter()`

Create an empty counter.

### `hit(timestamp: int) -> None`

Record one hit at `timestamp`.

### `getHits(timestamp: int) -> int`

Return how many recorded hits fall in `[timestamp - 299, timestamp]`.

That range is 300 seconds, inclusive on both ends. At time `300`, a hit at `1` still counts. At time `301`, it does not.

## Examples

LeetCode example:

```python
counter = HitCounter()
counter.hit(1)
counter.hit(2)
counter.hit(3)
counter.getHits(4)     # 3
counter.hit(300)
counter.getHits(300)   # 4
counter.getHits(301)   # 3  (the hit at t=1 has left the window)
```

Window edge:

```python
counter = HitCounter()
counter.hit(1)
counter.getHits(300)   # 1  window is [1, 300]
counter.getHits(301)   # 0  window is [2, 301]
```

Same second:

```python
counter = HitCounter()
counter.hit(5)
counter.hit(5)
counter.hit(5)
counter.getHits(5)     # 3
```

## Run tests

From this directory:

```bash
python3 -m unittest test_hit_counter.py -v
```
