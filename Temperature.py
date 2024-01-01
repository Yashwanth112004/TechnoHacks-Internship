while(1):
    print("----------------------------------------------------------------\n")
    print("In which temperature scale are you entering the temperature?: ")
    result=0
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    a=int(input("Enter your choice (1/2/3): "))
    if(a==1):
        t=float(input("Enter the temperature: "))
        print("Enter the scale from below to which the temperature should be converted: ")
        print("1. Fahrenheit")
        print("2. Kelvin")
        m=int(input("Enter your choice(1/2): "))
        if(m==1):
            result=t*(9/5)+32
            print("Temperature in Fahrenheit: ",result,"F")
        else:
            result=t+273.15
            print("Temperature in Kelvin: ",result,"K")
    if(a==2):
        t=float(input("Enter the temperature: "))
        print("Enter the scale from below to which the temperature should be converted: ")
        print("1. Celsius")
        print("2. Kelvin")
        m=int(input("Enter your choice(1/2): "))
        if(m==1):
            result=(t-32)*(5/9)
            print("Temperature in Celsius: ",result,"C")
        else:
            result=(t-32)*(5/9)+273.15
            print("Temperature in Kelvin: ",result,"K")
    if(a==3):
        t=float(input("Enter the temperature: "))
        print("Enter the scale from below to which the temperature should be converted: ")
        print("1. Celsius")
        print("2. Fahrenheit")
        m=int(input("Enter your choice(1/2): "))
        if(m==1):
            result=t-273.15
            print("Temperature in Celsius: ",result,"C")
        else:
            result=(t-273.15)*(9/5)+32
            print("Temperature in Fahrenheit: ",result,"F")
                