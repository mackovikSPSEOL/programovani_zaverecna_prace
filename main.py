import pygame
import sys
import random
import time
from pygame import draw

    


pygame.init()
pygame.mixer.init()
pozadi = pygame.image.load("assets/background_krbec.jpg") # nahrání pozadí
pozadi_obchod = pygame.image.load("assets\shop/background_obchod.png")
pozadi_secret_1 = pygame.image.load("assets/k_animaci\kamna/cislo0.png")
pozadi_secret_2 = pygame.image.load("assets/k_animaci\kamna/cislo1.png")
obchod_item = pygame.image.load("assets\shop\oriskova_kava.png")
cesta_k_fontu = "assets/cesta_k_fontu/Ubuntu_Sans_Mono/static/UbuntuSansMono-Bold.ttf"
secret_audio = pygame.mixer.Sound("assets/audio/hello_there.mp3")
secret_audio2 = pygame.mixer.Sound("assets/audio/final_final.mp3")
after_click_audio = pygame.mixer.Sound("assets/audio/hejhou.mp3")
pozadi_hudba = pygame.mixer.Sound("assets/audio/pozadi_hudba.mp3")
obchod_hudba = pygame.mixer.Sound("assets/audio\shop\pozadi_obchod_hudba.mp3")

sirka, vyska = 1600, 900
obrazky = [] 
obrazky_2 = []
nasobek = 1
jeho_projekty = 0
count = 0
switch = 0
timer = 0
pocet_kav = 0
cena_kavy =  4*pocet_kav
switch_obchod = False

font_text = pygame.font.Font(cesta_k_fontu, 18)
text = font_text.render(f'Počet vytvořených projektů: {jeho_projekty}', True, (255, 255, 255))
obchod_item1 = font_text.render(f'Ořískové Cappuccino: {pocet_kav}', True, (0, 0, 0))
pozadi_secret_1 = pygame.transform.scale(pozadi_secret_1, (sirka, vyska))
pozadi_secret_2 = pygame.transform.scale(pozadi_secret_2, (sirka, vyska))
obchod_item = pygame.image.load("assets\shop\oriskova_kava.png")
pozadi_hudba.play(loops=-1)
fps = pygame.time.Clock()

krbec_button = pygame.Rect(130, 270, 198, 390)



obraz = pygame.display.set_mode((sirka, vyska)) # nastavení velikosti okna
pygame.display.set_caption("Krbec Clicker") # nastavení názvu okna

# def zakoupeni_itemu():
#     global pocet_kav
#     global cena_kavy
#     global jeho_projekty
#     time.sleep(0.5)
#     if jeho_projekty >= cena_kavy:
#         pocet_kav += 1        
#         jeho_projekty = jeho_projekty - cena_kavy


def refresh_obrazu():
        obraz.blit(pozadi, (0, 0))
        obraz.blit(text, (150, 150))
        # obraz.blit(obchod_item, (1200, 150))
        # obraz.blit(obchod_item1, (1210, 160))
        pygame.display.flip()


def secret():
    global switch
    if switch == 0:
                obraz.blit(pozadi_secret_1, (0, 0))
                pozadi_hudba.stop()
                time.sleep(0.5)
                secret_audio2.play(loops=-1)
                secret_audio.play()
                switch += 1
                for i in range(0, 10):
                    obraz.blit(pozadi_secret_1, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
                    obraz.blit(pozadi_secret_2, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
    else:
        secret_audio2.stop()
        time.sleep(0.2)
        pygame.display.flip()
        switch -= 1
        pozadi_hudba.play(loops=-1)


def update_text():
    return font_text.render(f'Počet vytvořených projektů: {jeho_projekty}', True, (255, 255, 255))

def list_obrazku(slozka, pocet_obrazku):
    # počet obrázků je číslo kolik obrázků je v složce :) 
    for pocet in range(pocet_obrazku):
        # print(f"assets\{slozka}\cislo{pocet}.png") na kontrolu cesty
        obrazek = pygame.image.load(f"assets\{slozka}\cislo{pocet}.png")
        obrazek = pygame.transform.scale(obrazek, (sirka, vyska))
        obrazky.append(obrazek)
        for i in range(0, pocet_obrazku-1):
            obrazky_mensi = pygame.transform.scale(pygame.image.load(f"assets/{slozka}/cislo{i}.png"), (300, 300))
            obrazky_2.append(obrazky_mensi)
    return obrazky_2 #vrací seznam s adresami obrázků pro další použítí (zárověň menší naformátování)
list_obrazku("animace_hlavniho_obrazku", 15) #načtení obrázků pro animaci

def animace(pocet_obrazku, poloha_x, poloha_y):
    global text
    global snimek
    for cislo in range(pocet_obrazku):
        snimek = obrazky_2[cislo]
        obraz.blit(pozadi,(0,0))
        text = update_text()
        obraz.blit(text, (150, 150))
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (poloha_x, poloha_y) 
        obraz.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.1)
   

while True:
    
    dt = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos) 
        # if event.pos[0] > 1200 and event.pos[0] < 1500 and event.pos[1] > 150 and event.pos[1] < 270:
        #         zakoupeni_itemu() failnul jsem to
                
                
        if krbec_button.collidepoint(event.pos):      
                # print("trefa_krbec") kontrola pozic
                after_click_audio.play()
                jeho_projekty += 1 * nasobek
                animace(14, 700, 700)
                
        if event.pos[0] > 5 and event.pos[0] < 100 and event.pos[1] > 783 and event.pos[1] < 890:
                secret()
    
    refresh_obrazu()
