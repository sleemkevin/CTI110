#Kevin Sleem
#June 22, 2024
#P2LAB1
#Circle Dimensions User Input

radius = float(input('What is the radius of the circle? '))
import math
diameter = radius * 2
circumference = 2 * math.pi * radius
area= math.pi * radius**2
print('The diameter of the circle is', end=' ')
print(f'{diameter:.1f}')
print('The circumference of the circle is', end=' ')
print(f'{circumference:.2f}')
print('The area of the circle is', end=' ')
print(f'{area:.3f}')
