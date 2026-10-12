
# 1.is
# mutable- can change in original object(address)
#  -can not reuse
# immutable-can not change into original object(address)
#  -can reuse
#    - integer values are immutable



x=10
y=10
li1=[10,20]
li2=[10,20]

print(x is y)
print(id(x))
print(id(y))
print(li1 is li2)
print(id(li1))
print(id(li2))
# print(id(li1))
# print(id(li2))


# 2.is not
print(x is not y)


 