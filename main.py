import numpy as np
import matplotlib.pyplot as plt


print("Select an option")
print("Option 1")
print("Option 2")
print("Option 3")
c=input("Select   ")


if c=="1":
	x=np.linspace(1,100,100)
	y=np.sin(x)
	plt.plot(x,y)
else:
	print("selecciono otro")

