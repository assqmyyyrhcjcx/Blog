from collections import Iterable
from functools import reduce
import os

print("hello", "world")

#转义
print('\\\t\\')
#不转义
print(r'\\\t\\')

#显示多行内容
print('''line 
	line2 
	line3''')

#除法
#一个'/'得到的结果是一个浮点数
print(10 / 3)

print(9 / 3)

#取整
#两个'//'得到的结果是整数
print(10 // 3)

#取余
print(10 % 3)

#字符编码
print('包含中文的String')

print(ord('A'))

print(ord('中'))

print(chr(65))

#格式化输出
print('%4d' % 300)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#另一种格式化输出
print('hello {0} me, {1} is you'.format('is', "world"))

classmates = ["Rose", "Jack"]
print(classmates)
print(len(classmates))
#取最后一个元素，除了使用最后一个下标，还可以使用-1
print(classmates[-1])
#以此类推，倒数第二个-2
print(classmates[-2])

#在list尾部添加元素
classmates.append('Henry')
print(classmates)

#在指定下标插入元素，指定下标之后的元素往后退
classmates.insert(1, 'Jakson')
print(classmates)

#删除指定下标的元素
classmates.pop(1)
print(classmates)

#list中的数据类型可以不相同
dataList = [True, 'money', 123456]
print(dataList)

#tuple和list非常类似，但是tuple一旦初始化就不能修改,它也没有append()，insert()，pop()这样的方法
color = ('red', 'green', 'black')
print(color)

#条件判断
age = input('Please input your age: ')
#输入的是字符串，需要转换为int类型
age = int(age)
if age >= 18:
	print('The guy is adult')
elif age >= 3:
	print('The guy is kid')
else :
	print('The guy is baby')

#循环
for item in color:
	print(item)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	sum += x
print(sum)

#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
#左开右闭，从0到5，不包含下标为5
print(list(range(5)))

#range()表示从起始下标到结尾下标的整数
for x in range(1,10):
	print(x)

#dict 也就是 map
userInfo = {'Jack': 24, 'Rose': 23, "Tom": 28, "Jerry": 25}
#添加key-value
userInfo['Ada'] = 23
print(userInfo)
print('Jack', userInfo['Jack'])

#使用get获取map中的数据，如果没有此key，输出none，使用上面[]的形式获取value会报错
print('Joice', userInfo.get('Joice'))
#如果没有此key，输出填写的value，如果有，输出dict中的value
print('Albert', userInfo.get('Albert', 43))
print('Rose', userInfo.get('Rose', 43))
print(userInfo)
#删除key，使用pop()
print(userInfo.pop("Ada"))

#set中的key不重复,list是直接使用[],touple是使用()，dict是使用{}，set使用set([])
s = set([1, 2, 3])
print(s)
#使用add方法添加元素
s.add(3)
s.add(4)
print(s)
#使用remove方法删除元素
s.remove(4)
print(s)

s2 = set([2, 3, 4])
print('s&s2:', s&s2)
print('s|s2:', s|s2)

#函数
print(abs(-200))
print(max(1, 2))

#函数名其实就是指向函数对象的引用，可以把函数名赋值给一个变量，相当于给这个函数起了一个别名
absolute = abs
print(absolute(-1))

#定义一个函数使用def声明，依次写出函数名和形参
def addAll(n):
	sum = 0
	for x in range(n + 1):
		sum += x
	return sum

print(addAll(10))

#空函数,pass语句什么都不做，pass可用来作为占位符
def nop():
	pass

nop()

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(10))
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
#print(my_abs('A'))

#函数返回多个结果
def getUserInfo(name):
	username = name
	userage = userInfo.get(name)
	return username, userage

name, age = getUserInfo('Jack')
print(name, age)

#返回值是一个tuple
print(getUserInfo('Rose'))

#定义一个函数，用来实现以x为底，y为指数的数学运算,可以直接在形参中设置默认参数的值
#注意：默认参数必须指向不变对象，可以是list数据[]，不可以是list之类的变量name=[]！
def power(x, y = 1):
	result = 1
	while y >= 1:
		result *= x
		y = y - 1
	return result

print(power(2, 3))
#默认的参数可以不填
print(power(3))

#不可变参数
def calc(numbers):
	sum = 0
	for x in numbers:
		sum += x
	return sum

print('不可变参数', calc([1, 2]))

#可变参数 在形参前添加*
def calc2(*numbers):
	print(numbers)
	sum = 0
	for x in numbers:
		sum += x
	return sum

print('可变参数', calc2(1, 2))
nums = [1, 2, 3]
nums2 = (1, 2, 3)
#在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
print('可变参数', calc2(*nums))
print('可变参数', calc2(*nums2))

#关键字 在形参前添加**
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **other):
	print('name:', name, 'age:', age, 'other:', other)

