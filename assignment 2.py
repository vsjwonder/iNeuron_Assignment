# Jai Sri Krisna

# Task 1.1.1


def myreduce(x):
    a = 0
    for i in x:
        a = a + i
    return a


myreduce([1, 2, 3, 4])

# Actual function

import functools as fn
print(fn.reduce(lambda x, y: x+y, [1, 2, 3, 4]))

# Task 1.1.2


def myfilter(x):
    list1 = []
    list2 = []
    a = len(x)
    # print("length of input list =", a)
    for i in x:
        a = a-1
        # print('a =',a)
        if i >= 18:
           # print ("True")
           list1.append(i)
           if a == 0:
               # print("True condition represented by",list1)
               return list1
        else:
            # print ("False")
            list2.append(i)


adults = myfilter([18, 20, 25, 65, 12, 4, 19, 4, 3, 5, 20])
for i in adults:
    print(i)


def myfilter(x):
    for i in x:
        if i >= 18:
            yield i


adults = myfilter([18, 20, 25, 65, 12, 4, 19, 4, 3, 5, 20])
for i in adults:
    print(i)

# Actual function


def myFunc(x):
    if x >= 18:
        return True
    else:
        return False


ages = [18, 20, 25, 65, 12, 4, 19, 4, 3, 5, 20]
adults = filter(myFunc, ages)

for x in adults:
    print(x)


# Task 1.2.1

def list_comp1():
    word = "ACADGILD"
    list1 = [a for a in word]
    print(list1)


list_comp1()

# Task 1.2.2


def list_comp2():
    list2 = ['x', 'y', 'z']
    list2 = [a*b for a in list2 for b in range(1,5)]
    print(list2)


list_comp2()

# Task 1.2.3


def list_comp3():
    list3 = ['x', 'y', 'z']
    list3 = [a*b for b in range(1, 5) for a in list3]
    print(list3)


list_comp3()

# Task 1.2.4


def list_comp4():
    list4 = [2, 3, 4]
    list4 = [[a+b] for a in list4 for b in range(0, 3)]
    print(list4)


list_comp4()

# Task 1.2.5


def list_comp5():
    list5 = [2, 3, 4, 5]
    list5 = [[a+b for a in list5] for b in range(0, 4)]
    print(list5)


list_comp5()

# Task 1.2.6


def list_comp6():
    list6 = [1, 2, 3]
    list6 = [(b, a) for a in list6 for b in list6]
    print(list6)


list_comp6()

# Task 1.3.1


def longest_word(x):
    list7 = x
    list8 = []
    for i in list7:
        list8.append(len(i))
        list8.sort(reverse = True)
        b = len(list8)
    for a in list7:
        if len(a) == list8[0]:
            print("Longest word is", a)
        elif len(a) == list8[b-1]:
            print("Shortest word is", a)


longest_word(['vivek', 'rewansidha', 'shiwashankar', 'javalkote'])
# alternate


def longest_word():
    list7 = ['vivek', 'rewansidha', 'shiwashankar', 'javalkote']
    a = []
    a = len(max(list7, key=len))
    return ([b for b in list7 if len(b) == a])


longest_word()


# Task 2.1.1


class triangle_length():
    def __init__(self, length_a, length_b, length_c):
        self.length_a = length_a
        self.length_b = length_b
        self.length_c = length_c


    def area (self):
        s = (self.length_a + self.length_b + self.length_c) / 2
        print("semi perimeter is ", s)
        area = (s*(s-self.length_a)*(s-self.length_b)*(s-self.length_c))**0.5
        return area


class triangle_area(triangle_length):
    def __init__(self, length_a, length_b, length_c):
        triangle_length.__init__(self, length_a, length_b, length_c)


TrAr = triangle_area(4, 6, 7)
print("Area of triangle is ", TrAr.area())


# Task 2.1.2


def filterlongword1(listwords, length):
    filterwords = []
    for i in range(len(listwords)):
        if len(listwords[i]) > length:
            filterwords.append(listwords[i])
    return filterwords


def filterlongword():
    listwords = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    filterword1 = filterlongword1(listwords, length)
    filterword = ', '.join(filterword1)
    print("Words longer than {} are {}.".format(length, filterword))


filterlongword()

# Task 2.1.3


def countword1(listwords):
    countwords = []
    for i in listwords:
        print(i)
        countwords.append(len(i))
    return countwords


def countword():
    listwords = input("Enter words, separated by spaces: ").split()
    countword = countword1(listwords)
    print("Length of the each word are {}.".format(countword))


countword()

# Task 2.1.4


def vowel():
    alphabets = input("Enter letter ").split()
    vowellist = ['a', 'e', 'i', 'o', 'u']
    for i in alphabets:
        for v in vowellist:
            if i == v:
                print("Entered letter {} is vowel.".format(i))
                return True
            else:
                print("Entered letter {} is vowel.".format(i))
                return False


vowel()
