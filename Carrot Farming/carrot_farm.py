def farm_carrot():
	
	def carrot_worker():
		while True:
			if get_water() < 0.5:
				use_item(Items.Water)

			if(can_harvest()):
				harvest()
			if get_ground_type() != Grounds.Soil:
					till()
			plant(Entities.Carrot)
			move(North)

	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(carrot_worker):
			move(East)

	carrot_worker()
	
farm_carrot()