def farm_wood():

	def wood_worker():
		while True:
			if get_water() < 0.5:
				use_item(Items.Water)
			x = get_pos_x()
			y = get_pos_y()

			if can_harvest():
				harvest()
			if (x + y) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)

	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(wood_worker):
			move(East)

	wood_worker()
	
farm_wood()
