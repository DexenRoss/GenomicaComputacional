#!coding:utf8

import random
import math
from ast import pattern
import re
lista_secuencias=[
    "ATATATACATACTGGTAATGGGCGCGCGTGTGTTAAGTTCTGTTGTAGGGGTGATTAGGGGCG",
    "GGCCCACACCCCACACCAATATATGTGGTGTGGGCTCCACTCTCTCGCGCTCGCGCTGGGGAT",
    "ATAAGGTGTGTGGGCGCGCCCCGCGCGCGCGTTTTTTCGCGCGCCCCCGCGCGCGCGCGCGCG",
    "GGCGCGGGACGCGGCGGCGGATCCCGATCCGTGCGTCAATACTATTATGGCCAGATAGAATAA",
    "GTGCTGCTGCGGCGCCCACACCTATTATCTCTCTCTCTCTGCCTCTCCACCTCGGGGCTTAAT",
    "GCGCTGCTGCTGGCTCGATGGGCGCGTGCGTCGTAGCTCGATGCTGGCTCGAGCTGTAATCTT",
    "GGCGCTCGCTCGGATGCGCGGCCGGGCTCTCTGCTCGCGCTCGCTTCGCGCTCGTGACCGCTG",
    "AATTGGTGCGCGCTCGCGCACACACAGAGAGAGGGTTTATATAGGATGATATATCCACATTGG",
    "ATGCTGCTGCTGGCTCTGCTTGCGCTCTGCTCGCTGGGGTGTGTGTGCCGCGCGCTGCTGCTC",
    "GCTGGGCTCGCTCGATGCGCGCGGGCGCGCGACCGCGGACGGCGTCGCTGCTAAATGGGCTTC"
]

def ejercicio_2(lista_secuencias):
    L = []
    pattern = r'(TAC)(.{3})+(TAA|TAG|TGA)'
    indice=0
    for sec in lista_secuencias:
        if re.search(pattern,sec):
            L.append(indice)
        indice+=1

    return L
ejercicio_2(lista_secuencias)

def ejercicio_3(archivo):
    f = open(archivo,"r")
    lines = f.readlines()
    pattern = re.compile(r'(AGATAG|TGATAG|AGATAA|TGATAA)')
    L = []
    for sec in lines:
        ind = pattern.finditer(sec)
        L.append(len(list(ind)))

    return L
ejercicio_3("promotores.txt")

def ejercicio_4(M):
    x = 0.
    i = 1
    D = 0
    while(i < M):
        i += 1
        x = random.uniform(-1,1) <= 1
        y = random.uniform(-1,1) <= 1
        d = math.sqrt((x**2 + y**2))
        if d <= 1:
            D += 1
    x = 4*D/i
    return x
     