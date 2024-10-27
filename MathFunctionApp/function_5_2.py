import math

def surface_area(radius, height):
  surface_area = 2 * math.pi * radius * (radius + height)
  return surface_area


def volume(radius, height):
  volume = math.pi * radius**2 * height
  print(f'The volume of the cylinder is {volume:.3f}')
