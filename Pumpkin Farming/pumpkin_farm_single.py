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
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()

		if get_ground_type() != Grounds.Soil:
			till()

		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
			use_item(Items.Water

	def pumpkin_ready():
		return get_entity_type() == Entities.Pumpkin and can_harvest()

	def plant_field(world_size):
		failed_pumpkins = []

		x = 0
		while x < world_size:
			y = 0
			while y < world_size:
				go_to(world_size, x, y)
				prepare_pumpkin_tile()
				failed_pumpkins.append((x, y))
				y += 1
			x += 1

		return failed_pumpkins

	def retry_failed_pumpkins(world_size, failed_pumpkins):
		still_failed = []

		for x, y in failed_pumpkins:
			go_to(world_size, x, y)

			if pumpkin_ready():
				continue

			prepare_pumpkin_tile()
			still_failed.append((x, y))

		return still_failed

	clear()

	ws = get_world_size()

	while True:
		failed_pumpkins = plant_field(ws)

		while len(failed_pumpkins) > 0:
			failed_pumpkins = retry_failed_pumpkins(ws, failed_pumpkins)

		harvest()


farm_pumpkins()
