# Pumpkin Farming

## Prerequisites

- 32x32 World Unlocked
- 32 Drones Unlocked
- Enough Power
- Enough Carrots

## Implementation

The idea is to spawn two drones into the first 31 rows, whose only concern is to plant pumpkins, and replace dead pumpkins with new ones. The main drone, in the final column, does this as well, but is also tasked with checking if all of the pumpkins have combined into a giant pumpkin, and if so, harvesting it. This check is done using the "measure()" call, which will return an id for the pumpkin. Checking that the ids of the pumpkins at (0,0) and (world_size, world_size) are the same guarantees that they are the same pumpkin.

## Achievements

![pumpkin_unlock](./img/pumpkin_unlock.png)

## Leaderboards

### Pumpkin

Note: To make the code leaderboard applicable, change the `while True` in the drone functions to `while < 200000000`
![pumpkin_leaderboard](./img/pumpkin_leaderboard.png)

### Pumpkins_Single

Not done
