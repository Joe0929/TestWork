from hero_factory import HeroFactory

if __name__=="__main__":
    '''测试'''
    hero_factory = HeroFactory()    #创建英雄工厂实例
    timo = hero_factory.create_hero("timo") #创建Timo英雄实例
    police = hero_factory.create_hero("police") #创建police英雄实例
    police.fight(timo)  #police与timo进行fight
    timo.speak_lines()  #timo说话
    police.speak_lines()    #police说话