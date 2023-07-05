# Define conversion rates
unit_dict = {
    "inches": {
        "inches": 1,
        "centimeters": 2.54,
        "feet": 0.0833333,
        "yards": 0.0277778,
        "miles": 0.000015783
    },
    "centimeters": {
        "inches": 0.393701,
        "centimeters": 1,
        "feet": 0.0328084,
        "yards": 0.0109361,
        "miles": 0.0000062137
    },
    "feet": {
        "inches": 12,
        "centimeters": 30.48,
        "feet": 1,
        "yards": 0.333333,
        "miles": 0.000189394
    },
    "yards": {
        "inches": 36,
        "centimeters": 91.44,
        "feet": 3,
        "yards": 1,
        "miles": 0.000568182
    },
    "miles": {
        "inches": 63360,
        "centimeters": 160934,
        "feet": 5280,
        "yards": 1760,
        "miles": 1
    },
    "meters": {
        "meters": 1,
        "kilometers": 0.001,
        "feet": 3.28084,
        "yards": 1.09361
    },
    "kilometers": {
        "meters": 1000,
        "kilometers": 1,
        "feet": 3280.84,
        "yards": 1093.61
    },
    "milliliters": {
        "milliliters": 1,
        "liters": 0.001,
        "gallons": 0.000264172
    },
    "liters": {
        "milliliters": 1000,
        "liters": 1,
        "gallons": 0.264172
    },
    "gallons": {
        "milliliters": 3785.41,
        "liters": 3.78541,
        "gallons": 1
    }
}

# User input
unit_in = input("Enter the unit to convert from: ")
value = float(input("Enter the value: "))
unit_out = input("Enter the unit to convert to: ")

# Perform conversion
converted_value = value * unit_dict[unit_in][unit_out]

# Display result
print(f"{value} {unit_in} is equal to {converted_value} {unit_out}")
