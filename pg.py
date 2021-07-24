import pygame


pygame.init()


#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,255,255)

#resolution of screen
res = (700,600)

#GameWindow
screen = pygame.display.set_mode(res)

#Title
pygame.display.set_caption("World's Hardest Game")
pygame.display.update()

font = pygame.font.SysFont('Italic', 55)

def Draw_Text(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

    



def GameLoop():
    #Variables
    init_velocity = 0.5

    velocity_x = 0
    rect_x = 300

    velocity_x2 = 0
    rect_x2 = 300

    velocity_x3 = 0
    rect_x3 = 300

    velocity_x4 = 0
    rect_x4 = 300

    rect_y1 = 100
    rect_y2 = 200
    rect_y3 = 300
    rect_y4 = 400

    exit_game = False
    ball_x = 200
    ball_y = 500
    deaths = 0
    #velocity_y = 0
    exit_x = 300
    exit_y = 30



    #GameLoop
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity_x = init_velocity
                    velocity_x2 = -init_velocity
                    velocity_x3 = init_velocity
                    velocity_x4 = -init_velocity

                if event.key  == pygame.K_RIGHT:
                    ball_x += 25

                if event.key  == pygame.K_LEFT:
                    ball_x -= 25

                if event.key  == pygame.K_UP:
                    ball_y -= 25

                if event.key  == pygame.K_DOWN:
                    ball_y += 25

            

        rect_x = rect_x + velocity_x
        rect_x2 = rect_x2 + velocity_x2
        rect_x3 = rect_x3 + velocity_x3
        rect_x4 = rect_x4 + velocity_x4

        if rect_x > 500 :
            velocity_x = -init_velocity

        if rect_x2 > 500:
            velocity_x2 = -init_velocity

        if rect_x3 > 500:
            velocity_x3 = -init_velocity

        if rect_x4 > 500:
            velocity_x4 = -init_velocity

        
        rect_x = rect_x + velocity_x
        rect_x2 = rect_x2 + velocity_x2
        rect_x3 = rect_x3 + velocity_x3
        rect_x4 = rect_x4 + velocity_x4

        if rect_x < 0:
            velocity_x = init_velocity

        if rect_x2 < 0:
            velocity_x2 = init_velocity

        if rect_x3 < 0:
            velocity_x3 = init_velocity

        if rect_x4 < 0:
            velocity_x4 = init_velocity

        rect_x = rect_x + velocity_x
        rect_x2 = rect_x2 + velocity_x2
        rect_x3 = rect_x3 + velocity_x3
        rect_x4 = rect_x4 + velocity_x4


        if abs(ball_x - rect_x)<25 and abs(ball_y - rect_y1)<25:
            deaths +=1
            ball_y = 500
        if abs(ball_x - rect_x2)<25 and abs(ball_y - rect_y2)<25:
            deaths +=1
            ball_y = 500
        if abs(ball_x - rect_x3)<25 and abs(ball_y - rect_y3)<25:
            deaths +=1
            ball_y = 500

        if abs(ball_x - rect_x4)<25 and abs(ball_y - rect_y4)<25:
            deaths +=1
            ball_y = 500

        if abs(ball_x - exit_x)<50 and abs(ball_y - exit_y)<50:
            init_velocity = 0
            Draw_Text("YOU WON! MR.CHAMP",red,100,200)
                
            
            
            
            
            
        pygame.display.update()

        screen.fill((0,0,0))
        rect1 = pygame.draw.rect(screen,red,[rect_x,rect_y1,200,25])
        rect2 = pygame.draw.rect(screen,green,[rect_x2,rect_y2,200,25])
        rect3 = pygame.draw.rect(screen,blue,[rect_x3,rect_y3,200,25])
        rect4 = pygame.draw.rect(screen,(255,255,0),[rect_x4,rect_y4,200,25])
        rect5 = pygame.draw.ellipse(screen,(250, 0, 154),[ball_x,ball_y,25,25])
        rect6 = pygame.draw.rect(screen,(255,255,0),[exit_x,exit_y,100,50])
        a = Draw_Text("Deaths :" + str(int(deaths)),green,45,25)
        b = Draw_Text("Press space to start",blue,300,550)
        c = Draw_Text("Exit",(0,0,0),325,30)
        
    
        pygame.display.update()

    pygame.quit() 
    quit()


GameLoop()
