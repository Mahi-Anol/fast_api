
#Problem: age should be int, but parameter accepts string.
def test(name,age):
    print("name: ",name)
    print("age: ",age)

test("mahi","tweenty")


#solution:1
def test2(name:str,age:int):

    if type(name)!=str:
        raise TypeError("Name should be of str")
    if type(age)!=int:
        raise TypeError("Age should be of int")
    if age<0:
        raise ValueError("Age should be >=0")
    print(name,age)

test2("mahi",-1)