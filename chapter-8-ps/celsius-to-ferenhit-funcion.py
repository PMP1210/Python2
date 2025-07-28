def tempurature_convert(celcius):
    farenhit=(celcius*9/5)+32
    return farenhit

val=input("Enter the temperature in Celcius: ")
print(f"Tempurature in Ferenhit is : {tempurature_convert(float(val))}")