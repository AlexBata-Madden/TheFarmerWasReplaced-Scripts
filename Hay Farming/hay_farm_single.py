def farm_hay():

	def hay_worker():
		while True:
			if can_harvest():
				harvest()
			move(North)

	clear()
	hay_worker()

farm_hay()
