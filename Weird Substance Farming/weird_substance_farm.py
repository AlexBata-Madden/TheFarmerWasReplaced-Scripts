def farm_weird_substance():

	def weird_substance_worker():
		while True:
			if can_harvest():
				harvest()
			use_item(Items.Weird_Substance)
			move(North)

	clear()

	for _ in range(max_drones() - 1):
		if spawn_drone(weird_substance_worker):
			move(East)

	weird_substance_worker()

farm_weird_substance()
