import numpy as np
import matplotlib.pyplot as plt


print("Select an option")
print("Option 1")
print("Option 2")
print("Option 3")
c=input("Select   ")


if c=="1":
<<<<<<< HEAD
	PlotSin(20,5)
=======
	x=np.linspace(1,100,100)
	y=np.sin(x)
	plt.plot(x,y)
	plt.show()
>>>>>>> master
else:
	print("selecciono otro")


<<<<<<< HEAD


def PlotSin(a,h):
	x=np.linspace(1,100,100)
	y=a*np.sin(x/h)
	plt.plot(x,y)
=======
>>>>>>> master
