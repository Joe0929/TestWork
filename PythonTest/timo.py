from hero import Hero
class Timo(Hero):

    name = "timo"

    def __init__(self,hp=1300,power=50):
        '''
        :param hp: 定义timo血量，默认为1300
        :param power: 定义timo攻击，默认为50
        '''
        self.hp=hp
        self.power=power

    def speak_lines(self):
        '''
        重写hero的speak方法，用于timo说自己独特的话
        '''
        print("提莫队长正在待命")