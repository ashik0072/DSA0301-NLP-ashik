print("The temperature in the room is 25 degree celsius")
temperature_celcius=25
print("The room tempertaure is : ",temperature_celcius)
word="temperature"
canonical_form=word.capitalize
print("The canonical form of the word is : ",canonical_form)
temp_in_celcius=25
temp_in_faren=(temp_in_celcius*(9/5))+32
def analyze_temperature(temp):
    if temp<0:
        return"it is freezing"
    elif 0<=temp<20:
        return "is is cool"
    else:
        return "it is warm"
temperature=25
analysis=analyze_temperature(temperature)
print("the temperature of",temperature,"degree celcius : ",analysis)
