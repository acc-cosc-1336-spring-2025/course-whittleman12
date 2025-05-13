def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("The two strings must be of equal length.")
    sum = 0
    for ch in range(len(dna1)):
        if dna1[ch] != dna2[ch]:
            sum += 1
    return sum



def get_dna_complement(dna):
    for ch in dna:
        if ch == "A":
            ch = "T"
        if ch == "T":
            ch = "A"
        if ch == "G":
            ch = "C"
        if ch == "C":
            ch ="G"
    return dna[::-1]