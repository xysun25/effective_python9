#-*-encoding:utf-8_*-
# 用“生成器表达式”改写数据量较大的列表推导
# 生成器表达式在运行时，不会把整个输出序列都呈现出来，会 估值为迭代器(iterator)，这个迭代器每次可以根据生成器
# 表达式产生一项数据
# 用法：把 列表推导的实现放在一对圆括号中，就构成了生成器表达式
# 对生成器表达式求值时，会立即返回一个迭代器，而不会深入处理文件中的内容

squares = [int(x)**2 for x in open('./my_file.txt')]
print (squares)

value = [len(x) for x in open('./my_file.txt')]
print (value)

it = (len(x) for x in open('./my_file.txt'))
print (it)
# 以刚才返回的迭代器为参数，逐次调用内置的next函数，next函数就向下进行了，对后面起作用，即可按照生成器表达式输出下一个值
print (next(it))
print (next(it))

roots = ((x,x**0.5) for x in it)
print (next(roots))