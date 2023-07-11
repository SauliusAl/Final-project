# Baigiamasis darbas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style

def load_data(file):
    data = pd.read_csv(file, encoding='utf-8')
    # return data

    list_of_years = data['metai'].to_list()
    list_of_vma = data['vid_mot_amz'].to_list()
    list_of_vap = data['vid_amz_pirmag'].to_list()

    x = np.array(list_of_years)
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
    file = 'gimst_mirstam.csv'
    data = load_data(file)

if __name__ == '__main__':
    main()


