# Import os library which will help with directory reading
import os

# Import our main calculation logic class
from bioCalc.nucleotide_info import NucleotideInfo

# Use scandir method to get all files from data folder
with os.scandir('data') as files:
    # For each file print the info of calculations
    for file in files:
        print(f"****Info about {file.name} ****\n\n")
        dna = open(f"data/{file.name}")
        nucleotide_info = NucleotideInfo(dna.read())
        nucleotide_info.get_info();
        print(f"\n\n****{file.name} info end****\n\n")