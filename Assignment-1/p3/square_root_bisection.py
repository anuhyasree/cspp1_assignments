"""square root of bisection"""
def main():
    """Defining main"""
    s_s = int(input())
    eps_ilon = 0.01
    l_ow = 0
    h_ih = s_s
    gu_es = (l_ow+h_ih)/2
    while abs(gu_es**2-s_s) >= eps_ilon:
        if gu_es**2 > s_s:
            h_ih = gu_es
        else:
            l_ow = gu_es
        gu_es = (l_ow+h_ih)/2
    if (gu_es**2-s_s) >= eps_ilon:
        print("Failed")
    else:
        print(gu_es)
if __name__ == "__main__":
    main()
