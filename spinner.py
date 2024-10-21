# initial state of spinner is null (stable) 
state= {'turn':0 } 

# Draw fidget spinner 
def spin(): 
	clear() 

	# Angle of fidget spinner 
	angle = state['turn']/10
	right(angle) 

	# move the turtle forward by specified 
	# distance 
	forward(100) 

	# draw a dot with diameter 120 using colour 
	# red 
	dot(120, 'red') 

	# move the turtle backward by specified 
	# distance 
	back(100) 

	"second dot"
	right(120) 
	forward(100) 
	dot(120, 'blue') 
	back(100) 

	"third dot"
	right(120) 
	forward(100) 
	dot(120, 'green') 
	back(100) 
	right(120) 

	update() 
