ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
INTEGER = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

def roman_decoder(string):
    if string.isdigit():            # Decimal ==> Roman
        string = int(string)
        result = ""
        for value, symbol in INTEGER.items():
            while string >= value:
                result += symbol
                string -= value
        return result
    else:                           # Roman ==> Decimal
        string = string.split('/')
        result = ""
        for item in string:
            decimal = 0
            for i in range(len(item)):
                if i > 0 and ROMAN[item[i]] > ROMAN[item[i-1]]:
                    decimal += ROMAN[item[i]] - 2 * ROMAN[item[i-1]]
                else:
                    decimal += ROMAN[item[i]]

            result += str(decimal) + '/'
        return result

print(f'{roman_decoder("1100")} since {roman_decoder("V/III/MCMLXXXV")}')