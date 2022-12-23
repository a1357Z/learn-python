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

    # taking input from the user

    # person = input("what s your name ?")
    # print("hello "+ person+ "  !!")

    # building a calculator

    # lists in python
    # people = ["ajay", "shrini", "ballu", 2, False]
    # for p in people:
    #     print(p)
    #
    # for i in range(0,4,1):
    #     print(people[i])

    # 2-d list
    # coord = [[1, 2], [3, 4]]
    # print(coord)

    # we can also use -ve indexing in list in python, the backward indexing starts from -1
    # print(people[-2])

    # accessing all the elements after some index
    # print(people[1:])

    # accessing some elements in a range not including the last position
    # print(people[1:3])

    # changing values at some index
    # people[4] = "brumma"

    # list functions
    # friends = ["ajay", "ankit", "himanshu", "banra", "ajay"]
    # moreFriends = ["ashish", "deepak"]

    # add the second list to the first list
    # friends.extend(moreFriends)
    # print(friends)

    # add an item to the end of the list
    # friends.append("chopra")
    # print(friends)

    # add an item at a position in the list
    # friends.insert(0,"malik")
    # print(friends)

    # remove an item from a list
    # friends.remove("ajay")
    # print(friends)

    # remove the last item from the list
    # friends.pop()  #think of it like a stack
    # print(friends)

    # check if an item exists in the list by getting its index
    # print(friends.index("ajay"))
    # print(friends.index("demon")) #this will give error as element not in the list

    # get the occurrences of an element in the list
    # print(friends.count("ajay"))

    # sorting the list
    # friends.sort()
    # print(friends)

    # reversing the list
    # friends.reverse()
    # print(friends)

    # create a copy of a list
    # friends2 = friends.copy();
    # print(friends2)

    # tuples are immutable, think of it like const in javascript
    # coordinates = (1, 2, 3, 4)
    # print(coordinates)
    # print(coordinates[-1]) # we can access the elements just like lists

    # we cannot change a value in a tuple, following line throws an error
    # coordinates[0] = 10

    # if else statements
    # isMale = True
    # if isMale:
    #     print("isMale")
    # else:
    #     print("is not Male")

    # dictionaries in python: using key value pairs
    # think of dictionaries as objects in javascript and maps in c++
    # myObject = {"name": "ajay", "age": 24}
    # print(myObject)
    # print(myObject["name"])
    # print(myObject.get("age", "not found"))
    # print(myObject.get("school", "not found"))
    #
    # myObject["school"] = "ira"

    # 2d lists
    # number_grid = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     0,
    #     ["ajay"]
    # ]

    # for item in number_grid:
    #     print(item)
    # print(number_grid[0][1])

    # nested for loop
    # for item in number_grid:
    #     if type(item) == list:
    #         for val in item:
    #             print(val)
    #     else:
    #         print(item)

    # error handling ( try, except )
    # try:
    #     val = 100 / 0  # the code breaks at this lint itself and goes into the except block
    #     num = int(input("enter a number"))
    #     print(num)
    # except ZeroDivisionError as err:
    #     print(err)
    # except ValueError:
    #     print("invalid input!! input must be a number")

    # reading a file in python

    # dataFile = open('./data.txt', 'r')
    # print(dataFile.readable())  # check if the file can be read
    # print(dataFile.readline())
    # for line in dataFile.readlines():
    #     print(line)
    # print(dataFile.read())
    # dataFile.close()

    # appending to a file
    # dataFile = open('data.txt', 'a')
    # dataFile.write("\nnext line")

    # writing to a file
    # dataFile = open('data.txt', 'w')
    # dataFile.write("\nA brand new file with new content.")

    # creating a file and writing to it
    dataFile = open('data1.txt', 'a')
    dataFile.write("\na new file created and content written on it.")


# creating a new function, note that function cannot be empty else we will get indentation error
def getWorkDone():
    print("work done")


def cube(inp):  # we don't need to specify the input type here
    return inp * inp * inp


# if statements with comparisons
def getMaxNumb(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def print_up_to(n):
    print("print_up_to")
    val = 1
    while val < n:
        print(val)
        val += 1


def exponentFunction(a, b):
    answer = 1
    while b > 0:
        answer *= a
        b -= 1
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # getWorkDone()
    # print(cube(3))
    # print(getMaxNumb(1, 2, 2))
    # print_up_to(10)
    # print(exponentFunction(2, 5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
