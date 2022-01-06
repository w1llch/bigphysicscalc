import math

# this section provides variables for formatting purposes
v_0 = "v" + "\u2080"
vsquared = "v" + "\u00B2"
tsquared = "t" + "\u00B2"
v_0squared = "v" + "\u2080" + "\u00B2"
deltax = "\u0394" + "x"
sqrt = "\u221A"
sec = "s"
meter = "m"
metersec = "m/s"
metersec2 = "m/s" + "\u00B2"

# [v = v_0 + at] and all equations derived from it
equation1 = "v = " + v_0 + " + at"
equation2 = v_0 + " = v - at"
equation3 = "a = (v - " + v_0 + ")/t"
equation4 = "t = (v - " + v_0 + ")/a"

# [v^2 = v_0^2 + 2a(deltax)] and all equations derived from it
equation5 = "v = " + sqrt + "(" + v_0squared + " + 2a" + deltax + ")"
equation6 = v_0 + " = " + sqrt + "(" + vsquared + " + 2a" + deltax + ")"
equation7 = "a = (" + vsquared + " - " + v_0squared + ")/2" + deltax
equation8 = deltax + " = (" + vsquared + " - " + v_0squared + ")/2a"

# [(deltax) = v_0t + 0.5at^2] and all equations derived from it
equation9 = deltax + " = " + v_0 + "t + 0.5a" + tsquared
equation10 = v_0 + " = " + "(" + deltax + " - 0.5a" + tsquared + ")/t"
equation11 = "Quadratic solver coming soon"
equation12 = "This value is most likely g, or 9.8 m/s" + "\u00B2"

# [(deltax) = vt] and all equations derived from it
equation13 = deltax + " = vt"
equation14 = "v = (" + deltax + "/t)"
equation15 = "t = (" + deltax + "/v)"


# starting page that user is met with upon running program
def starting_page():
    print("Welcome to will's physics calculator! Choose topic A, B, C, or D to begin.")
    print("A. Kinematics" + "\n" + "B: Forces" + "\n" + "C. Rotational Kinematics" + "\n" + "D. More coming soon!\n")
    phys_topic = input("Enter a letter: ")
    if phys_topic == "A":
        choosekineq()
    elif phys_topic == "a":
        choosekineq()
    else:
        print("This topic is coming soon!")


# if kinematics is the chosen topic, the user will be led here to choose a kinematics equation
def choosekineq():
    print("A. " + equation1 + "\nB. " + equation2 + "\nC. " + equation3 + "\nD. " + equation4 + "\n")
    choosekineqinput = input("Enter A, B, C, or D: ")
    if choosekineqinput == "A":
        choosekineq1var()
    elif choosekineqinput == "a":
        choosekineq1var()
    elif choosekineqinput == "B":
        choosekineq2var()
    elif choosekineqinput == "b":
        choosekineq2var()
    elif choosekineqinput == "C":
        choosekineq3var()
    elif choosekineqinput == "c":
        choosekineq3var()
    elif choosekineqinput == "D":
        choosekineq4var()
    elif choosekineqinput == "d":
        choosekineq4var()
    else:
        print("not a valid input, rerun the program")


# if equation1  is chosen, the user will be led here to choose a variable to solve for
def choosekineq1var():
    print("A. v \n" + "B. " + v_0 + "\n" + "C. a \n" + "D. t \n")
    choosekineq1variable = input("Enter A, B, C, or D: ")
    if choosekineq1variable == "A":
        ke1solve(1)
    elif choosekineq1variable == "a":
        ke1solve(1)
    elif choosekineq1variable == "B":
        ke1solve(2)
    elif choosekineq1variable == "b":
        ke1solve(2)
    elif choosekineq1variable == "C":
        ke1solve(3)
    elif choosekineq1variable == "c":
        ke1solve(3)
    elif choosekineq1variable == "D":
        ke1solve(4)
    elif choosekineq1variable == "d":
        ke1solve(4)
    else:
        print("not a valid input, rerun the program")


# if equation2  is chosen, the user will be led here to choose a variable to solve for
def choosekineq2var():
    print("A. " + vsquared + "\n" + "B. " + v_0squared + "\n" + "C. a \n" + "D. " + deltax + "\n")
    choosekineq2variable = input("Enter A, B, C, or D: ")
    if choosekineq2variable == "A":
        ke2solve(1)
    elif choosekineq2variable == "a":
        ke2solve(1)
    elif choosekineq2variable == "B":
        ke2solve(2)
    elif choosekineq2variable == "b":
        ke2solve(2)
    elif choosekineq2variable == "C":
        ke2solve(3)
    elif choosekineq2variable == "c":
        ke2solve(3)
    elif choosekineq2variable == "D":
        ke2solve(4)
    elif choosekineq2variable == "d":
        ke2solve(4)
    else:
        print("not a valid input, rerun the program")


