# 计算器
class Calculator:
    def add(self, a, b):
        '''
        加法运算
        :return: 两个数相加的结果
        '''
        return a + b

    def sub(self, a, b):
        '''
        减法运算
        :return: 两个数相减的结果
        '''
        return a - b

    def mul(self, a, b):
        '''
        乘法运算
        :return: 两个数相乘的结果
        '''
        return a * b

    def div(self, a, b):
        '''
        除法运算
        :return: 两个数相除的结果
        '''
        if b==0:    #被除数为0的异常处理
            print('除数不能为0')
            return 0
        else:
            return a / b