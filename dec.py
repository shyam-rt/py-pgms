
def smart_div(func):
	def inf(a,b):
		if a<b:
			a,b=b,a
		print("swapped")
		return func(a,b)
	print(inf)
	return inf
#@smart_div
def div(a,b):
	print(a//b)

div=smart_div(div)
div(4,2)