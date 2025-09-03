import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500,500
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Color changing sprite")
    color = {"red":pygame.Color("red"),"green":pygame.Color("green"),"blue":pygame.Color("blue"),"yellow":pygame.Color("yellow"),"white":pygame.Color("white")}
    current_color = color["white"]
    x,y = 30,30
    sprite_width,sprite_height = 60,60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            x = x - 3
        if pressed[pygame.K_d]:
            x = x + 3
        if pressed[pygame.K_w]:
            y = y - 3
        if pressed[pygame.K_s]:
            y = y + 3
        x = min(max(0,x), screen_width - sprite_width)
        y = min(max(0,y), screen_height - sprite_height)
        if x == 0:
            current_color = color["blue"]
        elif x == screen_width - sprite_width:
            color["yellow"]
        elif y == 0:
            current_color = color["red"]
        elif y == screen_height - sprite_height:
            current_color = color["green"]
        else:
            current_color = color["white"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,(x,y,sprite_width,sprite_width))
        pygame.display.flip()
        clock.tick()
    pygame.quit()
if __name__ == "__main__":
    main()