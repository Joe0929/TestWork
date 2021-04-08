class Hero:
    '''
    hp 代表血量
    power 代表攻击力
    name 代表英雄的名字
    '''

    hp=0
    power=0
    name=None

    def fight(self,enemy):
        '''
        定义一个 fight 方法，用于两个英雄攻击、血量进行对比，血量剩余多的人获胜
        :param enemy:打架的对象
        :return:返回打架的结果
        '''
        if isinstance(enemy,Hero): #判断打架的对象是不是属于英雄
            my_hp = self.hp - enemy.power
            enemy_final_hp = enemy.hp - self.power
            if my_hp>enemy_final_hp:
                return print(f"{self.name}赢了")
            elif my_hp<enemy_final_hp:
                return print(f"{enemy.name}赢了")
            else:
                return print("无法判断谁赢了")
        else:
            raise Exception("这不是有效对象")


    def speak_lines(self):
        '''
        定义英雄说话的方法
        '''
        print("英雄会说话")