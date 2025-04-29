from PIL import Image
import pygame

def resize_fight():
    amount = 20
    for frame in range(amount):
        with Image.open(f"Fight_scene\\rogue_fight_{frame+1}.jpg") as img:
            size = (int(img.width//1.5), int(img.height//1.5))
            new_size = img.resize(size)
            new_size.save(f"Fight_scene\\rogue_fight_{frame+1}.jpg")
def reformat_image():
     amount = 20
     for frame in range(amount):
          with Image.open(f"Fight_scene\\rogue_fight_{frame+1}.jpg") as img:
              img.save(f"Fight_scene\\rogue_fight_{frame+1}.png")

def main():
    pygame.init()
    resolution = 600, 800
    screen = pygame.display.set_mode(resolution)
    white = pygame.color(255, 255, 255)
    screen.fill(white)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()