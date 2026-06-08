# Pumpkin Farming

## Prerequisites

- 32x32 World Unlocked
- 32 Drones Unlocked
- Enough Power
- Enough Carrots

## Implementation

The idea is to spawn drones across the field, plant pumpkins, replace dead pumpkins with new ones, and then harvest once the pumpkins have combined into a giant pumpkin. The main drone also checks whether the field is ready by using `measure()` on two corners. If the ids at `(0, 0)` and `(world_size - 1, world_size - 1)` are the same, the field is one giant pumpkin and can be harvested.

## Scripts

- `pumpkin_farm.py`: Multi-drone pumpkin farming.
- `pumpkin_farm_single.py`: Single-drone pumpkin farming.

## Achievements

![pumpkins_unlock](./img/pumpkins_unlock.png)

## Leaderboards

### Pumpkin

Note: Using `pumpkin_farm.py`. To make the code leaderboard applicable, change the `while True` in the drone functions to `while < 200000000`.

![pumpkins_leaderboard](./img/pumpkins_leaderboard.png)

### Pumpkins_Single

Note: Using `pumpkin_farm_single.py`. To make the code leaderboard applicable, change the `while True` in the drone functions to `while < 10000000`.

![pumpkins_single_leaderboard](./img/pumpkins_single_leaderboard.png)
