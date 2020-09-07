# Import os library which will help with directory reading
import os

# Import our main calculation logic class
from Graph.overlap_graphs import OverlapGraph
from bioCalc.nucleotide_info import NucleotideInfo
from main_menu import MainMenu

menu = MainMenu()
run = True
while run:
    selected_menu_item: int = menu.show_main_menu()

    if selected_menu_item == 1:
        # Use scandir method to get all files from data folder
        with os.scandir('data') as files:
            # For each file print the info of calculations
            for file in files:
                print(f"****Info about {file.name} ****\n\n")
                dna = open(f"data/{file.name}")
                nucleotide_info = NucleotideInfo(dna.read())
                nucleotide_info.get_info()
                print(f"\n\n****{file.name} info end****\n\n")
    elif selected_menu_item == 2:
        dnaList = dict(Rosalind_0498='AAATAAA', Rosalind_2391='AAATTTT', Rosalind_2323='TTTTCCC',
                       Rosalind_0442='AAATCCC', Rosalind_5013='GGGTGGG')
        graph = OverlapGraph(dnaList)
        graph.find_graph_overlap(3)
    elif selected_menu_item == 3:
        run = False