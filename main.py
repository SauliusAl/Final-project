# Baigiamasis darbas
# Projekto tema: Gimusių ir mirusių analizė Lietuvoje

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
    list_of_gyvsk = data['gyv_skaic'].to_list()
    list_of_gimproc = data['gimst_proc'].to_list()
    list_of_mirproc = data['mirt_proc'].to_list()
    list_of_pokyt = data['pokyt_proc'].to_list()


    # # 1.Gimdanciu moteru amziaus diagrama
    #
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


    # # 2.Gimusiu vaiku skaiciaus analize
    #
    # x = np.array(list_of_years)
    # y0 = np.array(list_of_gyvsk)
    # y3 = np.array(list_of_gimev)
    # y4 = np.array(list_of_gimeb)
    # y5 = np.array(list_of_gimem)
    # gim_5m_suma = np.sum(y3)
    # gim_5m_min = np.min(y3)
    # gim_5m_max = np.max(y3)
    # gim_5m_avg = np.average(y3)
    # print(f'Suminis 2018-2022 metais gimusių vaikų skaičius yra: {gim_5m_suma}')
    # print(f'2018-2022 metais mažiausiai ({gim_5m_min}) vaikų gimė {x} metais')
    # print(f'2018-2022 metais daugiausiai ({gim_5m_max}) vaikų gimė {x} metais')
    # print(f'2018-2022 metais vidutiniškai per metus gimdavo {int(gim_5m_avg)} vaikų')
    # plt.plot(x, y3, color = '#8a2be2', marker = 'o', label = 'Bendras')
    # plt.plot(x, y4, marker = 'o', label = 'Berniukai')
    # plt.plot(x, y5, marker = 'o', color='#fb607f', label='Mergaitės')
    # plt.title('Gimusių vaikų skaičiaus kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.grid()
    # plt.show()
    #
    # # Gimimu metinis procentinis rodiklis, vertinant salies gyventoju skaiciu
    # gimimu_metinis_pokytis = (y3 / y0) * 100
    # print(f'2018 metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[0], 2)} %')
    # print(f'2019 metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[1], 2)} %')
    # print(f'2020 metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[2], 2)} %')
    # print(f'2021 metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[3], 2)} %')
    # print(f'2022 metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[4], 2)} %')
    # plt.plot(x, gimimu_metinis_pokytis, color='#8a2be2', marker='o')
    # plt.title('Procentinio metinio gimimų rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimimų procentinis rodiklis %')
    # plt.grid()
    # plt.show()


    # # 3.Gimusiu vaiku uzsienyje skaiciaus palyginimas su gimusiais Lietuvoje
    #
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


    # # 4.Uzsienio salyse gimusiu vaiku skaiciu analize
    #
    # x = np.array(list_of_years)
    # y7 = np.array(list_of_uzs)
    # y8 = np.array(list_of_GBR)
    # y9 = np.array(list_of_NOR)
    # y10 = np.array(list_of_DE)
    # y11 = np.array(list_of_IRL)
    # y12 = np.array(list_of_RUS)
    # y13 = np.array(list_of_SWE)
    # y14 = np.array(list_of_ESP)
    # y15 = np.array(list_of_USA)
    # y16 = np.array(list_of_OC)

    # gim_uzs_5m_suma = np.sum(y7)
    # print(f'2018-2022 metais užsienyje gimusių lietuvių vaikų skaičius yra: {gim_uzs_5m_suma}')
    # plt.plot(x, y8, color = '#011efe', label = 'D.Britanija')
    # plt.plot(x, y9, color = '#fe00f6', label = 'Norvegija')
    # plt.plot(x, y10, color='#000000', label='Vokietija')
    # plt.plot(x, y11, color='#008744', label='Airija')
    # plt.plot(x, y12, color='#ff0000', label='Rusija')
    # plt.plot(x, y13, color='#071d54', label='Švedija')
    # plt.plot(x, y14, color='#ff7400', label='Ispanija')
    # plt.plot(x, y15, color='#0c6d63', label='JAV')
    # plt.plot(x, y16, color='#002d66', label='Kitos')
    # plt.title('Užsienio šalyse gimusių vaikų skaičių palyginimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.show()


    # # 5.Bendro mirusių per metus žmonių skaičiaus analize
    #
    # # linijjine ir stulpeline diagrama
    # x = np.array(list_of_years)
    # y17 = np.array(list_of_mireviso)
    # mirc_5m_suma = np.sum(y17)
    # mirc_5m_min = np.min(y17)
    # mirc_5m_max = np.max(y17)
    # mirc_5m_avg = np.average(y17)
    # print(f'2018-2022 metais mirusių žmonių skaičius yra: {mirc_5m_suma}')
    # print(f'2018-2022 metais mažiausiai ({mirc_5m_min}) žmonių mirė {x} metais')
    # print(f'2018-2022 metais daugiausiai ({mirc_5m_max}) žmonių mirė {x} metais')
    # print(f'2018-2022 metais vidutiniškai per metus mirdavo {int(mirc_5m_avg)} žmonių')
    # font1 = {'family': 'sans', 'color': '#000000', 'size': 14}
    # font2 = {'family': 'sans', 'color': '#000000', 'size': 12}
    # plt.plot(x, y17, color='#000000', marker='o', linewidth='2', label='Bendras mirusių žmonių skaičius')
    # plt.bar(x, y17, color = '#666666', width = 0.4)
    # plt.title('Bendro mirusių per metus žmonių skaičiaus kitimas', fontdict=font1)
    # plt.xlabel('Metai', fontdict=font2)
    # plt.ylabel('Mirusių žmonių skaičius', fontdict=font2)
    # plt.legend()
    # plt.show()

    # # Mirciu metinis procentinis rodiklis, vertinant salies gyventoju skaiciu
    # y0 = np.array(list_of_gyvsk)
    # mirciu_metinis_pokytis = (y17 / y0) * 100
    # print(f'2018 metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[0], 2)} %')
    # print(f'2019 metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[1], 2)} %')
    # print(f'2020 metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[2], 2)} %')
    # print(f'2021 metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[3], 2)} %')
    # print(f'2022 metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[4], 2)} %')
    # plt.plot(x, mirciu_metinis_pokytis, color='#800000', marker='o')
    # plt.title('Procentinio metinio mirčių rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirčių procentinis rodiklis %')
    # plt.grid()
    # plt.show()


    # # 6. Mirusiu zmoniu skaiciaus palyginimas pagal lyti
    #
    # x = np.array(list_of_years)
    # y18 = np.array(list_of_mirev)
    # y19 = np.array(list_of_mirem)
    # mirev2018 = (y18[0])
    # mirem2018 = (y19[0])
    # mirev2019 = (y18[1])
    # mirem2019 = (y19[1])
    # mirev2020 = (y18[2])
    # mirem2020 = (y19[2])
    # mirev2021 = (y18[3])
    # mirem2021 = (y19[3])
    # mirev2022 = (y18[4])
    # mirem2022 = (y19[4])
    #
    # # 2018 m. skaiciu palyginimas
    # mire2018 = np.array([mirev2018, mirem2018])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # mycolors = ['#0b2a75', '#c4121a']
    # ax.pie(mire2018, labels=mire2018, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('2018 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()
    #
    # # 2019 m. skaiciu palyginimas
    # mire2019 = np.array([mirev2019, mirem2019])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # mycolors = ['#006991', '#ff3030']
    # ax.pie(mire2019, labels=mire2019, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('2019 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()
    #
    # # 2020 m. skaiciu palyginimas
    # mire2020 = np.array([mirev2020, mirem2020])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # mycolors = ['#9200ff', '#ffb3ba']
    # ax.pie(mire2020, labels=mire2020, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('2020 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()
    #
    # # 2021 m. skaiciu palyginimas
    # mire2021 = np.array([mirev2021, mirem2021])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # mycolors = ['#6aa84f', '#fce069']
    # ax.pie(mire2021, labels=mire2021, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('2021 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()
    #
    # # 2022 m. skaiciu palyginimas
    # mire2022 = np.array([mirev2022, mirem2022])
    # fig, ax = plt.subplots()
    # myexplode = [0.1, 0]
    # mycolors = ['#247b61', '#ff8c14']
    # ax.pie(mire2022, labels=mire2022, colors = mycolors, autopct='%1.1f%%', startangle=90, explode = myexplode, shadow = True)
    # ax.axis('equal')
    # plt.title('2022 metais mirusių vyrų ir moterų skaičiaus palyginimas')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()


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
    # mirc_infekc_suma = np.sum(y25)
    # mirc_navik_suma = np.sum(y26)
    # mirc_diabet_suma = np.sum(y27)
    # mirc_krauj_suma = np.sum(y28)
    # mirc_kvepav_suma = np.sum(y29)
    # mirc_virskin_suma = np.sum(y30)
    # mirc_isorpr_suma = np.sum(y31)
    # mirc_transp_suma = np.sum(y32)
    # mirc_nukrit_suma = np.sum(y33)
    # mirc_paskend_suma = np.sum(y34)
    # mirc_alkoh_suma = np.sum(y35)
    # mirc_savizud_suma = np.sum(y36)
    # mirc_nuzud_suma = np.sum(y37)
    # mirc_kitospr_suma = np.sum(y38)
    # mirc_covid_suma = np.sum(y39)
    #
    # print(f'2018-2022 metais nuo infekcinių ligų mirė {mirc_infekc_suma} žmonės')
    # print(f'2018-2022 metais nuo piktybinių navikų ligų mirė {mirc_navik_suma} žmonės')
    # print(f'2018-2022 metais nuo cukrinio diabeto komplikacijų mirė {mirc_diabet_suma} žmonės')
    # print(f'2018-2022 metais nuo kraujotakos sistemos ligų mirė {mirc_krauj_suma} žmonės')
    # print(f'2018-2022 metais nuo kvėpavimo sistemos ligų mirė {mirc_kvepav_suma} žmonės')
    # print(f'2018-2022 metais nuo virškinimo sistemos ligų mirė {mirc_virskin_suma} žmonės')
    # print(f'2018-2022 metais nuo išorinių priežasčių mirė {mirc_isorpr_suma} žmonės')
    # print(f'2018-2022 metais nuo transporto įvykių mirė {mirc_transp_suma} žmonės')
    # print(f'2018-2022 metais nuo nukritimų mirė {mirc_nukrit_suma} žmonės')
    # print(f'2018-2022 metais nuo netyčinių paskendimų mirė {mirc_paskend_suma} žmonės')
    # print(f'2018-2022 metais nuo alkoholio sukeltų komplikacijų mirė {mirc_alkoh_suma} žmonės')
    # print(f'2018-2022 metais nusižudė {mirc_savizud_suma} žmonių')
    # print(f'2018-2022 metais buvo nužudyti {mirc_nuzud_suma} žmonės')
    # print(f'2018-2022 metais nuo kitų priežasčių mirė {mirc_kitospr_suma} žmonės')
    # print(f'2018-2022 metais nuo Covid-19 mirė {mirc_covid_suma} žmonių')
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
    # plt.xticks(x_axis, x)
    # plt.title('Mirusių žmonių statistika pagal mirties priežastį')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.legend()
    # plt.show()


    # # 9.Gimimu ir mirciu bendro rezultato tyrimas
    #
    # x = np.array(list_of_years)
    # y0 = np.array(list_of_gyvsk)
    # y3 = np.array(list_of_gimev)
    # y17 = np.array(list_of_mireviso)
    # rezultatas = y3 - y17
    # print(f'2018 metų gimimų-mirčių suminis rezultatas: {round(rezultatas[0], 2)}')
    # print(f'2019 metų gimimų-mirčių suminis rezultatas: {round(rezultatas[1], 2)}')
    # print(f'2020 metų gimimų-mirčių suminis rezultatas: {round(rezultatas[2], 2)}')
    # print(f'2021 metų gimimų-mirčių suminis rezultatas: {round(rezultatas[3], 2)}')
    # print(f'2022 metų gimimų-mirčių suminis rezultatas: {round(rezultatas[4], 2)}')
    # plt.plot(x, rezultatas, color='#8a2be2', marker='o', linewidth='3')
    # plt.title('Metinio gimimo-mirčių rezultato kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Metinis gimimų-mirčių rezultatas')
    # plt.grid()
    # plt.show()
    #
    # gimimu_metinis_pokytis = (y3 / y0) * 100
    # mirciu_metinis_pokytis = (y17 / y0) * 100
    # rezultatas_proc = gimimu_metinis_pokytis - mirciu_metinis_pokytis
    # print(f'2018 metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[0], 2)} %')
    # print(f'2019 metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[1], 2)} %')
    # print(f'2020 metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[2], 2)} %')
    # print(f'2021 metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[3], 2)} %')
    # print(f'2022 metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[4], 2)} %')
    # plt.plot(x, rezultatas_proc, color='#8a2be2', marker='o', linewidth='3', label='Rodiklis')
    # plt.title('Gimimų-mirčių suminio procentinio rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimimų-mirčių suminis procentinis rodiklis %')
    # tendencija = np.polyfit(x, rezultatas_proc, 1)
    # prognoze = np.polyval(tendencija, x)
    # plt.plot(x, prognoze, color='red', label='Prognozė')
    # plt.legend()
    # plt.grid()
    # plt.show()



def main():
    file = 'gimst_mirstam.csv'
    data = load_data(file)
if __name__ == '__main__':
    main()


