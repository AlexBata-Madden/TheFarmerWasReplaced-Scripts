def farm_hay():

	def hay_worker():
		while True:
			if can_harvest():
				harvest()
			move(North)

	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(hay_worker):
			move(East)

	hay_worker()

farm_hay()
