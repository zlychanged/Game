import cocos
import define

from cocos.director import director
from snake import Snake
from dot import Dot

class Arena(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        self.angle = None
        super().__init__(250, 255, 255, 255, director.get_window_size()[0], director.get_window_size()[1])
        # 游戏画框居中
        self.center = (director.get_window_size()[0] / 2, director.get_window_size()[1] / 2)
        # 动态调用GPU函数
        self.batch = cocos.batch.BatchNode() # type: ignore
        self.add(self.batch)

        self.snake = Snake()
        self.add(self.snake, 10000)
        self.snake.init_body()

        self.enemies = []
        # 添加其他蛇,ToDo：他们的行动能否智能控制些？
        for i in range(1):
            self.add_enemy()
        # 知识点set()：https://www.doubao.com/thread/wa4d4b8657a096641
        self.keys_pressed = set()

        # 默认屏幕上有50个零食
        for i in range(50):
            self.batch.add(Dot())

        self.schedule(self.update)

    def add_enemy(self):
        enemy = Snake(True)
        self.add(enemy, 10000)
        enemy.init_body()
        self.enemies.append(enemy)

    def update(self, dt):
        self.x = self.center[0] - self.snake.x
        self.y = self.center[1] - self.snake.y

        # self.x = min(0, self.x)
        # self.y = min(0, self.y)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.snake.update_angle(self.keys_pressed)

    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.snake.update_angle(self.keys_pressed)
