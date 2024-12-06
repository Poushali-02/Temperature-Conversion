def convert(userInput, userOutput,t):#function in which the conversion is held
    if(userInput=="Celcius"):
        tempC=t
        tempF= (9 * tempC) / 5 + 32
        return tempF
    elif(userInput=="Farenheit"):
        tempF=t
        tempF=tempF-32
        tempC = (5/9) * tempF 
        return tempF
    else:
        return None
userInput=input("Change from Celcius Or Farenheit?") #asking user for scale
userOutput=input("Change to? ")
try:
    t=float(input("Enter temperature:")) #taking the input
except:
    print("please enter valid input-a temperature") #in case of wrong input
print("In ",userOutput," temperature is: ",convert(userInput, userOutput,t)) #printing the output

