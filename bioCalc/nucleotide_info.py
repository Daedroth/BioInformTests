# Import our BioCalc class
from bioCalc.biocalc import BioCalc


class NucleotideInfo:
    # This class contains the main calculation logic
    # on initialize it's receive the DNA string
    def __init__(self, dna):
        self.DNA = dna

    def get_info(self):
        # This method do the main calculations:

        # Initiate the instance of BioCalc class
        bio_calc = BioCalc()
        print("****Get Nucleotides count****")
        # calculate the nucleotides counts and output them to console
        count_result = bio_calc.nucleotide_count_in_dna(self.DNA)
        print(("A: %s\nT: %s\nG: %s\nC: %s" % (
            count_result.ACount, count_result.TCount, count_result.GCount, count_result.CCount)))
        print("******************************")

        # Get the length of DNA string by using python build-in 'len' function
        dna_length = len(self.DNA)

        # Calculate the nucleotides percentages and output them to console
        print("\n\n****Get Nucleotides percentage****")
        a_percent = bio_calc.nucleotide_percentage_in_dna(count_result.ACount, dna_length)
        t_percent = bio_calc.nucleotide_percentage_in_dna(count_result.TCount, dna_length)
        g_percent = bio_calc.nucleotide_percentage_in_dna(count_result.GCount, dna_length)
        c_percent = bio_calc.nucleotide_percentage_in_dna(count_result.CCount, dna_length)

        print(f"A%: {a_percent}\nT%: {t_percent}\nG%: {g_percent}\nC%: {c_percent}")
        print("******************************")

        # Calculate the percentage of GC nucleotides and output them to console
        # TODO: can be simplified, using sum of G and C nucleotides percentage
        print("\n\n****Get GC Nucleotides percentage****")
        gc_count = count_result.GCount + count_result.CCount
        gc_percent = bio_calc.nucleotide_percentage_in_dna(gc_count, dna_length)
        print(f"GC%: {gc_percent}")
        print("******************************")