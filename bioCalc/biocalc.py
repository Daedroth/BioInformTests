from collections import Counter

from bioCalc.models.dnaCounterResult import DNACounterResult


class BioCalc:
    @staticmethod
    def nucleotide_count_in_dna(dna):
        count = Counter(dna)
        result_model = DNACounterResult(count['A'], count['T'], count['G'], count['C'])
        return result_model

    @staticmethod
    def nucleotide_percentage_in_dna(nucleotide_count, dna_length):
        percentage = (nucleotide_count * 100) / dna_length
        return percentage
