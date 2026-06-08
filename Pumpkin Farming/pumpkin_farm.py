def farm_pumpkins():
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


	def prepare_pumpkin_tile():
		if get_ground_type() != Grounds.Soil:
			till()

		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
			use_item(Items.Water)


	def work_column(world_size):
		for _ in range(world_size):
			prepare_pumpkin_tile()
			move(North)


	def pumpkin_id_if_ready():
		if get_entity_type() == Entities.Pumpkin and can_harvest():
			return measure()
		return -1


	def whole_field_ready(world_size):
		go_to(world_size, 0, 0)
		id1 = pumpkin_id_if_ready()

		if id1 == -1:
			return False

		go_to(world_size, world_size - 1, world_size - 1)
		id2 = pumpkin_id_if_ready()

		return id1 == id2


	def make_pumpkin_worker(world_size):
		def task():
			while True:
				work_column(world_size)
		return task


	def harvester_drone(world_size):
		go_to(world_size, world_size - 1, 0)
 
		while True:
			work_column(world_size)

			if whole_field_ready(world_size):
				harvest()

	clear()

	ws = get_world_size()

	for _ in range(ws):
		spawn_drone(make_pumpkin_worker(ws))
		move(East)

	harvester_drone(ws)


farm_pumpkins()
