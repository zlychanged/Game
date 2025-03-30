import cocos
import define

from arena import Arena
from gameover import Gameover
from cocos.director import director

class GluttonousSnake(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        # 调用父类的init
        super().__init__()
        # init Arena导入到当前类对象(控制颜色的类)
        self.arena = Arena()
        #将Arena添加到GluttonousSnake节点后，默认z是0
        self.add(self.arena)
        #ToDo：初始化分数符合正常累加逻辑
        self.score = cocos.text.Label('30',
                                      font_name='Times New Roman',
                                      font_size=24,
                                      color=define.GOLD)

        self.score.position = 20, 440
        self.add(self.score, 99999)

        self.gameover = Gameover()
        self.add(self.gameover, 100000)

    def update_score(self):
        self.score.element.text = str(self.arena.snake.score)

    def end_game(self):
        self.gameover.visible = True
        self.gameover.score.element.text = str(self.arena.snake.score)

    #鼠标按下事件，主要是在cocos2中run中做事件查询调用(相关学习参考cocos2文档)
    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.gameover.visible:
            self.gameover.visible = False
            self.arena.unschedule(self.arena.update)
            self.remove(self.arena)
            self.arena = Arena()
            self.add(self.arena)
            self.update_score()

director.init(define.WIDTH, define.HEIGHT, caption="贪吃蛇")
director.run(cocos.scene.Scene(GluttonousSnake()))
