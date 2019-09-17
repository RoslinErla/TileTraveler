def starting_tile ():
    return print("You can travel: (N)orth.")

def tile_one_two ():
    return print("You can travel: (N)orth or (E)ast or (S)outh.")

def tile_one_three ():
    return print("You can travel: (E)ast or (S)outh.")

def tile_two_one ():
    return print("You can travel: (N)orth.")

def tile_two_two():
    return print("You can travel: (S)outh or (W)est.")

def tile_two_three():
    return print("You can travel: (E)ast or (W)est.")

def tile_three_one():
    return print("Victory!")

def tile_three_two():
    return print("You can travel: (N)orth or (S)outh.")

def tile_three_three():
    return print("You can travel: (S)outh or (W)est.")
location = 1.1

while location != 3.1:
    if location == 1.1:
        starting_tile()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "N":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        else:
            location = 1.2
    elif location == 1.2:
        tile_one_two()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "S" and direction != "N" and direction != "E":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "S":
            location = 1.1
        elif direction == "N":
            location = 1.3
        elif direction == "E":
            location = 2.2
    elif location == 1.3:
        tile_one_three()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "S" and direction != "E":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "S":
            location = 1.2
        elif direction == "E":
            location = 2.3
    elif location == 2.1:
        tile_two_one()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "N":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        else:
            location = 2.2
    elif location == 2.2:
        tile_two_two()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "S" and direction != "W":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "S":
            location = 2.1
        elif direction == "W":
            location = 1.2
    elif location == 2.3:
        tile_two_three()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "W" and direction != "E":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "W": 
            location = 1.3
        elif direction =="E":
            location = 3.3
    elif location == 3.2:
        tile_three_two()
        direction= input("Direction: ")
        direction = direction.upper()
        while direction != "N" and direction != "S":
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "N":
            location = 3.3
        elif direction == "S":
            location = 3.1
    elif location == 3.3:
        tile_three_three()
        direction = input("Direction: ")
        direction = direction.upper()
        while direction != "W" and direction != "S": 
            print("Not a valid direction!")
            direction= input("Direction: ")
            direction = direction.upper()
        if direction == "W":
            location = 2.3
        elif direction == "S":
            location = 3.2
else: 
    tile_three_one()