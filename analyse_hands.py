import read_txt
import pygame

pygame.init()

filteredLines = read_txt.readFileAndFilter('sampleFile.txt')
hands = read_txt.splitHands(filteredLines)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

def analyseHand(hand):
    sb = hand.playerNames[1]
    bb = hand.playerNames[2]

    #Find Blinds
    BBLineWords = hand.events[1].split()
    BB = BBLineWords[4]
    BB = BB.replace("[", "")
    BB = BB.replace("]", "")
    BB = BB.replace("$", "")
    BB = float(BB)
    SB = BB/2

for hand in hands:
    analyseHand(hand)
