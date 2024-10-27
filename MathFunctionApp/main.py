#Sean Stack, COP1000 ID:2511132


from Program_5_2.function_5_2 import surface_area, volume

def main():
# Prompt user for the radius of the cylinder and store it
  radius = float(input('Enter the radius of the cylinder: '))
# Prompt user for the height of the cylinder and store it
  height = float(input('Enter the height of the cylinder: '))
# call the surface_area function imported from 5_2_function module and store it
  surface_area_1 = surface_area(radius,height)

# print the surface_area
  print(f'The surface area of the cylinder is {surface_area_1:.4f}')

# call the volume function imported from 5_2_function module
  volume(radius,height)
main()