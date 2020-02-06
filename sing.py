class singleton(object):
	_instance=None
	def __new__(self):
		if not self._instance:
			self._instance=super(singleton,self).__new__(self)
		return self._instance

x=singleton()
for 
print(x.y)
x.y=20
z=x
print(z.y)