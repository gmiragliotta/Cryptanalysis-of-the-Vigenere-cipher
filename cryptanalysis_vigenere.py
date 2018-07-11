import sys
from collections import Counter

def mic(cypher_x, cypher_y):
    N_x = len(cypher_x)
    N_y = len(cypher_y)
    freqs_x = Counter(cypher_x)
    freqs_y = Counter(cypher_y)

    alphabet =  map(chr, range( ord('A'), ord('Z')+1))

    freqsum = 0.0

    # sum all letter's frequences
    for letter in alphabet:
        freqsum += freqs_x[letter] * freqs_y[letter]

    mic_value = freqsum / (N_x * N_y)

    return mic_value

def mic_values(cyphertext, keylength):
    mic_values = []

    for i in range(0, keylength-1):
        # i due insiemi x ed y
        text_x = ""
        text_y = ""

        # make x set
        j = i
        while(j < len(cyphertext)):
            text_x += cyphertext[j]
            j += keylength

        # make y set
        j = i + 1
        while(j < len(cyphertext)):
            text_y += cyphertext[j]
            j += keylength

        # try all 26 shift and calculate mic between x and y
        temp = []
        for shift in range (0, 26):
            text_y_shifted = ""
            for letter in text_y:
                text_y_shifted += chr( ((ord(letter) - 65 + shift) % 26) + 65)
            temp.append(mic(text_x, text_y_shifted))

        # nested list
        mic_values.append(temp)
    return mic_values

def print_mic_values(mic_values):
    print()
    for i in range(0, len(mic_values)):
        print("k" + str(i) + " - k" +str(i+1) +  " = " + str(mic_values[i].index(max(mic_values[i]))) )
        print("\t")
        for mic_value in mic_values[i]:
            print("\t%.4f" % mic_value, end='')
        print("\n")

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

def print_ic_values(ic_values):
    print("\t\nt = ", len(ic_values))
    print("\n\tic_values:", end='')
    for ic_value in ic_values:
        print("\t%.4f" %ic_value, end='')

def find_keylength(cyphertext):
    for keylength in range(1, 10000):
        ic_values = ic_by_keylength(cyphertext, keylength)

        avg_ic_value = sum(ic_values) / float(len(ic_values))

        if(avg_ic_value > 0.060):
            print_ic_values(ic_values)
            print("\n\nThe key is likely to have a length of %d, with an average ic \
of %.3f\n" %(keylength, avg_ic_value))
            return keylength

    print("Keylength not found!\n")
    return 0

if __name__ == "__main__":
    cypher_file = open(sys.argv[1], 'r')
    cyphertext = cypher_file.read()
    keylength = 0

    # remove all whitespace characters (space, tab, newline, and so on)
    cyphertext = ''.join(cyphertext.split())

    while(True):
        print("1) Calculate coincidence index.")
        print("2) Calculate mutual coincidence index.")
        print("0) Exit.\n")

        try:
            choice = int(input("Make a choice: "))
        except ValueError as err:
            print("\nValueError: {}\n".format(err))
            continue

        if(choice == 0):
            break
        elif(choice == 1):
            keylength = find_keylength(cyphertext)
        elif(choice == 2):
            if(keylength > 0):
                mic_values = mic_values(cyphertext, keylength)
                print_mic_values(mic_values)
            else:
                print("\nCalculate coincidence index first!\n")
        else:
            print("\nWrong option selected!\n")