# if equation3  is chosen, the user will be led here to choose a variable to solve for
def choosekineq3var():
    print("A. " + deltax + "\n" + "B. " + v_0 + "\n" + "C. t \n" + "D. a \n")
    choosekineq3variable = input("Enter A, B, C, or D: ")
    if choosekineq3variable == "A":
        ke3solve(1)
    elif choosekineq3variable == "a":
        ke3solve(1)
    elif choosekineq3variable == "B":
        ke3solve(2)
    elif choosekineq3variable == "b":
        ke3solve(2)
    elif choosekineq3variable == "C":
        ke3solve(3)
    elif choosekineq3variable == "c":
        ke3solve(3)
    elif choosekineq3variable == "D":
        ke3solve(4)
    elif choosekineq3variable == "d":
        ke3solve(4)
    else:
        print("not a valid input, rerun the program")


# if equation4  is chosen, the user will be led here to choose a variable to solve for
def choosekineq4var():
    print("A. " + deltax + "\n" + "B. v \n" + "C. t \n")
    choosekineq4variable = input("Enter A, B, C, or D: ")
    if choosekineq4variable == "A":
        ke4solve(1)
    elif choosekineq4variable == "a":
        ke4solve(1)
    elif choosekineq4variable == "B":
        ke4solve(2)
    elif choosekineq4variable == "b":
        ke4solve(2)
    elif choosekineq4variable == "C":
        ke4solve(3)
    elif choosekineq4variable == "c":
        ke4solve(3)
    elif choosekineq4variable == "D":
        ke4solve(4)
    elif choosekineq4variable == "d":
        ke4solve(4)
    else:
        print("not a valid input, rerun the program")


# after a variable is selected for equation1, the user will be led here
def ke1solve(n):
    if n == 1:
        print(equation1 + "\n")
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        avalue = float(input("Enter a value for a: "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round((v_0value + avalue * tvalue), 3))
        print(xyz + metersec)
    elif n == 2:
        print(equation2 + "\n")
        vvalue = float(input("Enter a value for v: "))
        avalue = float(input("Enter a value for a: "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round((vvalue - avalue * tvalue), 3))
        print(xyz + metersec)
    elif n == 3:
        print(equation3 + "\n")
        vvalue = float(input("Enter a value for v: "))
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round(((vvalue - v_0value) / tvalue), 3))
        print(xyz + metersec2)
    elif n == 4:
        print(equation4 + "\n")
        vvalue = float(input("Enter a value for v: "))
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        avalue = float(input("Enter a value for a: "))
        xyz = str(round((vvalue - v_0value) / avalue, 3))
        print(xyz + sec)


def ke2solve(n):
    if n == 1:
        print(equation5 + "\n")
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        avalue = float(input("Enter a value for a: "))
        dxvalue = float(input("Enter a value for " + deltax + ": "))
        xyz = str(round(math.sqrt((math.pow(v_0value, 2)) + 2 * avalue * dxvalue), 3))
        print(xyz + metersec)
    elif n == 2:
        print(equation6 + "\n")
        vvalue = float(input("Enter a value for v: "))
        avalue = float(input("Enter a value for a: "))
        dxvalue = float(input("Enter a value for " + deltax + ": "))
        xyz = str(round(math.sqrt((math.pow(vvalue, 2)) + 2 * avalue * dxvalue), 3))
        print(xyz + metersec)
    elif n == 3:
        print(equation7 + "\n")
        vvalue = float(input("Enter a value for v: "))
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        dxvalue = float(input("Enter a value for " + deltax + ": "))
        xyz = str(round((math.pow(vvalue, 2) - math.pow(v_0value, 2)) / (2 * dxvalue), 3))
        print(xyz + metersec2)
    elif n == 4:
        print(equation8 + "\n")
        vvalue = float(input("Enter a value for v: "))
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        avalue = float(input("Enter a value for a: "))
        xyz = str(round((math.pow(vvalue, 2) - math.pow(v_0value, 2)) / (2 * avalue), 3))
        print(xyz + meter)


def ke3solve(n):
    if n == 1:
        print(equation9 + "\n")
        v_0value = float(input("Enter a value for " + v_0 + ": "))
        tvalue = float(input("Enter a value for t: "))
        avalue = float(input("Enter a value for a: "))
        xyz = str(round(v_0value * tvalue + 0.5 * avalue * math.pow(tvalue, 2), 3))
        print(xyz + meter)
    elif n == 2:
        print(equation10 + "\n")
        dxvalue = float(input("Enter a value for" + deltax + ": "))
        avalue = float(input("Enter a value for a (most likely 9.8 m/s" + "\u00B2" + "): "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round((dxvalue - 0.5 * avalue * math.pow(tvalue, 2)), 3) / tvalue)
        print(xyz + metersec)
    elif n == 3:
        print(equation11)
    elif n == 4:
        print(equation12)


def ke4solve(n):
    if n == 1:
        print(equation13 + "\n")
        vvalue = float(input("Enter a value for v: "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round(vvalue * tvalue, 3))
        print(xyz + meter)
    elif n == 2:
        print(equation14 + "\n")
        dxvalue = float(input("Enter a value for " + deltax + ": "))
        tvalue = float(input("Enter a value for t: "))
        xyz = str(round(dxvalue / tvalue, 3))
        print(xyz + metersec)
    elif n == 3:
        print(equation15 + "\n")
        dxvalue = float(input("Enter a value for " + deltax + ": "))
        vvalue = float(input("Enter a value for v: "))
        xyz = str(round(dxvalue / vvalue, 3))
        print(xyz + sec)


starting_page()
