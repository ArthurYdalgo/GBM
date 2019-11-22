import os

os.command("pip install networkx")
os.command("pip install inspect")
#os.command("pip install prettytable")
os.command("python parseBNF.py run")
os.command("python Reserved/reserved_generator.py")
os.command("python Alphabet/alphabet_generator.py")

