# # a="softwarica"

# # print(a.upper())



# # a="@@PYTHON"

# # print(a.isupper())



# # a="@@PYTHON"

# # print("a".isupper())



# # a="capital"

# # print("A".isupper())



# # a="capital"

# # print("a")



# # a="capital"

# # print("nischay".capitalize("c"))



# # a="    capital"

# # print(a.isalnum())



# # a="capital"

# # print(a.isalnum())



# # a="1Capital"

# # print(a.zfill(9))



# # a="+Capital"

# # print(a.zfill(9))



# # a="-Capital"

# # print(a.zfill(9))



# # a="$Capital"

# # print(a.zfill(9))



# # a="$Capital"

# # print(a.zfill(9,"*"))



# # a="$Capital"

# # print(a.center(9,"**"))



# # a="$Capital"

# # print(a.center(9,"*"))



# # a="+Capital"

# # print(a.center(9,"*"))



# # a="+Capital9"

# # print(a.count("a"))



# a="+Cap9ital9"

# print(a.find("9"))



# # a="+Cap9ital9"

# # print(a.rfind("9"))



# # a="+Cap9ital9"

# # print(a.find("A"))



# # # a="+Cap9ital9"

# # # print(a.index("A"))



# # a="Cap9"

# # print(a.isdigit())



# # a="pythON9"

# # print(a.swapcase())



# # a="\t"

# # print(a.isspace())



a="/t"

print(a.isprintable())



# # a="123abc"

# # print(a.isalpha())



# # a="123abc"

# # print(a.rjust(11,"#"))



# # a="123abc"

# # print(a.ljust(11,"#"))



# # a="123abc"

# # print(a.ljust(6,"#"))



# # fo="123abc"

# # print(fo.ljust(6,"#"))



a="123abc"
print(a,"b")
print(a.replace('a','1'))



# # a="123abc"

# # b=a.count("c")

# # print(b)



# # a="123abc"

# # b=a.maketrans("123","abc")


# # print(a.translate(b))



# # a="123abc"

# # b=a.maketrans("123","abc")

# # print(b)



# # a="123abc"

# # b=a.maketrans("A","a")

# # print(b)



# # a="123abc"

# # b=a.maketrans("ab","A")

# # print(b)



# # a="123abc "

# # b=a.endswith(" ")
# # print(b)
# # print(a)



# # a="123abc"

# # b=a.endswith("abc")

# # print(a)



# # a="123abc"

# # b=a.endswith("c")

# # print(a)



# # a="123abc"

# # print(a.replace('a',"1"))


# # # #set
# a={1,2,9,4,5,900,8}
# a.add(7)
# # # print(a)
# b={4,5,6}
# c={1,2,9,4,5,900}
# # # # print(a)

# # # # print(a)
# # # # # c=a.union(b)
# # # # a.update(b)
# # # # # d=a.intersection(b)
# # # # a.clear()
# # # # # print(a,c,d)
# # # # # print(a.difference(b))

# print(a.update(b))
# # a.remove(9000)
# a.discard(9000)
# a.pop()
# print(a)
# # d=a.clear()
# # print(a.clear())
# # print(a)
# # print(d)
# # print(a.issuperset(c))
# # print(a.issubset(c))


#Dictionary
a={'a':1 , 'b':2,'d':6,'a':5}
b={'e':4,'a':'9'}

# print(a)
# a.update(b)
a['c']=8
print(a)
a.setdefault('c',4)
# # # del a['a']
# # # a.clear()
# print(a)

print(a)
a.pop('a')
# # c=a.popitem()
print(a)
# # print(a)

# print(a.get('a'))

# c=a.get('e',"key not available")
# print(c)
# # # print(a['a'])
# # print(min(max((2,3,4),4)),"hello")

# # #list
# a=[1,2,3,5]
# a.append((1,2))
# print(a)
# a.extend((4,5,6))
# print(a)
# # # # # a.insert(1,"ram")

# # # # print(a)

# # for i in range(1,11):
# #     if i==12:
# #         continue
# #     print(i)
# #     i=i+1
# # else:
# #      print("this is inside else of for loop")


# # S = 'Hello, World!'
# # x = S.swapcase()
# # print(x)

# c=['1','2','3','4','5']
# c.pop()
# print(c)
# # print(c)
# # print(isinstance(c,int))

# # # del a[len(a)-1]
# # # print(a)

# # # a.clear()
# # # print(a)

# # # b=a.copy()
# # # b.remove(6)
# # # print(b)
# # # b=(1,2,3,4,[5,6,7])
# # # print(b[4].pop())
# # # print(b)
# # # print([1,2]+[1,2])
# # # n={1,2,3,4}
# # # n.add(4,6)
# # # print(n)

# # # print(f'hello\rpyt' )
# # # print('hello'=='hello')

# # # print('Hello Python'.capitalize())

# # S = 'The World is Beautiful'
# # x = S.split()
# # print(x)

# # S = '  The    World is  Beautiful'
# # x = S.split()
# # print(x)

# # S = 'The\n\rWorld\tis Beautiful'
# # x = S.split()
# # print(x)

# # S = 'red,green,blue'
# # x = S.split(',')
# # print(x)

# # S = 'the beginning is the end is the beginning'
# # x = S.split(' is ',1)
# # print(x)

# # S = 'The\rWorld is Beautiful'
# # x = S.split(None,1)
# # print(x)

# # S = 'The World is Beautiful'
# # x = S.split(None,2)
# # print(x)

# S = '''First line\nSecond line\n
# nischay
# Third Line\tFourthline'''
# x = S.splitlines()
# print(x)


# # S='is my FAVOURITE number.'
# # x = S.capitalize()
# # print(x)

# # S = 'bob is a CEO at ABC.'
# # x = S.capitalize()
# # print(x)

# # S = 'Centered'
# # x = S.center(14, '*')
# # print(x)


# # S = '{1} is {0} years old.'.format(25, 'Bob')
# # print(S)

# # S = 'Long, Longer, Longest'
# # x = S.replace('Long','Small', 2)
# # print(x)

# # S = {'red', 'green', 'blue'}
# # S.add('yellow')
# # print(S)
# # # S = {'red', 'green', 'blue'}
# # # S.add([1, 2])
# # # print(S)

# # list=[['a','b','c'],[3,2,1]]
# # print(list[0])


# # a={'1':2,2:3}
# # a['1']=4
# # print(a)

# # a={1,2,3,4}
# # a=[1,2,3]
# # a.discard(5)

# # list=[3,4,2,1]
# # print(list[0:5])


# # a=5
# # b=2
# # x=a>b and not(a==b)
# # y=a ** 3
# # z=a/b
# # t=1,2,3,4
# # print(x,y,z)
# # print(type(x),type(y),type(z))

def my_function(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

# Example calls to the function
my_function(1, 2, 3, name="Alice", age=30)