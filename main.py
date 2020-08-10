import os

from bioCalc.models.nucleotide_info import NucleotideInfo

with os.scandir('data') as files:
    for file in files:
        print(f"****Info about {file.name} ****\n\n")
        dna = open(f"data/{file.name}")
        nucleotide_info = NucleotideInfo(dna.read())
        nucleotide_info.get_info();
        print(f"\n\n****{file.name} info end****\n\n")