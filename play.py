#!/usr/bin/env python3

import argparse

import cv2

import snake

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python Graph Slam')
    parser.add_argument('--map_size', type=int, help='Map Size', default=50)
    parser.add_argument('--block_size', type=int, help='Block Size', default=15)
    args = parser.parse_args()
    game = snake.Game(args.map_size)
    while not game.done:
        screen = game.draw(args.block_size)
        cv2.imshow('cvwindow', screen)
        key = cv2.waitKey(50)
        if key == 81:
            direction = -game.snake.y_direction
        elif key == 82:
            direction = -game.snake.x_direction
        elif key == 83:
            direction = game.snake.y_direction
        elif key == 84:
            direction = game.snake.x_direction
        elif key == 27:
            break
        else:
            direction = 0
        game.step(direction)
