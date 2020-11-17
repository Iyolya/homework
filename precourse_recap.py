print ("Welcome to the guessing game!")
answer = input("Are you ready? ")

if answer == "yes":
   print("Let's start then!")

   answer = input("What year is it? ") 
   if answer == "2020":
      print ("Terrible, isn't it? Correct answer though!")  
   else:
      print (f"{answer}? Sorry pal, but it's not that year! ") 


   answer = input("In which city are we now? ") 
   if answer == "Edinburgh":
      print ("Beautiful city, right?")  
   else:
      print (f"I have some bad news, we are not in {answer} ")


   answer = input("Last one! Will it rain?(yes/no) ") 
   if answer == "yes":
      print ("Of course it will!")  
      print ("Thank you for playing, have a nice day!;)")
   else:
      print (f"{answer}? You're a hopeless optimist amigo! ")    
      print ("Thank you for playing, have a nice day!;)")   
else: 
  print("You will miss out on all the fun!:(")