person('Mary', 32)
person('Jeffery', 33, gender='Man', tel='110')

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**other参数，
#other将获得一个dict，注意other获得的dict是extra的一份拷贝，对other的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, tel):
	print(name, age, city, tel)

person2('Joice', 23, city='shanghai', tel='120')
#只接收city和job作为关键字参数
#person2('Joice', 23, city='shanghai', phone='120')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#例如：def person(name, age, *args, city, tel)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

#最神奇的是通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args1 = (1, 2, 3)
f1(*args1, **kw)
#a = 1 b = 2 c = 3 args = () kw = {'d': 99, 'x': '#'}
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

#尾递归
#尾递归是指，在函数返回的时候，调用自身本身，
#并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#非尾递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print('递归', fact(10))

#尾递归
def fact_tail(num):
	return fact_iter(num, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print('尾递归', fact_tail(10))
#大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
#所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出

#切片
Letter = ['A', 'B', 'C', 'D', 'E']
#从下标为0到下标为3,[0,3),左闭右开
print(Letter[0 : 3])
#第一索引为0，可以省略
print(Letter[: 3])
#-1为倒数第一个
print(Letter[-1])
#同理，省略不写，会遍历到最后一个索引
print(Letter[-2 : ])

#range表示从0开始的一百个数，也就是0-99
numerals = list(range(100))
print(numerals)

#从0开始，每隔一个数输出一个数，范围0-9
print(numerals[: 10 : 2])
#每隔五个取一个
print(numerals[: : 5])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEF'[: 3])

#迭代
#只要是可迭代对象，无论有无下标，都可以迭代
#迭代list
for x in Letter:
	print(x)

#迭代dict
for x in userInfo:
	print(x, ':', userInfo.get(x))

#默认情况下，dict迭代的是key。
#如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
for value in userInfo.values():
	print(value)

for k, v in userInfo.items():
	print(k, ':', v)

#判断是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(Letter):
	print('下标索引为', i, '的值为', value)

for x, y in [(1, 2), (3, 4), (5, 6)]:
	print(x, y)

#列表生成式 list,所以是[]
#把要生成的元素x * x放到前面，后面跟for循环
print([x * x for x in [1, 2, 3, 4, 5]])
print([x / 2 for x in [1, 2, 3, 4, 5]])
#for循环后面还可以加上if判断
print([x * 2 for x in [1, 2,3, 4, 5] if x % 2 != 0])
#还可以使用两层循环，生成全排列
print([x + y for x in ['A', 'B', 'C'] for y in ['X', 'Y', 'Z']])

#使用os来获取目录
print([dir for dir in os.listdir('.')])
#使用lower()将字母小写
print([s.lower() for s in Letter])

#生成器 ()
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的
#所以，如果列表元素可以按照某种算法推算出来，
#那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间
g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#也可以使用迭代的方式输出
#注意：上面使用了多个next，游标不会重新归位的，所以for循环遍历还是从之前游标停留的位置开始
for x in g:
	print(x)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
for x in o:
	print(x)

#使用生成器实现杨辉三角
def triangles(n):
    a, b = [0], [1]
    while n > 0:
        yield b
        c = [a[n] + b[n] for n in range(0, len(a))]
        a, b = [0] + c, c + [1]
        n = n - 1
	

t = triangles(10)
for x in t:
	print(x)

#传入函数
def add(x, y, func):
	return func(x) + func(y)

print('传入函数', add(1, -10, abs))

#map函数
#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x
#map()传入的第一个参数是f，即函数对象本身。
#由于结果是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(map(f, list(range(10)))))

#把这个list中的数字全部转换为字符
print(list(map(str, range(10))))

#reduce函数
def sum(x, y):
	return x + y
print(reduce(sum, list(range(5))))

def char2num(s):
	return int(s)
print(list(map(char2num, '13579')))
print(reduce(sum, map(char2num, '13579')))

#filter()
#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
	return x % 2 == 1
print(list(filter(is_odd, range(10))))

print(type(range(2)))
print(type(list(range(2))))

#sorted
#排序
print(sorted([23, 34, -12, 4, 9]))
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#排序应该忽略大小写，按照字母序排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#返回值
#如果不需要立刻求和，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3)
print(f())

#闭包
#返回的函数并没有立刻执行，而是直到调用了f()才执行
#等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print('f1:', f1(), 'f2:', f2(), 'f3:', f3())
#f1: 9 f2: 9 f3: 9

#用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count2():
	def f(j):
		return j * j

	fs = []
	for i in range(1, 4):
		fs.append(f(i))

	return fs

f4, f5, f6 = count2()
print('f4:', f4, 'f5:', f5, 'f6:', f6)
#f4: 1 f5: 4 f6: 9

#匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
print(list(map(lambda x : x * x, filter(is_odd, range(10)))))

f = lambda x : x * 2
print(f(5))


#装饰器
def now():
	print('2018-06')

f = now
f()

print(now.__name__)
print(f.__name__)