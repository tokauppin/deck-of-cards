import pygame
import os
from cards import deck
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Virtual Deck of Cards')
current_directory = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_directory, 'pics')

# text on screen
text_color = (0, 0, 0)
background = (211,211,211)
font = pygame.font.Font('freesansbold.ttf', 45)

# card positions on board
deck_width = 100
card_height = 200
dealed_card_width = 450

def text_on_top():
    text = font.render('Press enter to deal a card', True, text_color)
    WIN.blit(text, (120, 100))

def cards_left():
    '''
    shows how many cards are left in the deck
    '''
    # replace old text by drawing a new background
    pygame.draw.rect(WIN, background, pygame.Rect(0, 0, WIDTH, HEIGHT))
    pygame.display.update()

    #draw new text
    text = font.render(f'Cards left: {len(deck)}', True, text_color)
    WIN.blit(text, (250, 700))

def playing_deck():
    '''
    shows the deck with remaining cards in it
    '''
    text_on_top()
    if len(deck) == 0:
        return
    pack = pygame.image.load(os.path.join(image_folder, "cardback.jpg")) # Change the cardback to one you like
    pack = pygame.transform.scale(pack, (250, 400))
    WIN.blit(pack, (deck_width, card_height))
    

def next_card():
    '''
    Picks the next card from the deck to be displayed
    '''
    if len(deck) == 0:
        deck.generate_deck()
        deck.shuffle()
     
    next_card = str(deck.pop(0))
    card_in_play = pygame.image.load(os.path.join(image_folder, next_card + ".png"))
    card_in_play = pygame.transform.scale(card_in_play, (250, 400))
    cards_left()

    return card_in_play
