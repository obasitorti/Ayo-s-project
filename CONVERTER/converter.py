import pyinputplus as pyip

print("Hello, Welcome to my converter program!")
category = pyip.inputChoice(['Length', 'Mass', 'Temperature', 'Currency'])
# Length conversions
if category == "Length":
    print("What unit are you converting from? ")
    length = pyip.inputChoice(['Centimeter', 'Meter', 'Inch'])

    # Centimeter coversions
    if length == 'Centimeter':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Meter', 'Inch'])
        if converter == 'Meter':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 100
            print("{}m".format(num))
        if converter == 'Inch':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 2.54
            print("{}in".format(num))

    # Meter conversions
    if length == 'Meter':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Centimeter', 'Inch'])
        if converter == 'Centimeter':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 100
            print("{}cm".format(num))
        if converter == 'Inch':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 39.27
            print("{}in".format(num))

    # Inches conversions
    if length == 'Inch':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Centimeter', 'Meter'])
        if converter == 'Centimeter':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 2.54
            print("{}cm".format(num))
        if converter == 'Meter':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 39.27
            print("{}m".format(num))

# Mass conversion
if category == 'Mass':
    print("What unit are you converting from? ")
    mass = pyip.inputChoice(['Kilogram', 'Gram', 'Stone'])

    # Kilogram coversions
    if mass == 'Kilogram':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Gram', 'Stone'])
        if converter == 'Stone':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 6.35
            print("{}st".format(num))
        if converter == 'Gram':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 1000
            print("{}g".format(num))

    # Gram conversions
    if mass == 'Gram':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Kilogram', 'Stone'])
        if converter == 'Kilogram':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 1000
            print("{}kg".format(num))
        if converter == 'Stone':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 6350
            print("{}st".format(num))

    # Kilogram conversions
    if mass == 'Stone':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Kilogram', 'Gram'])
        if converter == 'Kilogram':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 6.35
            print("{}kg".format(num))
        if converter == 'Gram':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 6350
            print("{}g".format(num))

# Temperature conversion
if category == 'Temperature':
    print("What unit are you converting from? ")
    temperature = pyip.inputChoice(['Celsius', 'Fahrenheit', 'Kelvin'])

    # Celsius coversions
    if temperature == 'Celsius':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Fahrenheit', 'Kelvin'])
        if converter == 'Fahrenheit':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = (conversion * 9/5) + 32
            print("{}°F".format(num))
        if converter == 'Kelvin':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion + 100
            print("{}K".format(num))

    # Fahrenheit coversions
    if temperature == 'Fahrenheit':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Celsius', 'Kelvin'])
        if converter == 'Celsius':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = (conversion - 32) + 5/9
            print("{}°C".format(num))
        if converter == 'Kelvin':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = (conversion - 32) * 5/9 + 273.15
            print("{}K".format(num))
    
    # Kelvin coversions
    if temperature == 'Kelvin':
        print("What unit are you converting to?")
        converter = pyip.inputChoice(['Celsius', 'Fahrenheit'])
        if converter == 'Celsius':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion  - 273.15
            print("{}°C".format(num))
        if converter == 'Fahrenheit':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = (conversion - 273.15)* 9/5 + 32
            print("{}°F".format(num))

# Currency conversions
if category == "Length":
    print("What unit are you converting from? ")
    currency = pyip.inputChoice(['Dollars', 'Euros', 'Pounds'])

    # Centimeter coversions
    if currency == 'Dollars':
        print("What currency are you converting to?")
        converter = pyip.inputChoice(['Meter', 'Inch'])
        if converter == 'Euros':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion * 0.95
            print("{}€".format(num))
        if converter == 'Inch':
            conversion = pyip.inputNum(prompt='Enter number to be converted: ')
            num = conversion / 2.54
            print("{}in".format(num))
