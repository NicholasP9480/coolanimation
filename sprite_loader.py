import pygame


class Spritesheet:

      def_init_(self, ing_path):
            self .sprite_sheet = pygame.image.load(ing_path)

    def get_image(self, x, y, width, height):
        image = pygame,surface([width, heigh])
                image.blit(
                    self.sprite_sheet,
                    (0, 0)
                    (x, y, width, hieght)
         )
         image.set_colorkey(image.get_ at((0,0))
        return image


 