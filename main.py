# Baigiamasis darbas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from colorama import init, Fore, Back, Style

def load_data(file):
    data = pd.read_csv(file, encoding='utf-8')

    list_of_years = data['metai'].to_list()
    list_of_vma = data['vid_mot_amz'].to_list()
    list_of_vap = data['vid_amz_pirmag'].to_list()
    list_of_gimev = data['gime_viso'].to_list()
    list_of_gimeb = data['gime_b'].to_list()
    list_of_gimem = data['gime_m'].to_list()
    list_of_LT = data['LT'].to_list()
    list_of_GBR = data['GBR'].to_list()
    list_of_NOR = data['NOR'].to_list()
    list_of_DE = data['DE'].to_list()
    list_of_IRL = data['IRL'].to_list()
    list_of_RUS = data['RUS'].to_list()
    list_of_SWE = data['SWE'].to_list()
    list_of_ESP = data['ESP'].to_list()
    list_of_USA = data['USA'].to_list()
    list_of_OC = data['O_C'].to_list()
    list_of_mireviso = data['mire_viso'].to_list()
    list_of_mirev = data['mire_v'].to_list()
    list_of_mirem = data['mire_m'].to_list()
    list_of_mire18 = data['mire_0_18'].to_list()
    list_of_mire40 = data['mire_19_40'].to_list()
    list_of_mire60 = data['mire_41_60'].to_list()
    list_of_mire80 = data['mire_61_80'].to_list()
    list_of_mire99 = data['mire_81_99'].to_list()
    list_of_infekcija = data['infekcija'].to_list()
    list_of_navikai = data['navikai'].to_list()
    list_of_kraujotaka = data['kraujotaka'].to_list()
    list_of_kvepavimo = data['kvepavimo'].to_list()
    list_of_virskinimo = data['virskinimo'].to_list()
    list_of_isorpr = data['isor_priezastys'].to_list()
    list_of_transp = data['transp_ivykiai'].to_list()
    list_of_nukritimai = data['nukritimai'].to_list()
    list_of_paskendimas = data['paskendimas'].to_list()
    list_of_alkoholis = data['alkoholis'].to_list()
    list_of_savizudybe = data['savizudybe'].to_list()
    list_of_nuzudymas = data['nuzudymas'].to_list()
    list_of_kitospr = data['kitos_priezastys'].to_list()

    # gimdanciu moteru amziaus diagrama
    # x = np.array(list_of_years)
    # y1 = np.array(list_of_vma)
    # y2 = np.array(list_of_vap)
    #
    # plt.plot(x, y1, label = 'Visų gimdymų')
    # plt.plot(x, y2, color = 'r', label = 'Pirmagimis')
    # plt.title('Gimdančių moterų vidutinis amžius')
    # plt.xlabel('Metai')
    # plt.ylabel('Moters amžius')
    # plt.legend()
    # plt.show()

    # gimusiu vaiku skaiciaus diagrama
    x = np.array(list_of_years)
    y3 = np.array(list_of_gimev)
    y4 = np.array(list_of_gimeb)
    y5 = np.array(list_of_gimem)
    y6 = 

    plt.plot(x, y3, color = '#8a2be2', marker = 'o', label = 'Bendras')
    plt.plot(x, y4, marker = 'o', label = 'Berniukai')
    plt.plot(x, y5, marker = 'o', color='#fb607f', label='Mergaitės')
    plt.title('Gimusių vaikų skaičiaus kitimas')
    plt.xlabel('Metai')
    plt.ylabel('Gimusių vaikų skaičius')
    plt.legend()
    plt.grid()
    plt.show()










def main():
    file = 'gimst_mirstam.csv'
    data = load_data(file)

if __name__ == '__main__':
    main()


