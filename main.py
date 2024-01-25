from gameboard import *
from cards import deck


def main():
    '''
    Shuffle the deck, create initial state of the "game"
    with a shuffled, full deck and instructions on how to deal a card
    '''
    deck.shuffle()
    WIN.fill((background))
    playing_deck()
    text = font.render(f'Cards left: {len(deck)}', True, text_color) 
    WIN.blit(text, (250, 700))  
    pygame.display.update()
    

    running = True
    show_card = False
    clock = pygame.time.Clock()

    while running:
        clock.tick(30)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #Only 'enter' key is accepted for dealing out cards
                show_card = True
                
            if show_card:  # Deals the next card on the board          
                WIN.blit(next_card(), (dealed_card_width, card_height))            
                playing_deck()               
                pygame.display.update()
                show_card = False
        
    pygame.quit()

main()