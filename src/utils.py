import os
import sys
import math
import time


def limpar_tela():
    if(os.name == "nt"):
        os.system('cls')
    else:
        os.system('clear')
    
    print("#"*80)
    print("CONTROLE BANCARIO PYTHON         POS-GRADUACAO DATA SCIENCE E BIG DATA ANALITYCS")
    print("2020-04-27" + " "*30 + " Autor: HERSON MELO (hersonpc@gmail.com)")
    print("#"*80 + "\n")


def print_center(texto, tam_tela = 80):
    	tam = len(texto)
	espacos_a_esquerda = int(math.floor((tam_tela - tam) / 2))
	print(" "*espacos_a_esquerda + texto)


def sair_app():
    limpar_tela()
    print("\nAplicativo finalizado!\n\n".upper())
    sys.exit(1)
