def main():
    a_seed = 16807
    a_val = 783
    #a_val = 65
    b_seed = 48271
    b_val = 325
    #b_val = 8921

    divisor = 2147483647
    samples = 5000000

    matching = []
    a_samples = []
    b_samples = []

    count = 0

    while(len(a_samples) < samples or len(b_samples) < samples):

        a_val = (a_val * a_seed) % divisor
        b_val = (b_val * b_seed) % divisor

        if((a_val % 4) == 0):
            a_samples.append(a_val)

        if((b_val % 8) == 0):
            b_samples.append(b_val)

    for i in range(0, min(len(a_samples), len(b_samples))):
        if(str(bin(a_samples[i]))[-16:] == str(bin(b_samples[i]))[-16:]):
            count += 1

    print count


main()