# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


# Return keyword
def fun():
    S = 0

    for i in range(10):
        S += i
    return S


print(fun())


# Yield Keyword
def fun():
    S = 0

    for i in range(10):
        S += i
        yield S


for i in fun():
    print(i)
