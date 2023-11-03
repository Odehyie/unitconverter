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
        "miles": 0.000189394,
        "meters": 0.3048
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
        "yards": 1093.61,
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
    },
    "speed": {
        "mile_per_hour": 1,
        "knots": 0.539957,
        "meter_per_second": 3.6,
        "km_per_hour": 1.60934,
        "speed": 1
    },
    "mile_per_hour": {
        "mile_per_hour": 1,
        "knots": 0.539957,
        "meter_per_second": 3.6,
        "km_per_hour": 1.60934,
        "speed": 1
    },
    "knots": {
        "mile_per_hour": 0.539957,
        "knots": 1,
        "meter_per_second": 5.14444,
        "km_per_hour": 0.539957,
        "speed": 1
    },
    "meter_per_second": {
        "mile_per_hour": 3.6,
        "knots": 5.14444,
        "meter_per_second": 1,
        "km_per_hour": 3.6,
        "speed": 1
    },
    "km_per_hour": {
        "mile_per_hour": 0.621371,
        "knots": 0.539957,
        "meter_per_second": 3.6 / 1.60934,
        "km_per_hour": 1,
        "speed": 1
    },
    "mass": {
        "grams": 1,
        "ounces": 0.035274,
        "pounds": 0.00220462,
        "stones": 0.00157473,
        "metric_tons": 0.001,
        "uk_tonnes": 0.000011024,
        "us_tonnes": 0.0000098421,
        "mass": 1
    },
    "grams": {
        "grams": 1,
        "ounces": 0.035274,
        "pounds": 0.00220462,
        "stones": 0.00157473,
        "metric_tons": 0.001,
        "uk_tonnes": 0.000011024,
        "us_tonnes": 0.0000098421,
        "mass": 1
    },
    "ounces": {
        "grams": 28.3495,
        "ounces": 1,
        "pounds": 0.0625,
        "stones": 0.00714286,
        "metric_tons": 0.0000220462,
        "uk_tonnes": 0.00000283495,
        "us_tonnes": 0.00000220462,
        "mass": 1
    },
    "pounds": {
        "grams": 453.592,
        "ounces": 16,
        "pounds": 1,
        "stones": 0.157473,
        "metric_tons": 0.000453592,
        "uk_tonnes": 0.0000453592,
        "us_tonnes": 0.0000446429,
        "mass": 1
    },
    "stones": {
        "grams": 6350.293,
        "ounces": 224.062,
        "pounds": 14,
        "stones": 1,
        "metric_tons": 0.0006350293,
        "uk_tonnes": 0.00006350293,
        "us_tonnes": 0.0000623282,
        "mass": 1
    },
    "metric_tons": {
        "grams": 907.185,
        "ounces": 32.000,
        "pounds": 10,
        "stones": 0.11024,
        "metric_tons": 1,
        "uk_tonnes": 0.0000907185,
        "us_tonnes": 0.0000907185,
        "mass": 1
    },
    "uk_tonnes": {
        "grams": 1016.05,
        "ounces": 32.000,
        "pounds": 10,
        "stones": 0.11024,
        "metric_tons": 0.000907185,
        "uk_tonnes": 1,
        "us_tonnes": 0.000907185,
        "mass": 1
    },
    "us_tonnes": {
        "grams": 907.185,
        "ounces": 32.000,
        "pounds": 10,
        "stones": 0.11024,
        "metric_tons": 0.000907185,
        "uk_tonnes": 0.000907185,
        "us_tonnes": 1,
        "mass": 1
    },
    "temperature": {
        "celsius": 1,
        "fahrenheit": -17.77777,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 1,
        "tempFahrenheit": -17.77777,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 1
    },
    "celsius": {
        "celsius": 1,
        "fahrenheit": -17.77777,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 1,
        "tempFahrenheit": -17.77777,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 1
    },
    "fahrenheit": {
        "celsius": -17.77777,
        "fahrenheit": 32,
        "kelvin": 255.372,
        "rankine": 459.67,
        "tempCelsius": -17.77777,
        "tempFahrenheit": 32,
        "tempKelvin": 255.372,
        "tempRankine": 459.67,
        "temperature": 32
    },
    "kelvin": {
        "celsius": 273.15,
        "fahrenheit": 32,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 273.15,
        "tempFahrenheit": 32,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 273.15
    },
    "rankine": {
        "celsius": 273.15,
        "fahrenheit": 32,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 273.15,
        "tempFahrenheit": 32,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 459.67
    },
    "tempCelsius": {
        "celsius": 1,
        "fahrenheit": -17.77777,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 1,
        "tempFahrenheit": -17.77777,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 1
    },
    "tempFahrenheit": {
        "celsius": -17.77777,
        "fahrenheit": 32,
        "kelvin": 255.372,
        "rankine": 459.67,
        "tempCelsius": -17.77777,
        "tempFahrenheit": 32,
        "tempKelvin": 255.372,
        "tempRankine": 459.67,
        "temperature": 32
    },
    "tempKelvin": {
        "celsius": 273.15,
        "fahrenheit": 32,
        "kelvin": 273.15,
        "rankine": 459.67,
        "tempCelsius": 273.15,
        "tempFahrenheit": 32,
        "tempKelvin": 273.15,
        "tempRankine": 459.67,
        "temperature": 273.15
    },
    "tempRankine": {
        "celsius": 0,
        "fahrenheit": -459.67,
        "kelvin": 0,
        "rankine": 459.67,
        "tempCelsius": 0,
        "tempFahrenheit": -459.67,
        "tempKelvin": 0,
        "tempRankine": 459.67,
        "temperature": 459.67
    },
    "pressure": {
        "atm": 1,
        "bar": 1e-5,
        "torr": 1.33322e-5,
        "mmhg": 133.322,
        "inHG": 33.86389,
        "pa": 1,
        "psi": 0.000145038,
        "kPa": 0.001,
        "MPa": 0.001,
        "GPa": 0.001,
        "kgf/cm^2": 1e-5,
        "lbf/ft^2": 0.000145038,
        "pressure": 1
    },
    "kilograms": {
        "grams": 1000,
        "milligrams": 1e+6,
        "tonnes": 0.001,
        "metric tons": 0.001,
        "pounds": 2.20462,
        "ounces": 35.274,
        "stones": 0.157473,
        "UK short tons": 0.000561685,
        "US short tons": 0.000561685,
        "imperial tons": 0.000561685,
        "cubic meters": 1e-3,
        "liters": 1e-3,
        "UK gallons": 0.000219728,
        "US gallons": 0.000211338,
        "quarts": 0.000479018,
        "pints": 0.000946353,
        "fluid ounces": 0.00125224,
        "cup": 0.00236592,
        "tablespoon": 0.000027752,
        "teaspoon": 0.0000005,
        "weight": 1000
    },
    "weight": {
        "mass": 1,
        "grains": 14.5939,
        "dry metric ton (uk)": 0.001,
        "dry long ton (uk)": 0.001,
        "wet metric ton (uk)": 0.001,
        "wet long ton (uk)": 0.001,
        "short hundredweight (us)": 0.001,
        "long hundredweight (us)": 0.001,
        "stone (us)": 0.157473,
        "dry us ton": 0.001,
        "wet us ton": 0.001,
        "troy oz": 0.00283495,
        "carat": 0.0002,
        "pennyweights": 0.0000453592,
        "drachms": 0.000177185,
        "scruples": 0.000061524,
        "minims": 0.000011674,
        "gills": 0.000001592,
        "fluids dram": 0.000000196,
        "handfuls": 0.000022046,
        "bushels": 0.000453592,
        "barrels": 0.000453592,
        "firkin": 0.000453592,
        "hogshead": 0.000453592,
        "knotts": 0.00000002,
        "pecks": 0.00000002,
        "cord": 0.00000002,
        "chains": 0.00000002,
        "links": 0.00000002,
        "bars": 0.00000002,
        "quarters": 0.00000002,
        "dry quarters": 0.00000002,
        "dry cwt": 0.00000002,
        "wet quarters": 0.00000002,
        "wet cwt": 0.00000002,
        "tonne": 1,
        "metric tons": 1,
        "imperial tons": 1,
        "stones": 14,
        "coils": 144,
        "drums": 144,
        "cords": 144,
        "links": 144,
        "barrels (us)": 144,
        "cases": 144,
        "buttons": 144,
        "pounds per inch": 144,
        "feet": 144,
        "yards": 144,
        "miles": 144,
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
