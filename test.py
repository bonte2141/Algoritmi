def nr_opt(n):
    sir = str(n)
    c = 0
    if sir[len(sir)-1] == "8":
        c = 1
    if len(sir)-1 <= 0:
        return c
    return c + nr_opt(int(sir[:len(sir)-1]))








if __name__ == "__main__":
    print(nr_opt(15682868))