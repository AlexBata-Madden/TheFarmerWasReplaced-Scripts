def farm_carrots():

	def go_to(world_size, x, y):
		while get_pos_x() != x:
			current = get_pos_x()
			east_distance = (x - current) % world_size
			west_distance = (current - x) % world_size

			if east_distance <= west_distance:
				move(East)
			else:
				move(West)

		while get_pos_y() != y:
			current = get_pos_y()
			north_distance = (y - current) % world_size
			south_distance = (current - y) % world_size

			if north_distance <= south_distance:
				move(North)
			else:
				move(South)

	def prepare_ground(plant_type):
		if plant_type == Entities.Carrot:
			if get_ground_type() == Grounds.Grassland:
				till()
		else:
			if get_ground_type() == Grounds.Soil:
				till()

	def make_companion_task(world_size, plant_type, x, y):
		def task():
			go_to(world_size, x, y)

			if get_entity_type() == plant_type:
				return

			harvest()
			prepare_ground(plant_type)
			plant(plant_type)

		return task

	def maintain_tile():
		if can_harvest():
			use_item(Items.Water)
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			if num_items(Items.Fertilizer) > 100:
				use_item(Items.Fertilizer)
				use_item(Items.Weird_Substance)

	def send_drone(world_size):
		home_x = get_pos_x()
		home_y = get_pos_y()

		while True:
			plant_type, (x, y) = get_companion()

			task = make_companion_task(world_size, plant_type, x, y)
			drone = spawn_drone(task)

			if drone:
				wait_for(drone)
			else:
				task()
				go_to(world_size, home_x, home_y)

			maintain_tile()

	def make_worker_task(world_size, x, y):
		def task():
			go_to(world_size, x, y)
			send_drone(world_size)
		return task
		
	clear()

	ws = get_world_size()
	
	start = 3
	step = 7

	go_to(ws, start, start)

	x = start
	while x < ws:
		y = start
		while y < ws:
			if x != start or y != start:
				spawn_drone(make_worker_task(ws, x, y))
			y += step
		x += step
	
	send_drone(ws)


farm_carrots()
