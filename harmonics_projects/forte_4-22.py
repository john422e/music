"""
Sends one of two loop of the the 24 chords of the Forte-22 pitch class set to
Max for playback.
"""
import pygame, argparse, time, sys
import subprocess as sp

from pythonosc import osc_message_builder
from pythonosc import udp_client

def transpose_octaves(a_list):
    # transposes 4 pitch set to C4 octave
    b_list = []
    for pitch in a_list:
        pitch += 60
        b_list.append(pitch)
    return b_list

loop_1 = [[0, 2, 4, 7], [0, 2, 4, 9], [2, 4, 6, 9], [2, 4, 6, 11],
          [4, 6, 8, 11], [1, 4, 6, 8], [1, 6, 8, 10], [3, 6, 8, 10],
          [0, 3, 8, 10], [0, 5, 8, 10], [0, 2, 5, 10], [0, 2, 7, 10]]

loop_2 = [[1, 3, 5, 8], [1, 3, 5, 10], [3, 5, 7, 10], [0, 3, 5, 7],
          [0, 5, 7, 9], [2, 5, 7, 9], [2, 7, 9, 11], [4, 7, 9, 11],
          [1, 4, 9, 11], [1, 6, 9, 11], [1, 3, 6, 11], [1, 3, 8, 11]]

PORT = 7401

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=PORT,
        help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)

pygame.init()

#open a window and set display (width, height)
size = (100, 50)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Forte 4-22")

loop = loop_1
loop_name = 'Loop 1:'
speed = 2.0
count = 0

#----- Main Program Loop -----
while True:
    #--- Main event loop
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user clicked 'close'
            done = True # exit main program loop
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                print("User asked to quit.")
            elif event.key == pygame.K_1:
                loop = loop_1
                loop_name = 'Loop 1:'
            elif event.key == pygame.K_2:
                loop = loop_2
                loop_name = 'Loop 2:'
            elif event.key == pygame.K_EQUALS and speed > 0.1:
                speed -= 0.1
                print(speed)
            elif event.key == pygame.K_MINUS:
                speed += 0.1
                print(speed)

    # --- Game logic should go here
    transposed = transpose_octaves(loop[count])
    transposed.append(speed * 990)
    print(loop_name, count + 1, loop[count])
    client.send_message("pitches", transposed)
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((0, 0, 0))

    # --- Drawing code should go here

    # --- Update the screen with what we've drawn
    pygame.display.flip()

    count += 1
    if count > 11:
        count = 0

    time.sleep(speed)

#Close the window and quit
pygame.quit()
