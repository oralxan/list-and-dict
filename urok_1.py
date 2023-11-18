#2
'''def aaa(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:   
            count += 1    
    return count
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = aaa(my_list)
print("Количество четных чисел:", even_count)'''
#1
'''def aaa(numbers):
    count = 0
    for num in numbers:
        count += num 
    return count
my_list = [1, 2]
even_count = aaa(my_list)
print(even_count)'''
#19
a = {"a": 1, "b": 2, "c": 3}
b = a.pop("b")
print(b)
#18
a={'c':1}
b={'b':2}
a.update(b)
print(a)

#4
'''a=[1,4,4,8,8,77,4]
print(set(a))'''
#6
'''a=[1,2]
b=[8,9]
a.extend(b)
print(a)'''
#7
a=[0,1,2,2,6,7]
a.sort()
print(a)

#8
'''a = [15, 11, 13, 12, 14, 10] 
b =list(reversed(a))

print(b)'''
#homework
#11
'''c={'cat','dog','c'}
b={'c','dog','c'}
print(list(c.intersection(b)))'''
#3
'''a=[5,2,3]
c=max(a)
print(c)'''
#13
'''c = {'a': 1, 'b': 2, 'c': 3}

if 'a' in c:
    print(1)
elif 'd'in c:
    print(0)'''
#14
'''a = {'a': 2, 'b': 3, 'c': 4}
c = int(input('c='))

for key in a:
    a[key] *= c

print(a)'''
#15
'''a={'a':1,'b':2}
print(list(a.keys()))'''
#16
'''a={'a':1,'b':2}
print(list(a.values()))'''
#17?
#20
'''a=[5,4,2]
b=len(a)
print(b)'''
#12
'''a={'a':1,'b':2}
c=sum((a.values()))
print(c)'''




