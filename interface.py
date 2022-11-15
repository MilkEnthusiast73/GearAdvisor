class Interface: 
        BLACK = [0,0,0]
        WHITE = [255,255,255]   
        FPS = 30
         
         

        DISPLAY_WIDTH = 390 #setting height - Any drawn is based off a percentage of the width and height 
        DISPLAY_HEIGHT = 700 #setting width
        Display_Size = [DISPLAY_WIDTH, DISPLAY_HEIGHT] #creating display size
        x_axis = DISPLAY_WIDTH * 0.18
        y_axis = DISPLAY_HEIGHT * 0.3
        position = (x_axis, y_axis)

        import pygame
        pygame.init() #initialising pygame
        screen = pygame.display.set_mode(Display_Size) #creating screen - can be called when ready to show 
        clock = pygame.time.Clock()
        pygame.display.set_caption('App Display') #setting display captain
        font = pygame.font.Font('freesansbold.ttf', 25) #setting text font and size 
        screen.fill(WHITE)
        
        text = ''
        

        def __init__(self):
            pass

        def check_for_quit(self):
            for event in self.pygame.event.get():
            # If a pygame.QUIT event is in the queue.
                if event.type == self.pygame.QUIT :
                    running = False
                    self.pygame.quit()
                    quit()
                elif event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_ESCAPE:
                        #If the escape key was pressed
                        running = False
                        self.pygame.quit()
                        quit()    

        def update_advice(self, direction):
            
            if direction[0] == 'Maintain': 
                self.text = 'Maintain in gear ' + str(direction[1]) 
                #display_return = Function(text)
            elif direction[0] == 'Up':
                self.text = 'Change up to gear ' + str(direction[1])     
            elif direction[0] == 'Down':
                self.text = 'Change down to gear ' + str(direction[1])        
            else:
                self.text = 'Waiting for your car information'       


        def draw(self):
            #screen.blit(iphone_size, IPHONE_POSITION)
            #pygame.draw.rect(screen, WHITE, Rectangle)
            self.command = self.font.render(self.text, True, self.BLACK)
            self.screen.blit(self.command,self.position)       
            self.pygame.display.update()
            self.clock.tick(self.FPS) #sets clock to reset at 60 FPS 

    
