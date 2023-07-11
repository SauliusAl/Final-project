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
    list_of_uzs = data['sum_uzs'].to_list()
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
    # x = np.array(list_of_years)
    # y3 = np.array(list_of_gimev)
    # y4 = np.array(list_of_gimeb)
    # y5 = np.array(list_of_gimem)
    #
    # plt.plot(x, y3, color = '#8a2be2', marker = 'o', label = 'Bendras')
    # plt.plot(x, y4, marker = 'o', label = 'Berniukai')
    # plt.plot(x, y5, marker = 'o', color='#fb607f', label='Mergaitės')
    # plt.title('Gimusių vaikų skaičiaus kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.grid()
    # plt.show()


    # # gimusiu vaiku uzsienyje skaiciaus palyginimas su gimusiais Lietuvoje
    # x = np.array(list_of_years)
    # y6 = np.array(list_of_LT)
    # y7 = np.array(list_of_uzs)
    # lt2018 = (y6[0])
    # lt2019 = (y6[1])
    # lt2020 = (y6[2])
    # lt2021 = (y6[3])
    # lt2022 = (y6[4])
    # uzs2018 = (y7[0])
    # uzs2019 = (y7[1])
    # uzs2020 = (y7[2])
    # uzs2021 = (y7[3])
    # uzs2022 = (y7[4])

    # # Gimusiu vaiku Lietuvoje ir uzsienyje 2018 m. skaiciu palyginimas
    # pyrag2018 = np.array([lt2018, uzs2018])
    # fig, ax = plt.subplots()
    # ax.pie(pyrag2018, labels=pyrag2018, autopct='%1.1f%%', startangle=0)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2018 metais')
    # plt.show()

    # # Gimusiu vaiku Lietuvoje ir uzsienyje 2018 m. skaiciu palyginimas
    # pyrag2019 = np.array([lt2019, uzs2019])
    # fig, ax = plt.subplots()
    # ax.pie(pyrag2019, labels=pyrag2019, autopct='%1.1f%%', startangle=0)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2019 metais')
    # plt.show()

    # # Gimusiu vaiku Lietuvoje ir uzsienyje 2018 m. skaiciu palyginimas
    # pyrag2020 = np.array([lt2020, uzs2020])
    # fig, ax = plt.subplots()
    # ax.pie(pyrag2020, labels=pyrag2020, autopct='%1.1f%%', startangle=0)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2020 metais')
    # plt.show()

    # # Gimusiu vaiku Lietuvoje ir uzsienyje 2018 m. skaiciu palyginimas
    # pyrag2021 = np.array([lt2021, uzs2021])
    # fig, ax = plt.subplots()
    # ax.pie(pyrag2021, labels=pyrag2021, autopct='%1.1f%%', startangle=0)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2021 metais')
    # plt.show()

    # # Gimusiu vaiku Lietuvoje ir uzsienyje 2018 m. skaiciu palyginimas
    # pyrag2022 = np.array([lt2022, uzs2022])
    # fig, ax = plt.subplots()
    # ax.pie(pyrag2022, labels=pyrag2022, autopct='%1.1f%%', startangle=0)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2022 metais')
    # plt.show()


def main():
    file = 'gimst_mirstam.csv'
    data = load_data(file)

if __name__ == '__main__':
    main()


