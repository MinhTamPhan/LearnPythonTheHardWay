## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a object
class Dog(Animal):

	def __init__(self, name):
		## set attribul name = name
		self.name = name

## Cat is-a object
class Cat(object):

	def __init__(self, name):
		## set name of Cat
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## set name of person
		self.name = name
		## Person has-a pet of some kind
		self.pet = None


## Employee is-a object
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hm what is this strage magic
		super(Employee, self).__init__(name)
		## set salary = salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a object
class Salmon(Fish):
	pass

## Hailibut is-a object
class Hailibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet is satan
mary.pet = satan

## frank is-a Employee has-salary is 120000
frank = Employee("Frank", 120000)

## frank has-a pet is rover and it is a Dog
frank.pet = rover

## flipper is-a fish()
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Hailibut()

print "Name: ", frank.name , "Pet: ",
print frank.pet.name ,"salary: ", frank.salary