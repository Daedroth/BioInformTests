class OverlapGraph:

    def __init__(self, dnaList: dict):
        self.DnaList = dnaList

    def find_graph_overlap(self, k: int):
        listLength = len(self.DnaList)
        dnas = list(self.DnaList.values())
        keys = list(self.DnaList.keys())

        for i in range(listLength):
            dna: str = dnas[i]
            suffix = dna[-k:]
            for j in range(1, listLength-1):
                next_dna = dnas[j]
                prefix = next_dna[0:k]
                if(suffix == prefix):
                    print(keys[i], '->', keys[j], '\n')


