#!/usr/bin/env python3

import argparse

import cv2

import snake

def main():
    parser = argparse.ArgumentParser(description='Python Snake Game')
    parser.add_argument('--map_size', type=int, help='Map Size', default=50)
    parser.add_argument('--block_size', type=int,
            help='Block Size', default=15)
    args = parser.parse_args()
    game = snake.Game(args.map_size)
    while not game.done:
        screen = game.draw(args.block_size)
        cv2.imshow('cvwindow', screen)
        key = cv2.waitKey(50)
        if key == 81 or key == ord('a') or key == ord('h'):
            direction = game.snake.y_direction
        elif key == 82 or key == ord('w') or key == ord('k'):
            direction = -game.snake.x_direction
        elif key == 83 or key == ord('d') or key == ord('l'):
            direction = -game.snake.y_direction
        elif key == 84 or key == ord('s') or key == ord('j'):
            direction = game.snake.x_direction
        elif key == 27:
            break
        else:
            direction = 0
        game.step(direction)
    size = game.map_size*args.block_size
    scale = 3
    cv2.putText(img = screen, text = 'Game Over',
                org = (size//(2*scale), size//2),
                fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                fontScale = scale, color = 0.5,
                thickness=4)
    cv2.imshow('cvwindow', screen)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
