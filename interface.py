class Interface: 
        BLACK = [0,0,0]
        WHITE = [255,255,255]   
        RED = (139,0,0)
        FPS = 60
        

        DISPLAY_WIDTH = 390 #setting height - Any drawn is based off a percentage of the width and height 
        DISPLAY_HEIGHT = 700 #setting width
        Display_Size = [DISPLAY_WIDTH, DISPLAY_HEIGHT] #creating display size
        advice_position = (DISPLAY_WIDTH * 0.25, DISPLAY_HEIGHT * 0.6)

        top_heading = 'Car Simulator'
        bottom_heading = 'Gear Advice'
        instruction = 'Simulator Instructions'
        speedup = 'Increase speed'
        speeddown = 'Decrease speed'
        gearup = 'Shift up gear'
        geardown = 'Shift down gear'

        speedup_position = (DISPLAY_WIDTH * 0.37, DISPLAY_HEIGHT * 0.78)
        speeddown_position = (DISPLAY_WIDTH * 0.37, DISPLAY_HEIGHT * 0.95)
        gearup_position = (DISPLAY_WIDTH * 0.68, DISPLAY_HEIGHT * 0.89)
        geardown_position = (DISPLAY_WIDTH * 0.05, DISPLAY_HEIGHT * 0.89)

        

        FCR = 'FCR'
        SPEED = 'Speed'
        CURRENT_GEAR = 'Current Gear'
        


        SPEED_heading_position = (DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)
        SPEED_position = (DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.15)

        FCR_heading_position = (DISPLAY_WIDTH * 0.6, DISPLAY_HEIGHT * 0.1)
        FCR_position = ((DISPLAY_WIDTH * 0.6 , DISPLAY_HEIGHT * 0.15))


        x_CURRENT_GEAR = DISPLAY_WIDTH * 0.3
        
        
        CURRENT_GEAR_heading_position = (DISPLAY_WIDTH * 0.29, DISPLAY_HEIGHT * 0.25)
        CURRENT_GEAR_position = (DISPLAY_WIDTH * 0.45, DISPLAY_HEIGHT * 0.3)

        bottom_heading_position = (DISPLAY_WIDTH * 0.25, DISPLAY_HEIGHT * 0.45)
        top_heading_position = (DISPLAY_WIDTH * 0.22, DISPLAY_HEIGHT * 0.02)
        instruction_position = (DISPLAY_WIDTH * 0.04, DISPLAY_HEIGHT * 0.7)
        

        import pygame
        from pygame import mixer
        import os

        os.chdir(os.path.dirname(os.path.realpath(__file__)))       
        pygame.init() #initialising pygame
        mixer.init()
        mixer.music.load('carsounds.mp3')

        
        screen = pygame.display.set_mode(Display_Size) #creating screen - can be called when ready to show 
        clock = pygame.time.Clock()
        pygame.display.set_caption('Gear Advisor') #setting display captain
        sfont_size = round(DISPLAY_WIDTH * 0.038)
        font_size = round(DISPLAY_WIDTH * 0.064)
        lfont_size = round(DISPLAY_WIDTH * 0.075)
        smallfont = pygame.font.SysFont('verdana', sfont_size, bold=False, italic=False)
        font = pygame.font.SysFont('verdana', font_size, bold=False, italic=False)
        font_bold = pygame.font.SysFont('verdana', lfont_size, bold=True, italic=True) #setting text font and size 
        screen.fill(WHITE)
        

        arrowkeyImg = pygame.image.load('arrowkey.jpeg')
        imgsize = pygame.transform.scale(arrowkeyImg,(int(DISPLAY_WIDTH * 0.2),int(DISPLAY_WIDTH * 0.2)))
        img_position = (DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * 0.83)
        text = ''

        
        mixer.music.play(-1)
        

        def __init__(self):
            pass

        def check_for_input(self):
            for event in self.pygame.event.get():
            # If a pygame.QUIT event is in the queue.
                if event.type == self.pygame.QUIT:
                    print('hello')
                    self.pygame.quit()
                    quit()
                elif event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP:
                        return 1
                    elif event.key == self.pygame.K_DOWN:
                        return 2
                    elif  event.key == self.pygame.K_RIGHT:
                        gear_sound = self.mixer.Sound('gearshift.mp3')
                        gear_sound.play()
                        return 3
                    elif  event.key == self.pygame.K_LEFT:
                        gear_sound = self.mixer.Sound('gearshift.mp3')
                        gear_sound.play()
                        return 4

        def update_advice(self, direction, gear, speed, FCR):
            self.c_speed = str(speed) + ' kmh'
            self.c_fcr = str(round(FCR * 100, 1)) + ' kpl'
            self.c_gear = str(gear)
            
            self.pygame.mixer.music.set_volume((speed/100))
            
            if direction == 'maintain': 
                self.text = 'Maintain Gear ' + self.c_gear
            elif direction == 'up':
                self.text = 'Shift up to gear ' + str(gear + 1)
            elif direction == 'down':
                self.text = 'Shift down to gear ' + str(gear - 1)
            else:
                self.text = 'Waiting for input'
            

        def draw_changing_advice(self):
            self.command = self.font.render(self.text, True, self.BLACK)
            self.screen.blit(self.command,self.advice_position)

            speed_update = self.font.render(self.c_speed, True, self.BLACK)
            self.screen.blit(speed_update,self.SPEED_position)     

            fcr_update = self.font.render(self.c_fcr, True, self.BLACK)
            self.screen.blit(fcr_update,self.FCR_position)       

            gear_update = self.font.render(self.c_gear, True, self.BLACK)
            self.screen.blit(gear_update,self.CURRENT_GEAR_position)         
        
        def draw_unchanging_text(self):
            self.command = self.font.render(self.text, True, self.BLACK)
            self.screen.blit(self.command,self.position)

            speed_update = self.font.render(self.c_speed, True, self.BLACK)
            self.screen.blit(speed_update,self.FCR_position)     

            fcr_update = self.font.render(self.c_fcr, True, self.BLACK)
            self.screen.blit(fcr_update,self.SPEED_position)       

            gear_update = self.font.render(self.c_gear, True, self.BLACK)
            self.screen.blit(gear_update,self.CURRENT_GEAR_position)         

            self.pygame.display.update()
            self.clock.tick(self.FPS) #sets clock to 60 FPS 
        
        def draw_unchanging_text(self):
            FCR_text = self.font.render(self.FCR, True, self.BLACK)
            SPEED_text = self.font.render(self.SPEED, True, self.BLACK)
            CURRENT_GEAR_text = self.font.render(self.CURRENT_GEAR, True, self.BLACK)
            top_text = self.font_bold.render(self.top_heading, True, self.BLACK)
            bottom_text = self.font_bold.render(self.bottom_heading, True, self.BLACK)
            instruction_text = self.font_bold.render(self.instruction, True, self.RED)

            speedup_text = self.smallfont.render(self.speedup, True, self.RED)
            speeddown_text = self.smallfont.render(self.speeddown, True, self.RED)
            gearup_text = self.smallfont.render(self.gearup, True, self.RED)
            geardown_text = self.smallfont.render(self.geardown, True, self.RED)

            self.screen.blit(speedup_text, self.speedup_position)
            self.screen.blit(speeddown_text, self.speeddown_position)
            self.screen.blit(gearup_text, self.gearup_position) #
            self.screen.blit(geardown_text, self.geardown_position) #
            self.screen.blit(instruction_text, self.instruction_position) #draws instuctions on another surface
            self.screen.blit(bottom_text, self.bottom_heading_position) # draws gear advice onto another surface - white background
            self.screen.blit(top_text, self.top_heading_position) #draws car simulator text onto surface
            self.screen.blit(self.imgsize,self.img_position) #draws ftext onto another surface - white background
            self.screen.blit(FCR_text, self.FCR_heading_position) #draws uel consumption text onto another surface - white background
            self.screen.blit(SPEED_text, self.SPEED_heading_position) #draws speed text onto another surface 
            self.screen.blit(CURRENT_GEAR_text, self.CURRENT_GEAR_heading_position) #draws current gear text onto another surface 

            self.pygame.display.update() #updates display screen with changes 


        def main_draw(self): #function that can be called within the class
            self.screen.fill(self.WHITE) # fills screen white before anything else is drawn - is background 
            self.draw_changing_advice() #calls function 
            self.draw_unchanging_text() #calls function 
            self.pygame.display.update() #updates display screen with changes 
            
            
