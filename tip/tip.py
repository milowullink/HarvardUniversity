def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dol = float(d.replace("$", ""))
    return dol


def percent_to_float(p):
    per = "0." + p.replace("%", "")
    per2 = float(per)
    return per2


main()