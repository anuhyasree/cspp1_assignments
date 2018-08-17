"""Write a python program to find the square root of the given number"""
def main():
    """epsilon and step are initialized
    don't change these values"""
    s_so = float(input())
    epsilon_a = 0.01
    gues_s = s_so/2.0
    while gues_s <= s_so:
        if abs(gues_s**2-s_so) >= epsilon_a:
            gues_s = gues_s-(gues_s**2 - s_so)/(2*gues_s)
        else:
            break
    if abs(gues_s**2-s_so) >= epsilon_a:
        print("Failed")
    else:
        print(gues_s)
if __name__ == "__main__":
    main()
