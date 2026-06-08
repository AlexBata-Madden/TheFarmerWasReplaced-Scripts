def farm_wood():

	def wood_worker():
		ws = get_world_size()
		
		while True:
			for _ in range(ws):
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
			move(East)

	clear()
	wood_worker()
	
farm_wood()
