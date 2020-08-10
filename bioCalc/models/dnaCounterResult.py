class DNACounterResult:
    # This model will used to keep counted
    # nucleotides in DNA
    def __init__(self, a_count, t_count, g_count, c_count):
        self.ACount = a_count
        self.TCount = t_count
        self.GCount = g_count
        self.CCount = c_count
