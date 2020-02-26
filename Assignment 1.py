# Jai Sriram!

#Task 1.2
def num():
    a=range(2000,3201)
    b=[]
    for i in a:
        if i%7==0 and i%5==0:
            b.append(str(i))
    print(b)
num()
        
#Task 1.3

def name():
    name=input("Enter your first name and last name\n")
    Reverse_Name= print("Reverse of", name, "is:",name[::-1])
    return Reverse_Name
name()

#Task 1.4

def volume():
    r = int(input("Enter diameter in cm\n"))
    π = 3.14
    volume = round((4/3) * (π) * (r**3),2)
    return volume
volume()

#Task 2.1

def numberlist():
    a=input("Enter numbers separated by ,\n")
    a=[a]
    return a
numberlist()

#Task 2.2

def star():
    i=0
    a=5
    c="*"
    while i<a:
        print(i*(c))
        i=i+1
    else:
        while a>=0:
            print(a*(c))
            a=a-1
star()     

#Task 2.3

def word():
    word=input("Enter any word\n")
    Reverse_word= print("Reverse of", word, "is:",word[::-1])
    return Reverse_word
word()

# Task 2.4
print ("WE, THE PEOPLE OF INDIA, !")
print ('\t' * 1 + "having solemnly resolved to constitute India into a SOVEREIGN")
print ('\t' * 2 + "SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC")
print ('\t' * 2 + " and to secure to all its citizens")
#or single line code
print ("WE, THE PEOPLE OF INDIA, !\n",'\t' * 1 + "having solemnly resolved to constitute India into a SOVEREIGN\n",'\t' * 2 + "SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n",'\t' * 2 + " and to secure to all its citizens")

