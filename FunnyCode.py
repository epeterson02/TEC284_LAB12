#This will place giant structures at the player location every 1 sec
#import the API
from mcpi_addons.minecraft import Minecraft
#Initialize the API (MCPI must be open and in a world at this time)
mc = Minecraft.create()
import time

count = 1
while count <= 30:
    pos = mc.player.getPos()
    mc.setBlocks (pos.x, pos.y, pos.z, pos.x + 20, pos.y + 20, pos.z + 20, 3)
    count += 1
    time.sleep(1)
