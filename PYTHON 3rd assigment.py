import random
secret_number = random.randint(1, 10)
attempts=3
print("you have 3 attempts")

while attempts>0:
    guess_number=int(input("guess a number :"))
    
    if guess_number<1 or guess_number>10 :
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue
        
    elif guess_number==secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess_number>secret_number:
        attempts -=1
        print("Too high. Try again. ")
        
    elif guess_number<secret_number:
        attempts -=1
        print("Too low. Try again.")
            
else:
    print("Better luck next time!")
 








n=int(input("Enter the number for which you want the multiplication table:"))

for i in range(1,11):
    print(n,"*",i,"=",n*i)







def calculate_bmi(weight, height):
    BMI=weight/height**2
    return BMI

weight=float(input("Enter your weight in kg:"))
height=float(input( "Enter your height in meters:"))
a=calculate_bmi(weight,height)

print("Your BMI is:",round(a,2))           
              
