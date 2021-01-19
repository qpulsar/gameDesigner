
import sys
import pygame
import main

"""Asagıdaki muzigin telif haklari olabilir
sadece muzik ekleme calisiyor mu diye ekledim
herkes bu yorum satrini okuyunca kaldirebiliriz (zy)"""

music01= "./resources/musics/undertale.mp3"
pygame.mixer.music.load(music01)
pygame.mixer.music.play()


if __name__ == '__main__':
    main.main()
    pygame.quit()
    sys.exit()
