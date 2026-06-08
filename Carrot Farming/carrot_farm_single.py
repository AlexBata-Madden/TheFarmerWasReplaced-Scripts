def farm_carrots():

	def carrot_worker():
		ws = get_world_size()

		while True:
			for _ in range(ws):
				if get_water() < 0.5:
					use_item(Items.Water)
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				move(North)
			move(East)

	clear()
	carrot_worker()

farm_carrots()
