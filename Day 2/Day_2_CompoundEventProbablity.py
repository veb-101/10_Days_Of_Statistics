X = {"red": 4 / 7, "black": 3 / 7}
Y = {"red": 5 / 9, "black": 4 / 9}
Z = {"red": 4 / 8, "black": 4 / 8}

first = X["red"] * Y["red"] * Z["black"]
second = X["red"] * Y["black"] * Z["red"]
third = X["black"] * Y["red"] * Z["red"]

final = first + second + third
print(f"Probablity of getting 2 red balls and 1 black ball: {final}")
