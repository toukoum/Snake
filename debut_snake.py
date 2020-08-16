import sys, random
import pygame


class Jeu:
       
    def __init__(self):
        
        self.ecran = pygame.display.set_mode((800, 600))
        
        pygame.display.set_caption ("__JEU SNAKE__")
        self.jeu_encours = True 

        # direction du serpent 
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0 
        self.dimension_serpent = 10

        # pomme 
        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.dimension_pomme = 10 
        self.clock = pygame.time.Clock()

        # liste des positions du serpent 
        self.liste_position_serpent =[]
        
        # taille du serpent 
        self.taille_du_serpent = 1

        self.ecran_de_debut = True  

    def fonction_principale(self):
        while self.ecran_de_debut:
            for evenement in pygame.event.get():
            
                if evenement.type==pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_de_debut = False 
                
                self.ecran.fill((0,0,0))
                self.creer_message('grande', 'JEU SNAKE', (335, 60, 50, 50),(0, 255, 0))
                self.creer_message('petite', 'Le but du jeu est que le serpent grandisse', (300, 250, 300, 50),(240,240,240))
                self.creer_message('petite', 'pour cela, mangez les pommes rouges', (310, 270, 300, 5),(240,240,240))
                self.creer_message('moyenne', 'Appuyer sur ENTRER pour commencer !!', (250, 450, 200, 5),(240,240,240))

                pygame.display.flip()


        while self.jeu_encours:

            for evenement in pygame.event.get():
            
                if evenement.type==pygame.QUIT:
                    sys.exit()
                
                if evenement.type==pygame.KEYDOWN:

                    if evenement.key==pygame.K_RIGHT:
                        self.serpent_direction_x=10
                        self.serpent_direction_y=0
                        print('DROITE')
                    
                    if evenement.key==pygame.K_LEFT:
                        self.serpent_direction_y=0
                        self.serpent_direction_x=-10
                        print('GAUCHE')
                    
                    if evenement.key==pygame.K_DOWN:
                        self.serpent_direction_x=0
                        self.serpent_direction_y=10
                        print('BAS')
                    
                    if evenement.key==pygame.K_UP:
                        self.serpent_direction_y=-10
                        self.serpent_direction_x=0
                        print('HAUT')
            
            
            # position de la tete du serpent 
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)
        
            # on ajoute les positions de la tete du serpent dans la liste des positions du serpent en entier 
            self.liste_position_serpent.append(la_tete_du_serpent)
            
            # si le nombre des positions du serpent est plus grand que que la taille du serpent, alors on supprime l'élément numero 1
            if len(self.liste_position_serpent)>self.taille_du_serpent:
                self.liste_position_serpent.pop(0)

            self.serpent_mouvement()
            self.afficher_les_elements()
            self.se_mord(la_tete_du_serpent)
            self.serpent_qui_grandit()
            self.quite_si_touche_bordure()
    


            self.cree_limite()
            self.clock.tick(20)

            pygame.display.flip()


    
    def cree_limite(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)

    def serpent_mouvement(self):
        # déplacement du serpent
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y


    def afficher_les_elements(self):
            # ecran de couleur noir 
            self.ecran.fill((0, 0, 0))
            
            # afficher le serpent    
            pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y, self.dimension_serpent, self.dimension_serpent))

            # afficher la pomme 
            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme_position_x, self.pomme_position_y, self.dimension_pomme, self.dimension_pomme))

            self.afficher_les_elements_du_serpent()


    def afficher_les_elements_du_serpent(self):
         # afficher les autres parties du serpent 
        for partie_du_serpent in self.liste_position_serpent:
            print(partie_du_serpent)
            pygame.draw.rect(self.ecran,(0,255,0), (partie_du_serpent[0], partie_du_serpent[1], self.dimension_serpent, self.dimension_serpent))
    
    
    def se_mord(self, la_tete_du_serpent):
        # si le serpent de mort la queue, le jeu stop

        for partie_du_serpent in self.liste_position_serpent[:-1]:
            if la_tete_du_serpent == partie_du_serpent:

                sys.exit()

   
    def serpent_qui_grandit(self):
        # si le serpent mange la pomme, il doit grandir
        if self.pomme_position_y==self.serpent_position_y and self.pomme_position_x== self.serpent_position_x:
                
            self.pomme_position_x= random.randrange(110, 690, 10)
            self.pomme_position_y= random.randrange(110, 590, 10)

            self.taille_du_serpent+=1
    
    
    def quite_si_touche_bordure(self):
        # si on touche les bordures, le jeu quite  
        if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
            or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:

            sys.exit()


    def creer_message(self, font, message,message_rectangle, couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)

        if font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, False)

        if font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)

        message = font.render(message, True, couleur)

        self.ecran.blit(message, message_rectangle)





if __name__ =='__main__':

    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
                
