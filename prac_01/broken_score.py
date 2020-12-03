"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
out_file = open("output.txt", "w")

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score > 90:
        print("Excellent", file=out_file)
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

out_file.close()