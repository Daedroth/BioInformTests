from bioCalc.biocalc import BioCalc

dna = "GAAGGTCACAGTGACGGTATGGCGCACCCATGGATTGCTTCACCGCGGTGATACATAGTCGATTTGGCTACCCCACCACCGAGTAGGAATCGATAGATTCTTCTTTCTTATAGAGCCTGAAGGTCTGCCAGACGAGTACCTAAATAGTTTATGTTGTTCGTCGAGAAGGGCATCTGGTCAGTACATTTATACGAACCTCCCCTGATGTAAATTCACCCGGGATGATGCACAATCCATTATAGTGTGCCCCGACCCCGCCTTCAACTTAATGCTGAAATGAACGTGCTCGAGTTTGCTTTATTCCTGGTCATACGCTGGGAGTGCAGACGAGTCCTCTGGAGCCAGATTGAGGGTATAGGTCGCGGACCCTAGTGCCAAAGCCCCCGAGGGGAGGCACATAGAGCTAGATGATCGACTCTCGGCTCGAAAACAGTTGACTCTTATCGCCCTCGGGTTACCGCACGACGTGACCCGGAGGCAACCTGCACAACTGGCTAATTTGGGGACACGTCCAACCTCGTGTAATCGTAGAAAAGATAGTTCATGGCACTTTGCTTTAGACACCCATCTTGTCTCCATGAATAACGGAGCTTGGATCAGATTTTGGGCCTGACAGAGTAGAATAACGCCAGCGGGTTACTCTGGAGGACAAAATAATGGCCGTGAAGCTAGCGAGTAGTCTCCTTAGTCCATTGAGGCCTGCGCGGCTTGGCCATTTCTTGAGTAGTAGAATTTAATCTTCCATCTGGTTGGGCAAGATATACCGGTAGCTAGGACAGTAGTAGCCGATTGCCCAGTCATCACGCCAGCAGCGCTAAAGATTAAGTCGTTGATCCTGGTGAAAAAAAAACGAGTCATTCCGAGTGACCGTGTGAGACCCACGACTTCCATGCGAACTAACCGGAGGAGAGTAGGGGA "
bioCalc = BioCalc()
print("****Get Nucleotides count****")
countResult = bioCalc.nucleotide_count_in_dna(dna)
print(("A: %s\nT: %s\nG: %s\nC: %s" % (countResult.ACount, countResult.TCount, countResult.GCount, countResult.CCount)))
print("******************************")

dnaLength = len(dna)

print("\n\n****Get Nucleotides percentage****")
aPercent = bioCalc.nucleotide_percentage_in_dna(countResult.ACount, dnaLength)
tPercent = bioCalc.nucleotide_percentage_in_dna(countResult.TCount, dnaLength)
gPercent = bioCalc.nucleotide_percentage_in_dna(countResult.GCount, dnaLength)
cPercent = bioCalc.nucleotide_percentage_in_dna(countResult.CCount, dnaLength)

print(f"A%: {aPercent}\nT%: {tPercent}\nG%: {gPercent}\nC%: {cPercent}")
print("******************************")

print("\n\n****Get GC Nucleotides percentage****")
gcCount = countResult.GCount + countResult.CCount
gcPercent = bioCalc.nucleotide_percentage_in_dna(gcCount, dnaLength)
print(f"GC%: {gcPercent}")
print("******************************")