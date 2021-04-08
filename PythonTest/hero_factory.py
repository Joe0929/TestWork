from timo import Timo
from police import Police

class HeroFactory:
    '''
    用于创建英雄
    '''
    def create_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("此英雄不再英雄工厂中")

