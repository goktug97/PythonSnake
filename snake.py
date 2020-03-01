import numpy as np

class Snake(object):
    def __init__(self, map_size):
        self.x_direction = 1
        self.y_direction = 0
        self.head = (map_size//2, map_size//2)
        self.body = [self.head]
        for i in range(2):
            self.body.append((self.body[-1][0]-self.x_direction,
                              self.body[-1][1]-self.y_direction))

    def grow(self):
        self.body.append(self.old_tail)

    def move(self, direction):
        self.turn(direction)
        self.old_tail = self.body[-1]
        for idx in reversed(range(len(self.body))):
            self.body[idx] = (self.body[idx-1] if idx else
                              (self.body[idx][0] + self.x_direction,
                               self.body[idx][1] + self.y_direction))
        self.head = self.body[0]

    def turn(self, direction):
        if direction:
            self.x_direction, self.y_direction = self.y_direction, self.x_direction
            self.x_direction *= -direction
            self.y_direction *= direction
        
class Game(object):
    def __init__(self, map_size):
        self.map_size = map_size
        self.snake = Snake(self.map_size)
        self.update_map()
        self.add_apple()
        self.done = False

    def update_map(self):
        self.map = np.zeros((self.map_size-2, self.map_size-2))
        self.map  = np.pad(self.map, ((1, 1), (1, 1)), 'constant', constant_values=1)
        body = np.array(self.snake.body)
        self.map[body[:, 1], body[:, 0]] = 1

    def add_apple(self):
        xgrid, ygrid = np.meshgrid(np.arange(self.map_size), np.arange(self.map_size))
        free_x = xgrid[self.map == 0]
        free_y = ygrid[self.map == 0]
        if len(free_x):
            idx = np.random.randint(len(free_x))
            self.apple = (free_x[idx], free_y[idx])

    def step(self, direction):
        if not self.done:
            self.snake.move(direction)
            if self.snake.head == self.apple:
                self.snake.grow()
                self.add_apple()
            elif self.map[self.snake.head[1], self.snake.head[0]]:
                self.done = True
            self.update_map()

    def draw(self, block_size: int):
        screen = self.map.copy()
        screen[self.apple[1], self.apple[0]] = 0.5
        screen = np.repeat(screen, block_size, axis=1)
        screen = np.repeat(screen, block_size, axis=0)
        return screen
