def farm_wierd_substance():	

	def wierd_substance_worker():
		while True:
			if can_harvest():
				harvest()
			use_item(Items.Weird_Substance)
			move(North)
	
	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(wierd_substance_worker):
			move(East)
	
	wierd_substance_worker()
	
farm_wierd_substance()
	
	