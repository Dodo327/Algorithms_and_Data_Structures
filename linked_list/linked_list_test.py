from linked_list import LinkedList

L1 = LinkedList()
print(L1)

L1.pushFront(1)
L1.pushBack(2)
L1.pushFront(3)
print(L1)

L2 = LinkedList()
L2.insert(10, 0)
L2.pushBack(20)
L2.pushFront(30)
L2.insert(40, 3)
print(L2)
print(L2.size())

print(L1.search(10))
print(L1.search(1))
print(L2.front().value)
print(L2.rear().value)

# L1.joinRear(L2)
# print(L1)
# L1.joinFront(L2)
# print(L1)


print(L1.popFront().value)
print(L1)
print(L2)
print(L2.popBack().value)
print(L2.popIndex(2).value)

print(L1)
# L3 = L1.backwards()
# print(L3)
# print(L3.backwards())