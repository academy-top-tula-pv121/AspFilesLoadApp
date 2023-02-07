import time
import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

#icon = pygame.image.load('icon.jpg')

max = 100
first = 0
second = str(first)
third = 0
fourth = str(third)
lie = 0

def feas():
    pygame.display.update()
    screen.fill((100, 0, 0))

pygame.init()
screen = pygame.display.set_mode((850, 150))
pygame.display.set_caption("WARNING!")
font = pygame.font.SysFont("Lucida Console", 20)

while lie==0:
    while first<=max:
        feas()
        label = font.render("Delete your files... "+ second, 1, (255, 0, 0, 1))
        screen.blit(label, (50, 50))
        first += 1
        second = str(first)
        time.sleep(0.01)
    while third<=max:
        feas()
        label = font.render("Delete your files... 100", 1, (255, 0, 0, 1))
        label1 = font.render("Stealing your money... "+ fourth, 1, (0, 255, 0, 2))
        screen.blit(label, (50, 50))
        screen.blit(label1, (50, 70))
        third += 1
        fourth = str(third)
        time.sleep(0.01)
    label2 = font.render("Tvoi compudahter sloman!", 1, (255, 0, 0, 3))
    screen.blit(label2, (500, 60))
    lie = 1

#pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)
            screen = pygame.display.set_mode((850, 150))
            pygame.display.set_caption("IMPORTANT MESSAGE")
            #pygame.display.set_icon(icon)
            messagebox.showerror("LOL", "WE ARE ENCRYPTING YOUR FILES")

    screen.fill((100, 0, 0))
    screen.blit(label, (50, 50))
    screen.blit(label1, (50, 70))
    screen.blit(label2, (500, 60))
    pygame.display.update()