# Import Counter from python library 'collections', which will allow to calculate all chars in string
from collections import Counter
# Import model in which we will keep given DNA nucleotides count
from bioCalc.models.dnaCounterResult import DNACounterResult


class BioCalc:
    # Declare the class BioCalc which have two methods

    @staticmethod
    def nucleotide_count_in_dna(dna):
        # This method receive the DNA string as parameter
        # populate DNACounterResult model with A, T, G and C counts
        # and return the populated model
        count = Counter(dna)
        result_model = DNACounterResult(count['A'], count['T'], count['G'], count['C'])
        return result_model

    @staticmethod
    def nucleotide_percentage_in_dna(nucleotide_count, dna_length):
        # This method receive nucleotide count (Ex: A nucleotide count) and DNA length
        # calculate and return the percentage of given nucleotide in given DNA
        percentage = (nucleotide_count * 100) / dna_length
        return percentage
