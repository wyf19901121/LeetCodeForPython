import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while 1:
            x = random.uniform(self.x_center - self.radius,
                               self.x_center + self.radius)
            y = random.uniform(self.y_center - self.radius,
                               self.y_center + self.radius)
            if (x - self.x_center)**2 + (y - self.y_center)**2 <= self.radius**2:
                break
        return [x, y]
