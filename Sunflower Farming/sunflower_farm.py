def farm_sunflower():	

	def sunflower_worker():
		while True:
			for _ in range(get_world_size()):
				if get_water() < 0.6:
					use_item(Items.Water)
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
				move(North)
	
	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(sunflower_worker):
			move(East)
	
	sunflower_worker()
	
farm_sunflower()
	
	