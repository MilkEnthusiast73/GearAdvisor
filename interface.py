class Interface(): 
        BLACK = [0,0,0]
        WHITE = [255,255,255]   
        FPS = 60
        

        DISPLAY_WIDTH = 390 #setting height - Any drawn is based off a percentage of the width and height 
        DISPLAY_HEIGHT = 700 #setting width
        Display_Size = [DISPLAY_WIDTH, DISPLAY_HEIGHT] #creating display size
        x_axis = DISPLAY_WIDTH * 0.18
        y_axis = DISPLAY_HEIGHT * 0.6
        position = (x_axis, y_axis)

        advice = 'Advice'
        x_advice = DISPLAY_WIDTH * 0.37
        y_advice = DISPLAY_HEIGHT * 0.5
        advice_location = (x_advice, y_advice)

        FCR = 'FCR'
        SPEED = 'Speed'
        CURRENT_GEAR = 'Current Gear'

        speed_unit = 'kmh'
        Fuel_efficiency_unit = 'kpl'


        x_FCR =  DISPLAY_WIDTH * 0.75
        Y = DISPLAY_HEIGHT * 0.2
        x_SPEED = DISPLAY_WIDTH * 0.04
        x_CURRENT_GEAR = DISPLAY_WIDTH * 0.3
        FCR_location = (x_FCR, Y)
        FCR_position = ((x_FCR , Y +30))
        Fuel_efficiency_unit_position = ((x_FCR + 50, Y +30))
        SPEED_location = (x_SPEED, Y)
        SPEED_position = (x_SPEED, Y+30)
        speed_unit_position = (x_SPEED + 17, Y+60)
        CURRENT_GEAR_location = (x_CURRENT_GEAR, Y)
        CURRENT_GEAR_position = (x_CURRENT_GEAR +60, Y+30)

        

        import pygame
        pygame.init() #initialising pygame
        screen = pygame.display.set_mode(Display_Size) #creating screen - can be called when ready to show 
        clock = pygame.time.Clock()
        pygame.display.set_caption('App Display') #setting display captain
        font = pygame.font.Font('freesansbold.ttf', 18, bold=False, italic=False)
        font_bold = pygame.font.Font('freesansbold.ttf', 18, bold=True, italic=True) #setting text font and size 
        screen.fill(WHITE)
        
        text = ''
        

        def __init__(self):
            pass

        def check_for_input(self):
            for event in self.pygame.event.get():
            # If a pygame.QUIT event is in the queue.
                if event.type == self.pygame.QUIT :
                    running = False
                    self.pygame.quit()
                    quit()
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP:
                        return 1
                    elif event.key == self.pygame.K_DOWN:
                        return 2
                    elif  event.key == self.pygame.K_RIGHT:
                        return 3
                    elif  event.key == self.pygame.K_LEFT:
                        return 4
                return None 

        def update_advice(self, direction, gear, speed, FCR):
            
            if direction == 'maintain': 
                self.text = 'Maintain Gear '
                #display_return = Function(text)
            elif direction == 'up':
                self.text = 'Shift up to gear '     
            elif direction == 'down':
                self.text = 'Shift down to gear '        
            else:
                self.text = 'Waiting for your car information'
            
            self.c_speed = str(speed)
            self.c_fcr = str(FCR)
            self.c_gear = str(gear)

        def draw_changing_advice(self):
            self.command = self.font.render(self.text, True, self.BLACK)
            self.screen.blit(self.command,self.position)

            speed_update = self.font.render(self.c_speed, True, self.BLACK)
            self.screen.blit(speed_update,self.SPEED_position)     

            fcr_update = self.font.render(self.c_fcr, True, self.BLACK)
            self.screen.blit(fcr_update,self.FCR_position)       

            gear_update = self.font.render(self.c_gear, True, self.BLACK)
            self.screen.blit(gear_update,self.CURRENT_GEAR_position)         
        
        def draw_unchanging_text(self):
            FCR_text = self.font_bold.render(self.FCR, True, self.BLACK)
            SPEED_text = self.font_bold.render(self.SPEED, True, self.BLACK)
            CURRENT_GEAR_text = self.font_bold .render(self.CURRENT_GEAR, True, self.BLACK)
            advice_text = self.font_bold.render(self.advice, True, self.BLACK)
            self.screen.blit(advice_text, self.advice_location)
            self.screen.blit(FCR_text, self.FCR_location)
            self.screen.blit(SPEED_text, self.SPEED_location)
            self.screen.blit(CURRENT_GEAR_text, self.CURRENT_GEAR_location)

            speed_unit = self.font.render(self.speed_unit, True, self.BLACK)
            self.screen.blit(speed_unit,self.speed_unit_position)      

            fcr_unit = self.font.render(self.Fuel_efficiency_unit, True, self.BLACK)
            self.screen.blit(fcr_unit,self.Fuel_efficiency_unit_position)    

        def main_draw(self):
            self.screen.fill(self.WHITE)
            self.draw_changing_advice()
            self.draw_unchanging_text()
            self.pygame.display.update()