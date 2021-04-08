from hero import Hero
class Police(Hero):
    name="police"

    def __init__(self,hp=1200,power=60):
        '''
        :param hp: 定义police血量，默认为1200
        :param power: 定义police攻击，默认为60
        '''
        self.hp=hp
        self.power=power

    def speak_lines(self):
        '''
        重写hero的speak方法，用于police说自己独特的话
        '''
        print("见识一下法律的子弹")