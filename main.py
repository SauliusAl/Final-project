# Baigiamasis darbas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style

def load_data1(file):
    data1 = pd.read_csv(file, encoding='utf-8')
    # return data

    list_of_years1 = data1['Metai'].to_list()
    list_of_vma = data1['Vid_mot_amzius'].to_list()
    list_of_vap = data1['Vid_amz_pirmag'].to_list()

    x = np.array(list_of_years1)
    y1 = np.array(list_of_vma)
    y2 = np.array(list_of_vap)

    plt.plot(x, y1, label = 'Visų gimdymų')
    plt.plot(x, y2, color = 'r', label = 'Pirmagimis')
    plt.title('Gimdančių moterų vidutinis amžius')
    plt.xlabel('Metai')
    plt.ylabel('Moters amžius')
    plt.legend()
    plt.show()

def main():
    file = 'gimd_mot_amzius.csv'
    data = load_data1(file)


if __name__ == '__main__':
    main()


