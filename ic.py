import sys
from collections import Counter

def ic(cyphertext):
    N = len(cyphertext)
    freqs = Counter(cyphertext)

    alphabet =  map(chr, range( ord('A'), ord('Z')+1))

    freqsum = 0.0

    # sum all letter's frequences
    for letter in alphabet:
        freqsum += freqs[letter] * (freqs[letter] - 1)

    ic_value = freqsum / (N * (N-1))

    return ic_value

def ic_by_keylength(cyphertext, keylength):
    ic_values = []

    for i in range(0, keylength):
        text = ""
        j = i
        while(j < len(cyphertext)):
            text += cyphertext[j]
            j += keylength
        ic_values.append(ic(text))

    return ic_values

if __name__ == "__main__":
    cypher_file = open(sys.argv[1], 'r')
    cyphertext = cypher_file.read()
    keylength = int(sys.argv[2])

    # remove all whitespace characters (space, tab, newline, and so on)
    cyphertext = ''.join(cyphertext.split())

    ic_values = ic_by_keylength(cyphertext, keylength)

    print("\t\nt = ", keylength)
    print("\n\tic_values:", end='')
    for ic_value in ic_values:
        print("\t%.4f" %ic_value, end='')

    avg_ic_value = sum(ic_values) / float(len(ic_values))

    print("\n")
    if(avg_ic_value > 0.060):
        print("The key is likely to have a length of %d, with an average ic \
of %.3f\n" %(keylength, avg_ic_value))
    else:
        print("Try another keylength. Average ic of %.4f\n" %avg_ic_value)
