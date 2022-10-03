# t1:
def t1():
    name = input("请输入姓名哈:")
    print("你好，" + name + "!")


# t2
def t2():
    num = input("请输入1-100之间数字：")
    check = int(num)
    if check == 19:
        print("回答正确")
    else:
        print("不对哈")


def t3():
    print("Let\'s go!")
    print("let's go!")
    print(f"let's go!")


def t4():
    year = 365
    day = 24
    hours = 60
    min = 60
    hourss = hours * min
    days = 24 * hourss
    years = 365 * days
    print(f'一年有{years}s')


def t5():
    num = input("请1-100输入数字：")
    check = int(num)
    while check != 10:
        num = input("请再1-100输入数字：")
        check = int(num)
        if check > 10:
            print("再小一点")
        elif check < 10:
            print("小咯")
        else:
            print("ok")
    print("bu")


def t6():
    member = ["嘿1", '嘿2', '嘿3', '嘿4']
    # 列表中插入一个元素
    # member.append('嘿5')
    # 列表中插入多个元素
    # member.extend(['嘿6','嘿7'])
    # 列表指定位置中插入元素
    # member.insert(2,['嘿8','嘿9'])
    member[0]
    member[1]
    t = member[1]
    member[1] = member[0]
    member[0] = t
    print(t)
    print(member[1])
    print(member)


def t7():
    # t="{{{1}}}".format("budayin","cehsi")
    # print(t)
    a = "ceshi"
    a = list(a)
    print(a)
    b = ["a", "b", "c"]
    b = tuple(b)
    print(b)
    c = {1, 2, 3, 4, 5, 6}
    c = max(c)
    print(c)


# 函数参数传递
def t8(num1, num2):
    result = num1 + num2
    print(result)


# 函数的返回值
def t9(num1, num2):
    result = num1 - num2
    return result


# 函数的形参和实参  定义函数时 设置了的参数 叫形参，调用函数时传入的值叫实参
def t9(num1, num2):
    result = num1 - num2
    return result
    t9(1, 2)


# 位置可变参数:不限制传参个数
def t10(*params):
    print("参数的长度", len(params))
    print('第二个参数', params[1])


# 要加可变参数外的参数时  需要使用关键字参数传递
def t11(*params, exp):
    print("参数的长度", len(params))


# 关键字可变参数，不限制关键字参数个数,,返回结果是一个字典
def t12(**params):
    print(params)


# 返回多个值
def back():
    return 1, "ceshi", 1.2


# 局部变量
# def discounts(price, rate):
#     final_price = price * rate
#     print('打印局部变量old_price', old_price)
#     return final_price
#
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣:'))
# # 折扣价
# new_price = discounts(old_price, rate)
# print('修改后的old值：', old_price)
#
# count=5
# def t13():
#     global count
#     count=10
#     print(10)
#     print('huhu',count)
# print(count)
# 内嵌函数
def x1():
    print('函数x1在被调用')

    def x2():
        print('函数x2在被调用')

    x2()


# 闭包
def x3(a):
    def x4(b):
        return a * b

    return x4

    # 递归 求5的阶乘 1*2*3*4*5 n*（n-1）
    def cont(n):
        if n == 1:
            return 1
        else:
            # 调用自身完成循环
            res = n * cont(n - 1)
        return res

    sum = cont(5)
    print(sum)

    # 迭代
    def factorial(n):
        result = n
        for i in range(1, n):
            result = result * i
        return result

    res = factorial(5)
    print(res)


# 年龄判断 18岁以下及70岁以上不能办理 知道正确
def age1(age):
    if age < 18:
        print(f'当前年龄{age},未满18 不行哦')
    elif age > 70:
        print(f'当前年龄{age},超过70 不行哦')
    else:
        print(f'当前年龄{age}，可以的')
    print('感谢使用')


# 三目
def sum3():
    a = 1
    b = 2
    c = a if a > b else b
    print(c)


# 字典
def dirct():
    a = {1: 'a', 2: 'b', 3: 'c'}
    # 字典键值变更
    a[1] = 'c'
    # 插入新键值
    a[4] = 'd'
    # get方法查询字典，找不到对应键值时，返回none
    print(a.get(5))
    # 通过[]键查询值,找不到对应键值时 报错 不继续执行
    print(a[4])
    # 查询字典中所有值
    print(a.values())
    # 已元组形式返回字典中键值
    print(a.items())
    # 字典遍历 键 a /a.keys
    for i in a:
        print(i)
    # 遍历字典 值
    for i in a.values():
        print(i)
    # 遍历字典 以元组形式
    for i, j in a.items():
        print(f'{i}={j}')
    # break
    for i in a:
        if i == 3:
            print(f'遇到{i}就停止')
            break
        print(i)
    # countinue
    for i in a:
        if i == 3:
            print(f'遇到{i}就跳过')
            continue
        print(i)


