import pygame

class UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Sudoku')

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Display some text
        font = pygame.font.Font(None, 72)
        text = font.render("Sudoku", 1, (10, 10, 10))
        text_position = text.get_rect()
        text_position.centerx = self.background.get_rect().centerx
        self.background.blit(text, text_position)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def blit(self):
        self.screen.blit(self.background, (0, 0))