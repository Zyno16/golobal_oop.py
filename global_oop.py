x=0

class employee:
    
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0


    def change(self,num):
        global x
        x =num
        
        
    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())
emp =employee()
emp.change(6)
print(x)

