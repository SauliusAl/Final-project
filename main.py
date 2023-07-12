# Baigiamasis darbas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    list_of_diabetas = data['diabetas'].to_list()
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
    list_of_covid = data['covid'].to_list()


    # # 1.Gimdanciu moteru amziaus diagrama
    # x = np.array(list_of_years)
    # y1 = np.array(list_of_vma)
    # y2 = np.array(list_of_vap)
    # plt.plot(x, y1, label = 'Visų gimdymų')
    # plt.plot(x, y2, color = 'red', label = 'Pirmagimis')
    # plt.title('Gimdančių moterų vidutinis amžius')
    # plt.xlabel('Metai')
    # plt.ylabel('Moters amžius')
    # plt.legend()
    # plt.show()


    # # 2.Gimusiu vaiku skaiciaus diagrama
    # x = np.array(list_of_years)
    # y3 = np.array(list_of_gimev)
    # y4 = np.array(list_of_gimeb)
    # y5 = np.array(list_of_gimem)
    # plt.plot(x, y3, color = '#8a2be2', marker = 'o', label = 'Bendras')
    # plt.plot(x, y4, marker = 'o', label = 'Berniukai')
    # plt.plot(x, y5, marker = 'o', color='#fb607f', label='Mergaitės')
    # plt.title('Gimusių vaikų skaičiaus kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.grid()
    # plt.show()


    # # 3.Gimusiu vaiku uzsienyje skaiciaus palyginimas su gimusiais Lietuvoje
    # x = np.array(list_of_years)
    # y6 = np.array(list_of_LT)
    # y7 = np.array(list_of_uzs)
    # lt2018 = (y6[0])
    # uzs2018 = (y7[0])
    # lt2019 = (y6[1])
    # uzs2019 = (y7[1])
    # lt2020 = (y6[2])
    # uzs2020 = (y7[2])
    # lt2021 = (y6[3])
    # uzs2021 = (y7[3])
    # lt2022 = (y6[4])
    # uzs2022 = (y7[4])
    #
    # # 2018 m. skaiciu palyginimas
    # pyrag2018 = np.array([lt2018, uzs2018])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # ax.pie(pyrag2018, labels=pyrag2018, autopct='%1.1f%%', startangle=0, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2018 metais')
    # plt.show()
    #
    # # 2019 m. skaiciu palyginimas
    # pyrag2019 = np.array([lt2019, uzs2019])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # ax.pie(pyrag2019, labels=pyrag2019, autopct='%1.1f%%', startangle=0, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2019 metais')
    # plt.show()
    #
    # # 2020 m. skaiciu palyginimas
    # pyrag2020 = np.array([lt2020, uzs2020])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # ax.pie(pyrag2020, labels=pyrag2020, autopct='%1.1f%%', startangle=0, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2020 metais')
    # plt.show()
    #
    # # 2021 m. skaiciu palyginimas
    # pyrag2021 = np.array([lt2021, uzs2021])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # ax.pie(pyrag2021, labels=pyrag2021, autopct='%1.1f%%', startangle=0, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2021 metais')
    # plt.show()
    #
    # # 2022 m. skaiciu palyginimas
    # pyrag2022 = np.array([lt2022, uzs2022])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # ax.pie(pyrag2022, labels=pyrag2022, autopct='%1.1f%%', startangle=0, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('Gimusiu vaiku skaicius Lietuvoje ir uzsienyje 2022 metais')
    # plt.show()


    # # 4.Uzsienio salyse gimusiu vaiku skaiciu palyginimas
    # x = np.array(list_of_years)
    # y8 = np.array(list_of_GBR)
    # y9 = np.array(list_of_NOR)
    # y10 = np.array(list_of_DE)
    # y11 = np.array(list_of_IRL)
    # y12 = np.array(list_of_RUS)
    # y13 = np.array(list_of_SWE)
    # y14 = np.array(list_of_ESP)
    # y15 = np.array(list_of_USA)
    # y16 = np.array(list_of_OC)
    #
    # plt.plot(x, y8, color = '#011efe', label = 'D.Britanija')
    # plt.plot(x, y9, color = '#fe00f6', label = 'Norvegija')
    # plt.plot(x, y10, color='#000000', label='Vokietija')
    # plt.plot(x, y11, color='#008744', label='Airija')
    # plt.plot(x, y12, color='#ff0000', label='Rusija')
    # plt.plot(x, y13, color='#071d54', label='Švedija')
    # plt.plot(x, y14, color='#ff7400', label='Ispanija')
    # plt.plot(x, y15, color='#0c6d63', label='JAV')
    # plt.plot(x, y16, color='#002d66', label='Kitos')
    #
    # plt.title('Užsienio šalyse gimusių vaikų skaičių palyginimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.show()


    # # 5.Bendro mirusių per metus žmonių skaičiaus kitimas
    #
    # # linijjine ir stulpeline diagrama
    # x = np.array(list_of_years)
    # y17 = np.array(list_of_mireviso)
    # font1 = {'family': 'sans', 'color': '#120917', 'size': 14}
    # font2 = {'family': 'sans', 'color': '#120917', 'size': 12}
    # plt.plot(x, y17, color='#120917', marker='o', linewidth='2', label='Bendras mirusių žmonių skaičius')
    # plt.bar(x, y17, color = "#4a2f37", width = 0.4)
    # plt.title('Bendro mirusių per metus žmonių skaičiaus kitimas', fontdict=font1)
    # plt.xlabel('Metai', fontdict=font2)
    # plt.ylabel('Mirusių žmonių skaičius', fontdict=font2)
    # plt.legend()
    # plt.show()


    # 6. Mirusiu zmoniu skaiciaus palyginimas pagal lyti

    x = np.array(list_of_years)
    y18 = np.array(list_of_mirev)
    y19 = np.array(list_of_mirem)
    mirev2018 = (y18[0])
    mirem2018 = (y19[0])
    mirev2019 = (y18[1])
    mirem2019 = (y19[1])
    mirev2020 = (y18[2])
    mirem2020 = (y19[2])
    mirev2021 = (y18[3])
    mirem2021 = (y19[3])
    mirev2022 = (y18[4])
    mirem2022 = (y19[4])

    # 2018 m. skaiciu palyginimas
    mire2018 = np.array([mirev2018, mirem2018])
    fig, ax = plt.subplots()
    myexplode = [0.1, 0]
    mycolors = ['#0b2a75', '#c4121a']
    ax.pie(mire2018, labels=mire2018, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    ax.axis('equal')
    plt.title('2018 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    plt.legend(['Vyrai', 'Moterys'])
    plt.show()

    # 2019 m. skaiciu palyginimas
    mire2019 = np.array([mirev2019, mirem2019])
    fig, ax = plt.subplots()
    myexplode = [0.1, 0]
    mycolors = ['#006991', '#ff3030']
    ax.pie(mire2019, labels=mire2019, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    ax.axis('equal')
    plt.title('2019 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    plt.legend(['Vyrai', 'Moterys'])
    plt.show()

    # 2020 m. skaiciu palyginimas
    mire2020 = np.array([mirev2020, mirem2020])
    fig, ax = plt.subplots()
    myexplode = [0.1, 0]
    mycolors = ['#9200ff', '#ffb3ba']
    ax.pie(mire2020, labels=mire2020, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    ax.axis('equal')
    plt.title('2020 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    plt.legend(['Vyrai', 'Moterys'])
    plt.show()

    # 2021 m. skaiciu palyginimas
    mire2021 = np.array([mirev2021, mirem2021])
    fig, ax = plt.subplots()
    myexplode = [0.1, 0]
    mycolors = ['#6aa84f', '#fce069']
    ax.pie(mire2021, labels=mire2021, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    ax.axis('equal')
    plt.title('2021 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    plt.legend(['Vyrai', 'Moterys'])
    plt.show()

    # 2022 m. skaiciu palyginimas
    mire2022 = np.array([mirev2022, mirem2022])
    fig, ax = plt.subplots()
    myexplode = [0.1, 0]
    mycolors = ['#247b61', '#ff8c14']
    ax.pie(mire2022, labels=mire2022, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    ax.axis('equal')
    plt.title('2022 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    plt.legend(['Vyrai', 'Moterys'])
    plt.show()


    # # 7.Mirusių žmonių skaičiaus kitimo tyrimas pagal amziaus grupes
    #
    # x = np.array(list_of_years)
    # y17 = np.array(list_of_mireviso)
    # y20 = np.array(list_of_mire18)
    # y21 = np.array(list_of_mire40)
    # y22 = np.array(list_of_mire60)
    # y23 = np.array(list_of_mire80)
    # y24 = np.array(list_of_mire99)
    #
    # # Bendras mirciu skaicius
    # plt.figure(figsize=(10, 6))
    # plt.plot(x, y17, color='#e80000', marker='o', linewidth='2.5', label='Bendras mirusių žmonių skaičius')
    # plt.title('Bendro mirusių per metus žmonių skaičiaus kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.legend()
    # plt.grid()
    # plt.show()
    #
    # # Zmoniu nuo 0 iki 60 metu mirtingumas
    # plt.figure(figsize=(10, 12))
    # plt.subplot(3, 1, 1)
    # plt.plot(x, y20, marker='o', color='#e80000', linewidth='2.5')
    # plt.title('Nuo 0 iki 18 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.grid()
    # plt.subplot(3, 1, 2)
    # plt.plot(x, y21, marker='o', color='#e80000', linewidth='2.5')
    # plt.title('Nuo 19 iki 40 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.grid()
    # plt.subplot(3, 1, 3)
    # plt.plot(x, y22, marker='o', color='#e80000', linewidth='2.5')
    # plt.title('Nuo 41 iki 60 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.grid()
    # plt.suptitle('Žmonių iki 60 metų mirtingumas Lietuvoje')
    # plt.show()
    #
    # # Zmoniu vyresniu nei 60 metu mirtingumas
    # plt.figure(figsize=(10, 10))
    # plt.subplot(2, 1, 1)
    # plt.plot(x, y23, marker='o', color='#990000', linewidth='2.5')
    # plt.title('Nuo 61 iki 80 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.grid()
    # plt.subplot(2, 1, 2)
    # plt.plot(x, y24, marker='o', color='#990000', linewidth='2.5')
    # plt.title('Vyresnių nei 80 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.grid()
    # plt.suptitle('Žmonių vyresnių nei 60 metų mirtingumas Lietuvoje')
    # plt.show()


    # # 8.Lietuvos zmoniu mirtingumas pagal mirties priezasti
    #
    # x = np.array(list_of_years)
    # y25 = np.array(list_of_infekcija)
    # y26 = np.array(list_of_navikai)
    # y27 = np.array(list_of_diabetas)
    # y28 = np.array(list_of_kraujotaka)
    # y29 = np.array(list_of_kvepavimo)
    # y30 = np.array(list_of_virskinimo)
    # y31 = np.array(list_of_isorpr)
    # y32 = np.array(list_of_transp)
    # y33 = np.array(list_of_nukritimai)
    # y34 = np.array(list_of_paskendimas)
    # y35 = np.array(list_of_alkoholis)
    # y36 = np.array(list_of_savizudybe)
    # y37 = np.array(list_of_nuzudymas)
    # y38 = np.array(list_of_kitospr)
    # y39 = np.array(list_of_covid)
    #
    # x_axis = np.arange(len(x))
    # plt.figure(figsize=(16, 7))
    # plt.bar(x_axis + 0.06, y25, width=0.06, label='Infekcinės ligos')
    # plt.bar(x_axis + 0.06 * 2, y26, width=0.06, label='Piktybiniai navikai')
    # plt.bar(x_axis + 0.06 * 3, y27, width=0.06, label='Cukrinis diabetas')
    # plt.bar(x_axis + 0.06 * 4, y28, width=0.06, label='Kraujotakos ligos')
    # plt.bar(x_axis + 0.06 * 5, y29, width=0.06, label='Kvėpavimo ligos')
    # plt.bar(x_axis + 0.06 * 6, y30, width=0.06, label='Virškinimo ligos')
    # plt.bar(x_axis + 0.06 * 7, y31, width=0.06, label='Išorinės priežastys')
    # plt.bar(x_axis + 0.06 * 8, y32, width=0.06, label='Transporto įvykiai')
    # plt.bar(x_axis + 0.06 * 9, y33, width=0.06, label='Nukritimai')
    # plt.bar(x_axis + 0.06 * 10, y34, width=0.06, label='Paskendimas')
    # plt.bar(x_axis + 0.06 * 11, y35, width=0.06, label='Alkoholio poveikis')
    # plt.bar(x_axis + 0.06 * 12, y36, width=0.06, label='Savižudybė')
    # plt.bar(x_axis + 0.06 * 13, y37, width=0.06, label='Nužudymas')
    # plt.bar(x_axis + 0.06 * 14, y38, width=0.06, label='Kitos priežastys')
    # plt.bar(x_axis + 0.06 * 15, y39, width=0.06, label='Covid-19')
    #
    # plt.xticks(x_axis, x)
    # plt.title('Mirusių žmonių statistika pagal mirties priežastį')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.legend()
    # plt.show()


def main():
    file = 'gimst_mirstam.csv'
    data = load_data(file)

if __name__ == '__main__':
    main()


