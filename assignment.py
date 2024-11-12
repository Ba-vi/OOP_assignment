#oop=object oriented programming.
# here we mainly focus on working with key objects.
# we have classes and objects.
#classes always have properties.
#objects coe from class.
#an object takes on the properties of a class.

#creating classes  # A CLASS NAME STARTS WITH A CAPITAL LETTER AND SINGULAR.
#cohort class
# class Cohort:
# Name
# description
# start_date
# end_date

#Question 1
#add aconstructor for a cohort class,
class Cohort:
    def __init__(self, name , description, start_date, end_date):
        #we use the _init_ function to assign values for name,description,start date and end date.
        self.name = name
        self.description = description  # self is the instance of the class being created.
        self.start_date = start_date
        self.end_date = end_date
p1 =Cohort("Violah","student","11th/8/2024","24th/12/2026")
print(p1.name)
print(p1.description)
print(p1.start_date)
print(p1.end_date)

 
#question 2
#add a method to a class that prints a cohort name and the total number of students.
class Cohort_four:
    def __init__(self, cohort_name,total_number):
          self.cohort_name = cohort_name
          self.total_number = total_number
    def  print_Cohort_info(self) :
        print(f"cohort_name:{self.cohort_name} ")
        print(f"total_number:{self.total_number}")
p1=Cohort_four("WITU", 56)
p1.print_Cohort_info()  



#question 3
#create a new object/instance of the cohort class.

# Create a new cohort instance
class Cohort_two:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
    def display_info(self):
        print(f" Cohort name : {self.name}")
        print(f"Start date :{self.start_date}")
        print(f"end date : {self.end_date}")

p1=Cohort_two("Programmers", "2nd/8/2024","8th/12/2026")
p1.display_info()