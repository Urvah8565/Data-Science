# class Students :
#     def __init__(self,name,marks,grade):
#         self.name = name
#         self.marks = marks
#         self.grade = grade

#     def show_details (self) :
#         print(f"Name = {self.name}, Marks = {self.marks}, Grade = {self.grade}")
#     @staticmethod
#     def rule () :
#         print("All students attends here ")

# s1 = Students("darkyy",[65],'A')
# s1.show_details()      
# s1.rule()

# s2 = Students("Leena",[56],'B')
# s2.show_details()    
# s1.rule()

class payments :
    
    
    def __init__ (self,name,check) :
         self.name = name 
         self.__check = check

    def payment (self) :
         print("you paid the amount.....")
    def check_pay (self) :
         print(f"You remaining amount is {self.__check} ")     
         print(self.__check)  # i can easily print this private class look CHATGPT
        
p1 = payments("Darkyy",56)
p1.payment()
# p1.__check()
p1.check_pay()

    