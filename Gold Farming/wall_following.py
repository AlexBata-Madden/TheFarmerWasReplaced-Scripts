def generate_full_map_maze():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))
	
def farm_gold():
	directions = [West, North, East, South]
	
	clear()
	generate_full_map_maze()

	while True:
		heading = 0
		
		while get_entity_type() != Entities.Treasure:
			
			heading = (heading - 1) % 4
			
			while not move(directions[heading]):
				heading = (heading + 1) % 4
			
		harvest()
		generate_full_map_maze()

farm_gold()