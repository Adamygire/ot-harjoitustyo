from ui.ui import UI
import pygame
import pygame.locals

def main():
    pygame.init()
    ui = UI()
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return

        ui.blit()
        pygame.display.flip()

if __name__ == '__main__':
    main()
