def farm_bones():
	clear()
	ws = get_world_size()
	change_hat(Hats.Dinosaur_Hat)
	
	def loop():
		move(North)
		
		def move_up():
			for i in range(ws-2):
				move(North)
				
			move(East)
			
		def move_down():
			for i in range(ws-2):
				move(South)
				
			move(East)
			
		for i in range(ws):
			move_up()
			move_down()
		
		for i in range(ws):
			move(West)
	
	for i in range(ws*ws):
		loop()
	change_hat(Hats.Brown_Hat)
	

farm_bones()