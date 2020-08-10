from bioCalc.biocalc import BioCalc


class NucleotideInfo:
    def __init__(self, dna):
        self.DNA = dna

    def get_info(self):
        bio_calc = BioCalc()
        print("****Get Nucleotides count****")
        count_result = bio_calc.nucleotide_count_in_dna(self.DNA)
        print(("A: %s\nT: %s\nG: %s\nC: %s" % (
            count_result.ACount, count_result.TCount, count_result.GCount, count_result.CCount)))
        print("******************************")

        dna_length = len(self.DNA)

        print("\n\n****Get Nucleotides percentage****")
        a_percent = bio_calc.nucleotide_percentage_in_dna(count_result.ACount, dna_length)
        t_percent = bio_calc.nucleotide_percentage_in_dna(count_result.TCount, dna_length)
        g_percent = bio_calc.nucleotide_percentage_in_dna(count_result.GCount, dna_length)
        c_percent = bio_calc.nucleotide_percentage_in_dna(count_result.CCount, dna_length)

        print(f"A%: {a_percent}\nT%: {t_percent}\nG%: {g_percent}\nC%: {c_percent}")
        print("******************************")

        print("\n\n****Get GC Nucleotides percentage****")
        gc_count = count_result.GCount + count_result.CCount
        gc_percent = bio_calc.nucleotide_percentage_in_dna(gc_count, dna_length)
        print(f"GC%: {gc_percent}")
        print("******************************")