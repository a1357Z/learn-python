# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # for i in range(2, 20, 3):
    #     print(i)
    #

    # dealing with strings

    # name = "ajaY_Yadav"
    # print(name[2:])
    # print(name[:len(name) - 1])
    #
    # for i in range(0, len(name)-1, 1):
    #     print(name.replace("jaY", "jubbi"))

    # dealing with numbers

    # print(5 * 3)
    # print(str(5 * 3 / 5) + str(True) + str("ajay"))
    # print(abs(-10))
    # print(max(20, 30))
    # print(round(2.9))
    # print(round(2.1))
    # print(floor(2.9))
    # print(ceil(2.1))
    # print(sqrt(36))


    #taking input from the user

    # person = input("what s your name ?")
    # print("hello "+ person+ "  !!")

    #building a calculator

    #lists in python
    # people = ["ajay", "shrini", "ballu", 2, False]
    # for p in people:
    #     print(p)
    #
    # for i in range(0,4,1):
    #     print(people[i])

    #we can also use -ve indexing in list in python, the backward indexing starts from -1
    # print(people[-2])

    #accessing all the elements after some index
    # print(people[1:])

    #accessing some elements in a range not including the last position
    # print(people[1:3])

    #changing values at some index
    # people[4] = "brumma"

    #list functions
    friends = ["ajay", "ankit", "himanshu", "banra", "ajay"]
    moreFriends = ["ashish", "deepak"]

    #add the second list to the first list
    # friends.extend(moreFriends)
    # print(friends)

    #add an item to the end of the list
    # friends.append("chopra")
    # print(friends)

    #add an item at a position in the list
    # friends.insert(0,"malik")
    # print(friends)

    #remove an item from a list
    # friends.remove("ajay")
    # print(friends)

    #remove the last item from the list
    # friends.pop()  #think of it like a stack
    # print(friends)

    #check if an item exists in the list by getting its index
    # print(friends.index("ajay"))
    # print(friends.index("demon")) #this will give error as element not in the list

    #get the occurences of an element in the list
    # print(friends.count("ajay"))

    #sorting the list
    # friends.sort()
    # print(friends)

    #reversing the list
    # friends.reverse()
    # print(friends)

    #create a copy of a list
    friends2 = friends.copy();
    print(friends2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
