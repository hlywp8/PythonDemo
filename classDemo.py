class Person:
    count=0
    __test=2
    class P1:
        p1name='p1'
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        Person.count+=1
        print(self.name)
        print('person = '+str(Person.count))
        print('self = '+str(self.count))
    def getTest(self):
        return  self.__test
    @classmethod
    def classM(self):
        print('classmethod')
    @staticmethod
    def staticM():
        print('staticmethod')
class Chinese(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age=age
    def getAge(self):
        print('age is '+str(self.age))
Person.staticM()

p1=Person('tom')
p4=p1.P1()
print(p4.p1name)
p1.count=11111111111
p1.sayHi()



p2=Person('jerry')
p2.count=222222222222
p2.sayHi()

p3=Chinese('lily',23)
p3.count=333333333333
p3.sayHi()
p3.getAge()




