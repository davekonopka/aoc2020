import math

class BoardingPass:

    def __init__(self, binary):
        self.binary = binary

    def __str__(self):
        return self.binary

    def getSeatId(self):
        pos = 0
        lower = 0
        upper = 127
        row = -1
        col = -1
        for letter in self.binary:
            seat = -1
            if pos < 6 or (pos > 6 and pos < 9):
                middle = (upper + lower) / 2
                if letter == "F" or letter == "L":
                    upper = math.floor(middle)
                elif letter == "B" or letter == "R":
                    lower = math.ceil(middle)
            elif pos == 6:
                if letter == "F":
                    row = lower
                elif letter == "B":
                    row = upper
                lower = 0
                upper = 7
            elif pos == 9:
                if letter == "L":
                    col = lower
                elif letter == "R":
                    col = upper
            pos += 1
        return (row * 8) + col

def missing_ids(seats):
    seats = sorted(seats)
    start, end = seats[0], seats[-1]
    return sorted(set(range(start, end + 1)).difference(seats))

with open("5.input.txt", "r") as f:
    seats = []
    for bpass in f:
        bp = BoardingPass(bpass.rstrip())
        seats.append(bp.getSeatId())
    print(f"Seat Ids: {sorted(seats)}")
    print(f"Your Seat Id: {missing_ids(seats)}") 
