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

if __name__ == "__main__":
    cypher_file = open(sys.argv[1], 'r')
    cyphertext = cypher_file.read()
    keylength = int(sys.argv[2])

    # remove all whitespace characters (space, tab, newline, and so on)
    cyphertext = ''.join(cyphertext.split())

    mic_values = mic_values(cyphertext, keylength)

    print("\n")
    for i in range(0, len(mic_values)):
        print("k" + str(i) + " - k" +str(i+1) +  " = " + str(mic_values[i].index(max(mic_values[i]))) )
        print("\t")
        for mic_value in mic_values[i]:
            print("\t%.4f" % mic_value, end='')
        print("\n")
