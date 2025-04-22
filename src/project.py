from PIL import Image
import pygame

def resize_sequence(folder_path, height):
    amount = 72
    for frame in range(amount):
            if frame+1 < 10:
                 with Image.open(f"Fight_scene\\rogue_fight_{frame+1}.jpg") as img:
                      size = (int(img.width//1.5), int(img.height//1.5))
                      new_size = img.resize(size)
                      new_size.save(f"Fight_scene\\rogue_fight_{frame+1}.png")
            else: 
                 with Image.open(f"Fight_scene\\rogue_fight_{frame+1}.jpg") as img:
                      size = (int(img.width//1.5), int(img.height//1.5))
                      new_size = img.resize(size)
                      new_size.save(f"Fight_scene\\rogue_fight_{frame+1}.png")