def generate_full_map_maze():
	clear()
	plant(Entities.Bush)
	n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, n_substance)
	

def rotate(d):
	first = d[0]
	d.remove(first)
	d.append(first)
	return d

generate_full_map_maze() 
directions = [West, North, East, South]

while True:
	if(get_entity_type() == Entities.Treasure):
		harvest()
		generate_full_map_maze()
	if(can_move(directions[0])):
		move(directions[0])
		rotate(directions)
		rotate(directions)
		rotate(directions)
	elif(can_move(directions[1])):
		move(directions[1])
	elif(can_move(directions[2])):
		move(directions[2])
		rotate(directions)
	elif(can_move(directions[3])):
		move(directions[3])
		rotate(directions)
		rotate(directions)