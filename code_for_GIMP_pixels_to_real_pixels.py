for u in range(1, 3):
	v = 50
	x = 0
	y = 0
	z = 1
	
	for w in range(1, v + 1):
		x += 1
		y += 1
	
		if y == 3 or w == 2:
			z += 1
			y = 0
	
		if u == 1:
			print(f"{x} = {z}")
		else:
			print(f"{x}:{z}")
        
	if u == 1:
		print("\n \n \n \n")