# 推导式 创建列表[1,3,5,7,9]
def list():
    # a=[]
    # for i in range(0,11):
    #     a.append(i)
    # print(a)
    a = [i for i in range(0, 11)]
    print(a)


def dirct2():
    # 合并列表为字典
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    c = {a[i]: b[i] for i in range(len(a))}
    print(c)


# while 打印1-100
def whil():
    i = 1
    while i < 100:
        i = i + 1
        print(i)
    print('jiehu ')


# n+（n-1）
def sum2(n):
    if n == 1:
        return 1
    else:
        su = n + sum2(n - 1)
        return su


def arg(*args):
    print(args)


# 多函数返回值调用
def name1():
    return 19


def name2(a):
    print(a)


i = name1()


# 文件读写
# 闭包 函数嵌套
def han1(a, b):
    c = 1

    def han2():
        s = a + b + c
        print(s)

    return han2


x = han1(1, 2)
x()


#
# # 面向对象
# # 1.定义类 类名格式按照大驼峰， 以类来组装真个学校 比如 学校里有老师 学生 校长这种人物角色
# class School:
#     #类属性，公共属性
#     class_num='一班'
#     #初始化方法  构造方法 实例化时会自动执行 进行一些初始化工作
#     def __init__(self,sex,adress):
#         print('初始化学生的性别，地址',sex,adress)
#         self.sex=sex
#         self.adress=adress
#
#     # self 表示这是一个实例方法，定义方法时 必须以第一个参数形式定义到方法中，在调用时 不需要写self参数,
#     #定义学生方法 用来存放学生信息
#     def student(self, name, age, sid):
#         data = {
#             'name': name,
#             'age': age,
#             'sid': sid,
#             'class':self.class_num
#         }
#         return data
# # 调用实例方法时  需要先实例化
# stu = School()
#
# s1=stu.student('小马', '18', '20151093002')
# s2=stu.student('小红', '10', '20151092333')
# print(s1,s2)


# @calssmethod 修饰 表示这是一个类方法，既可以由类名直接调用 也可以由实例来访问，，第一个参数必须是cls，实例方法权限高于类方法
# @classmethod
# def teacher(cls,name):
#     print('老师的姓名：{}'.format(name))
# 直接调用类名来访问
# School.teacher('张大枪')
# 也可以用实例方法调用访问
# tea=School()
# tea.teacher('李四')
# 实例属性，已self开头定义的属性叫实例属性


#
# if __name__ == "__main__":
#
#
#

# 面向对象示例  分别将大象 小狗 小猫装进冰箱
# 步骤分为 打开冰箱 装进动物 关闭冰箱
# 定义一个冰箱类
class Icebox:
    # 类属性 又叫公共属性 所有实例可共享 通过类名调用，也可以通过实例名去调用
    icebox_type = 'tcl'

    def __init__(self, animal_type):
        print('操作动物类型：{}'.format(animal_type))
        # 实例属性
        self.antype = animal_type

    def openbox(self):
        print('操作：{},打开{}冰箱'.format(self.antype, self.icebox_type))

    def putinto(self):
        print('操作：{},放入冰箱'.format(self.antype))

    def closebox(self):
        print('操作：{}，关闭冰箱'.format(self.antype))


# 实例方法 调用各操作步骤

dog = Icebox('小狗')
# 类属性通过重新调用变更值
Icebox.icebox_type = '美的'
print(dog.icebox_type)
print(dog.antype)
dog.openbox()
dog.putinto()
dog.closebox()
cat = Icebox('小猫')
cat.openbox()
cat.putinto()
cat.closebox()
elephant = Icebox('大象')
elephant.icebox_type = 'ceshi'
print(elephant.icebox_type)
elephant.openbox()
elephant.putinto()
elephant.closebox()

# 人狗大战实例
'''
狗人都有对应的生命值和攻击值，狗攻击人后 人的生命值会减少 人攻击狗后 狗的生命值会减少
'''


class Dog():
    # 定义狗的默认信息 包含 狗名称 品种 攻击值 生命值
    def __init__(self, name, type, attack):
        self.dname = name
        self.stype = type
        self.dattck = attack
        self.dlife = 100

    # 狗狗打人
    def dogattack(self, person):
        person.plife= person.plife - self.dattck
        print(person.plife)
        print('[%s]攻击了人[%s]，[%s]生命值减少为[%s]' % (self.dname, person.pname, person.pname, person.plife))


class Pepoles():
    # 定义人类信息 包括名称 攻击值 生命值
    def __init__(self, name, attack):
        self.pname = name
        self.pattack = attack
        self.plife = 100

    def pepoleattack(self, dog):
        dog.dlife = dog.dlife - self.pattack
        print('{}攻击了狗{}，狗{}生命值减少{}'.format(self.pname, dog.dname, dog.dname, dog.dlife))


dog1 = Dog("雪宝", '田园狗', 50)
p1 = Pepoles("李四", 60)
dog1.dogattack(p1)
p1.pepoleattack(dog1)
#多继承
