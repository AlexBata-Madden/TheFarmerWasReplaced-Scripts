def farm_bones():
	clear()
	ws = get_world_size()
	change_hat(Hats.Dinosaur_Hat)
	
	def move_up(world_size):
		for i in range(world_size - 2):
			move(North)

		move(East)

	def move_down(world_size):
		for i in range(world_size - 2):
			move(South)

		move(East)

	def loop(world_size):
		move(North)

		for i in range(world_size):
			move_up(world_size)
			move_down(world_size)

		for i in range(world_size):
			move(West)
	
	for i in range(ws*ws):
		loop(ws)
	change_hat(Hats.Brown_Hat)
	

farm_bones()
