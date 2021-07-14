import pygame

pygame.init()

screen = (600, 600)
win = pygame.display.set_mode(screen, pygame.RESIZABLE)
#pygame.display.set_icon(pygame.image.load("logo.png"))
pygame.display.set_caption("Game On!")

x = 300
y = 300
width = 40
height = 60
speed_x = 0
speed_y = 0
acc = 3
run = True

def rounding(number):
    return int(str(number).split(".")[0])


while run:
    pygame.time.delay(30)
    win.fill((5, 179, 173))
    font = pygame.font.Font('Helvetica-Normal.ttf', 30)
    text = font.render(f"{round(x)}, {round(y)}", True, (30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed_x + width / 2:
        speed_x -= acc

    if keys[pygame.K_RIGHT] and x < screen[0] - width:
        speed_x += acc

    if keys[pygame.K_UP] and y > speed_y + height / 2:
        speed_y -= acc

    if keys[pygame.K_DOWN] and y < screen[1] - height / 2:
        speed_y += acc        

    pygame.draw.rect(win, (192, 253, 251), (x, y, width, height))
    win.blit(text, (0,0))

    x += speed_x
    y += speed_y

    screen = pygame.display.get_surface().get_size()

    if x < 0:
        x = 0
    if x > screen[0] - width:
        x = screen[0] - width
    if y < 0:
        y = 0
    if y > screen[1] - height:
        y = screen[1] - height


    speed_x = rounding(speed_x * .8)
    speed_y = rounding(speed_y * .8)
    
    pygame.display.update()

pygame.quit()