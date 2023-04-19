################# Running this code require Python 3.10 or newer ##################
with open("d.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

# Create the keypad dictionary
keypad = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2),
}

# Follow the instructions and append button labels to a list and finally get the secret
curr_button = "5"
secret = ""
for instruction in instructions:
    for move in instruction:
        row, col = keypad[curr_button]
        match move:
            case "U": row -= 1
            case "D": row += 1
            case "L": col -= 1
            case "R": col += 1
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            curr_button = next(button for button, pos in keypad.items() if pos == (row, col))
    secret += curr_button

print("Secret: " + secret)
## Secret: 61475