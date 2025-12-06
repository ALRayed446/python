while True:
    print("What do you want to measure?")
    print("l for Length, a for Area, v for Volume, w for Weight")

    choice = input("Enter your choice: ").lower()

    if choice == "l":
        print("\nLength units: cm, inch, foot, meter, km, mile")
        value = float(input("What is the value of length? "))
        unit = input("Enter the unit: ").lower()

        # সবিকছু meter-এ রূপান্তর
        if unit == "cm":
            meter = value / 100
        elif unit == "inch":
            meter = value * 0.0254
        elif unit == "foot":
            meter = value * 0.3048
        elif unit == "km":
            meter = value * 1000
        elif unit == "mile":
            meter = value * 1609.34
        elif unit == "meter":
            meter = value
        else:
            print("Invalid unit.")
            exit()

        print("\nConverted values:")
        print(f"Centimeter: {meter * 100}")
        print(f"Inch: {meter / 0.0254}")
        print(f"Foot: {meter / 0.3048}")
        print(f"Meter: {meter}")
        print(f"Kilometer: {meter / 1000}")
        print(f"Mile: {meter / 1609.34}")

    elif choice == "a":
        print("\nArea units: sqm, sqkm, sqmile, acre, hectare, sqft")
        value = float(input("What is the value of area? "))
        unit = input("Enter the unit: ").lower()

        # সবিকছু sqm-এ রূপান্তর
        if unit == "sqm":
            sqm = value
        elif unit == "sqkm":
            sqm = value * 1_000_000
        elif unit == "sqmile":
            sqm = value * 2_589_988
        elif unit == "acre":
            sqm = value * 4046.86
        elif unit == "hectare":
            sqm = value * 10_000
        elif unit == "sqft":
            sqm = value * 0.092903
        else:
            print("Invalid unit.")
            exit()

        print("\nConverted values:")
        print(f"Square Meter: {sqm}")
        print(f"Square Kilometer: {sqm / 1_000_000}")
        print(f"Square Mile: {sqm / 2_589_988}")
        print(f"Acre: {sqm / 4046.86}")
        print(f"Hectare: {sqm / 10_000}")
        print(f"Square Foot: {sqm / 0.092903}")

    elif choice == "v":
        print("\nVolume units: liter, ml, cubicmeter, cubicfoot, gallon, pint")
        value = float(input("What is the value of volume? "))
        unit = input("Enter the unit: ").lower()

        # সবিকছু liter-এ রূপান্তর
        if unit == "liter":
            liter = value
        elif unit == "ml":
            liter = value / 1000
        elif unit == "cubicmeter":
            liter = value * 1000
        elif unit == "cubicfoot":
            liter = value * 28.3168
        elif unit == "gallon":
            liter = value * 3.78541
        elif unit == "pint":
            liter = value * 0.473176
        else:
            print("Invalid unit.")
            exit()

        print("\nConverted values:")
        print(f"Milliliter: {liter * 1000}")
        print(f"Liter: {liter}")
        print(f"Cubic Meter: {liter / 1000}")
        print(f"Cubic Foot: {liter / 28.3168}")
        print(f"Gallon: {liter / 3.78541}")
        print(f"Pint: {liter / 0.473176}")

    elif choice == "w":
        print("\nWeight units: gram, kg, mg, pound, ounce, ton")
        value = float(input("What is the value of weight? "))
        unit = input("Enter the unit: ").lower()

        # সবিকছু gram-এ রূপান্তর
        if unit == "gram":
            gram = value
        elif unit == "kg":
            gram = value * 1000
        elif unit == "mg":
            gram = value / 1000
        elif unit == "pound":
            gram = value * 453.592
        elif unit == "ounce":
            gram = value * 28.3495
        elif unit == "ton":
            gram = value * 1_000_000
        else:
            print("Invalid unit.")
            exit()

        print("\nConverted values:")
        print(f"Milligram: {gram * 1000}")
        print(f"Gram: {gram}")
        print(f"Kilogram: {gram / 1000}")
        print(f"Pound: {gram / 453.592}")
        print(f"Ounce: {gram / 28.3495}")
        print(f"Ton: {gram / 1_000_000}")

    else:
        print("Invalid choice.")