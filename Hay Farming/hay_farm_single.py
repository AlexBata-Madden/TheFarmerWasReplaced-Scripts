def farm_hay():
	
	def hay_worker():
		while True:
			for _ in range(get_world_size()):
				x = get_pos_x()
				y = get_pos_y()
	
				if(can_harvest()):
					harvest()
				move(North)

	clear()
	hay_worker()
	
farm_hay()