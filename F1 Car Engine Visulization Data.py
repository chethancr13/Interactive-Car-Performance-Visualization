import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Simulated car data
speed = np.linspace(0, 200, 100)
rpm = np.linspace(1000, 8000, 100)
torque = np.random.randn(100, 100)

# Create the figure
fig = plt.figure(figsize=(10, 6))

# 3D plot for torque map
ax1 = fig.add_subplot(121, projection='3d')
X, Y = np.meshgrid(speed, rpm)
ax1.plot_surface(X, Y, torque)
ax1.set_xlabel('Speed (km/h)')
ax1.set_ylabel('RPM')
ax1.set_zlabel('Torque (Nm)')

# 2D plot for speed vs time
ax2 = fig.add_subplot(122)
ax2.plot(speed)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Speed (km/h)')

# Add a car image (replace with actual image)
car_img = plt.imread('car.png')
ax2.imshow(car_img, extent=[0, 10, 0, 50], aspect='auto', alpha=0.5)

plt.show()
