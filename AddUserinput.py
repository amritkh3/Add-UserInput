# 4.Write a program to enter the numbers till the user wants and at the end it should
#  display the sum of all the numbers entered(Bonus + in class).
"""
1.declare a variable with name sum and assign it with value 0
2.ask user if they want to inter any number .(answer must be in y/n)
3.use if condition when ui=y
4. use whie loop uner if confition 
    unless the ui =n
     ask user to input any number
5 ask user to if they want more nuber until they answer n
6.override the value of sum to sum+un
7.once the loop is stop print add which will be the sum of all the number entered by user"""


sum=0
ui=input("do you want to enter any number y/n ")
ui=ui.lower()#changing the user input to lowercase
if ui=="y":
    while ui!="n":#while loop run until userinput is "n"
        un=int(input("enter any number "))
        ui=input("do you want to enter any number y/n ")
        ui=ui.lower()
        sum=sum+un#adding the number evertime the user input
    

print("sum off all numbers is",sum)


   


    

     

   
   
      
      

     



