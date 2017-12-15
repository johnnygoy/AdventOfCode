def main():
    a_seed = 16807
    a_val = 783
    #a_val = 65
    b_seed = 48271
    b_val = 325
    #b_val = 8921

    divisor = 2147483647
    samples = 40000000

    count = 0

    for i in range(0,samples):
        a_val = (a_val * a_seed) % divisor
        b_val = (b_val * b_seed) % divisor
        if(str(bin(a_val))[-16:] == str(bin(b_val))[-16:]):
            count += 1

    print count


main()