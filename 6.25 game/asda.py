for k in range(0, self.map_max * self.tile_size + 1, self.tile_size):  # 세로선
	x, y = self.Map_c.moveposGet()
	pygame.draw.line(self.screen, (255, 255, 255), start_pos=(k, y), end_pos=(x + self.map_max * self.tile_size, k + y))