import numpy as np
from models import simple2

g = 9.81


# F_d = 1/2 * air density * (flow velocity)^2 * coefficient of drag * surface area
def drag(area, cd, velocity, density=1.225):
	return 0.5 * density * velocity * np.abs(velocity) * cd * area


def area(radius):
	return 4 * np.pi * radius**2


class Golfball(simple2.Golfball):
	def __init__(self):
		simple2.Golfball.__init__(self)

		self.cd = 0.3

	def accelerations(self):
		fg = np.array([0, -g])
		fd = -drag(area(self.radius), self.cd, self.velocities())

		print(area(self.radius), self.cd, self.velocities())

		return (fg + fd) / self.mass
