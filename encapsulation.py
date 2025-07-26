class Students  :
    def __init__(self,name,marks) :
        self.name = name 
        self.__marks = marks

    def show_details (self) :
        print(f"the name of the student is {self.name} and marks {self.__marks}") 

    def show_marks (self,password,code) :
        if password  == "admin123" and code == "88565" :
            print(f"Marks {self.__marks}")
        else :
            print("Access denied")
    def update_marks (self,password,code,new_mark) :
        if password == "admin123" and code == "865" :
         if new_mark > 0 and new_mark < 100 :
             self.__marks = new_mark 
             print("")         

s1 = Students("Darkyy",56)
s1.show_details()
s1.show_marks("admin123","865")


