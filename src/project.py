from PIL import Image, ImageDraw
import pygame

def resize_fight():
    amount = 20
    for frame in range(amount):
        with Image.open(f"OGFight_scene\\rogue_fight_{frame+1}.jpg") as img:
            size = (int(img.width//10), int(img.height//10))
            if frame == 13:
                size = (int(img.width//3.5), int(img.height//3.5))
            new_size = img.resize(size)
            new_size.save(f"Resized_scene\\rogue_fight_{frame+1}.jpg")
def reformat_image():
     amount = 20
     for frame in range(amount):
          with Image.open(f"Resized_scene\\rogue_fight_{frame+1}.jpg") as img:
              img.save(f"Final_fight_scene\\rogue_fight_{frame+1}.png")

def sliceSound():
    pygame.mixer.init()
    slice = pygame.mixer.Sound("Slice.wav")
    pygame.mixer.Sound.set_volume(slice, .90)
    pygame.mixer.Sound.play(slice)
    

def music():
    pygame.mixer.init()
    music = pygame.mixer.Sound("Music.wav")
    pygame.mixer.Sound.set_volume(music, .75)
    pygame.mixer.Sound.play(music, -1)
    

def main():
    """with Image.open(pic) as img:
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), score)
        img.show()"""
    pygame.init()
    music()
    pygame.freetype.init()
    scene = 1
    resize_fight()
    reformat_image()
    resolution = 300, 400
    hitCount = 0
    score = f"Hit Count: {hitCount}"
    scene = 1
    display = pygame.image.load(f"Final_fight_scene\\rogue_fight_{scene}.png")
    screen = pygame.display.set_mode(resolution)
    screen.fill(pygame.Color(255, 255, 255))
    screen.blit(display, (0, 0))
    font = pygame.freetype.SysFont('ariel', (24))
    text, rect = font.render(f'{score}', (0, 0, 0))
    screen.blit(text, (15, 15))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                display = pygame.image.load(f"Final_fight_scene\\rogue_fight_{scene+1}.png")
                screen.fill(pygame.Color(255, 255, 255))
                screen.blit(display, (0, 0))
                screen.blit(text, (15, 15))
                scene += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                hitCount += 1
                sliceSound()
                screen.fill(pygame.Color(255, 255, 255))
                screen.blit(display, (0, 0))
                text, rect = font.render(f'Hit Count: {hitCount}', (0, 0, 0))
                screen.blit(text, (15, 15))
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()