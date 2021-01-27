import numpy as np
import matplotlib.pyplot as plt


print("Select an option")
print("Option 1")
print("Option 2")
print("Option 3")
c=input("Select   ")


if c=="1":
	PlotSin(20,5)
else:
	print("selecciono otro")




def PlotSin(a,h):
	x=np.linspace(1,100,100)
	y=a*np.sin(x/h)
	plt.plot(x,y)