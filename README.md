Python Snake
==========================================

A Snake environment to train AIs.

![Playing](https://raw.githubusercontent.com/goktug97/PythonSnake/master/snake.gif)

## Requirements
* Python >= 3.6
* numpy

### Demo GUI
* cv2 

## Install

```bash
git clone https://github.com/goktug97/PythonSnake
cd PythonSnake
python setup.py install --user
```

## Play

``` bash
python-snake
```

## Usage

Check [play.py](https://github.com/goktug97/PythonSnake/blob/master/play.py) for an example.

``` python
import snake
import AwesomeAIAlgorithm
import cv2

game = snake.Game()
best_ai = AwesomeAIAlgorithm.BestAI()

while not game.done:
    screen = game.draw()
    cv2.imshow('center', screen)
    if cv2.waitKey(50) == 27:
        break
    action = best_ai.eval(game.map, game.snake.head,
                          game.snake.x_direction,
                          game.snake.y_direction,
                          game.apple)
    game.step(action)
```

