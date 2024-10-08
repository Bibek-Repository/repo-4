# returning an iterator from a tuple

tuple1=("ram","shyam","hari")

myiter=iter(tuple1)
print(next(myiter))
print(next(myiter))
print(next(myiter))

# returning an iterator from the strings

a="apple"
myiter1=iter(a)
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

# for loop for iterating the iterables

b=("ram", "shyam", "hari")            # here b is the iterable(type:tuple)
for x in b:
    print(x)

c="python"
for x in c:
    print(x)

# creating an iterator

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass=MyNumbers()
myiter2=iter(myclass)

print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))

# Using for loop to iterate using iterator

class Mega:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

class1=Mega()
myiter3=iter(class1)

for x in myiter3:
    print(x)


        


