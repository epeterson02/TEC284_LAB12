# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at this time)
mc = Minecraft.create()
mc.postToChat("Hello World!")

x = input("X Coordinate: ")
y = input("Y Coordinate: ")
z = input("Z Coordinate: ")

x = int(x)
y = int(y)
z = int(z)

mc.setBlocks (x, y, z, x + 20, y + 20, z + 20, 3)
mc.setBlocks (x, y, z, x + 19, y + 19, z + 19, 0)