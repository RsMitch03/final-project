from PIL import Image, ImageDraw
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

# def music():

def main():
    """with Image.open(pic) as img:
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), score)
        img.show()"""
    pygame.init()
    scene = 1
    resize_fight()
    reformat_image()
    resolution = 600, 600
    hitCount = 0
    score = f"Hit Count: {hitCount}"
    scene = 1
    screen = pygame.display.set_mode(resolution)
    screen.fill(pygame.Color(255, 255, 255))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                hitCount += 1
                with Image.open(f"rogue_fight_{scene}.png") as img:
                    draw = ImageDraw.Draw(img)
                    draw.text((0, 0), score)
                    img.show()
            #if event.type == pygame.KEYDOWN and pygame.K_SPACE:
            #    fade to white
            #   scene += 1
            #   fade to new image
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()