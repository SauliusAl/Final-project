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


    # # 1.Gimdanciu moteru amziaus analize - linijine diagrama
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
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    #
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
    # gimev2018 = y3[0]
    # gimev2019 = y3[1]
    # gimev2020 = y3[2]
    # gimev2021 = y3[3]
    # gimev2022 = y3[4]
    # gimeb2018 = y4[0]
    # gimeb2019 = y4[1]
    # gimeb2020 = y4[2]
    # gimeb2021 = y4[3]
    # gimeb2022 = y4[4]
    # gimem2018 = y5[0]
    # gimem2019 = y5[1]
    # gimem2020 = y5[2]
    # gimem2021 = y5[3]
    # gimem2022 = y5[4]
    #
    # # spausdiname statistinius rodiklius
    # print(f'2018-2022 metais viso gimė {gim_5m_suma} vaikų')
    # print(f'2018-2022 metais mažiausiai ({gim_5m_min}) vaikų gimė 2022 metais')
    # print(f'2018-2022 metais daugiausiai ({gim_5m_max}) vaikų gimė 2018 metais')
    # print(f'2018-2022 metais vidutiniškai per metus gimdavo {int(gim_5m_avg)} vaikų')
    #
    # # Linijine gimusiu vaiku diagrama
    #
    # plt.plot(x, y3, color='#8a2be2', marker='o', label='Bendras')
    # plt.plot(x, y4, color='#0a75ad', marker='o', label='Berniukai')
    # plt.plot(x, y5, color='#fb607f', marker='o', label='Mergaitės')
    # plt.text(2018-0.1, 26850, gimev2018, fontsize=10, color='#8a2be2')
    # plt.text(2019-0.15, 26000, gimev2019, fontsize=10, color='#8a2be2')
    # plt.text(2020-0.15, 23750, gimev2020, fontsize=10, color='#8a2be2')
    # plt.text(2021-0.15, 22000, gimev2021, fontsize=10, color='#8a2be2')
    # plt.text(2022-0.3, 20700, gimev2022, fontsize=10, color='#8a2be2')
    # plt.text(2018-0.1, 15000, gimeb2018, fontsize=10, color='#0a75ad')
    # plt.text(2019-0.15, 14600, gimeb2019, fontsize=10, color='#0a75ad')
    # plt.text(2020-0.15, 13700, gimeb2020, fontsize=10, color='#0a75ad')
    # plt.text(2021-0.15, 12500, gimeb2021, fontsize=10, color='#0a75ad')
    # plt.text(2022-0.3, 12200, gimeb2022, fontsize=10, color='#0a75ad')
    # plt.text(2018-0.1, 12600, gimem2018, fontsize=10, color='#fb607f')
    # plt.text(2019-0.2, 12200, gimem2019, fontsize=10, color='#fb607f')
    # plt.text(2020-0.2, 10950, gimem2020, fontsize=10, color='#fb607f')
    # plt.text(2021-0.2, 10300, gimem2021, fontsize=10, color='#fb607f')
    # plt.text(2022-0.3, 10000, gimem2022, fontsize=10, color='#fb607f')
    # plt.title('Gimusių vaikų skaičiaus kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių per metus vaikų skaičius')
    # plt.legend()
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    #
    # # Gimimu metinis procentinis rodiklis, vertinant salies gyventoju skaiciu
    #
    # gimimu_metinis_pokytis = (y3 / y0) * 100
    # # spausdiname
    # for i in range(gimimu_metinis_pokytis.size):
    #     print(f'{i + 2018} metų gimimų procentinis rodiklis: {round(gimimu_metinis_pokytis[i], 2)} %')
    #
    # # Procentinio rodiklio linijine diagrama
    #
    # plt.plot(x, gimimu_metinis_pokytis, color='#8a2be2', marker='o')
    # plt.title('Procentinio metinio gimimų rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimimų procentinis rodiklis %')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    # #
    #
    # # 3.Uzsienio salyse gimusiu lietuviu vaiku skaiciu analize
    #
    # # Viso 2018-2022 m. uzsienyje gimusiu lietuviu vaiku suma
    # # spausdiname
    # y7 = np.array(list_of_uzs)
    # gim_uzs_5m_suma = np.sum(y7)
    # print(f'2018-2022 metais užsienyje gimusių lietuvių vaikų skaičius yra: {gim_uzs_5m_suma}')
    #
    # # Gimusiu lietuviu vaiku Lietuvoje ir uzsienyje 2018-2022 m. palyginimo linijine diagrama
    #
    # x = np.array(list_of_years)
    # y6 = np.array(list_of_LT)
    # y7 = np.array(list_of_uzs)
    # gimeLT2018 = y6[0]
    # gimeLT2019 = y6[1]
    # gimeLT2020 = y6[2]
    # gimeLT2021 = y6[3]
    # gimeLT2022 = y6[4]
    # gimeUZS2018 = y7[0]
    # gimeUZS2019 = y7[1]
    # gimeUZS2020 = y7[2]
    # gimeUZS2021 = y7[3]
    # gimeUZS2022 = y7[4]
    # plt.figure(figsize=(9, 6))
    # plt.plot(x, y6, color='#000000', marker='o', linewidth='2', label='Gimė Lietuvoje')
    # plt.plot(x, y7, color='red',marker='o', linewidth='2', label='Gimė užsienyje')
    # plt.text(2018, 24200, gimeLT2018, fontsize=12, color='#000000')
    # plt.text(2019, 22300, gimeLT2019, fontsize=12, color='#000000')
    # plt.text(2020, 21600, gimeLT2020, fontsize=12, color='#000000')
    # plt.text(2021, 20700, gimeLT2021, fontsize=12, color='#000000')
    # plt.text(2022-0.2, 19600, gimeLT2022, fontsize=12, color='#000000')
    # plt.text(2018, 3000, gimeUZS2018, fontsize=12, color='red')
    # plt.text(2019, 4100, gimeUZS2019, fontsize=12, color='red')
    # plt.text(2020, 2700, gimeUZS2020, fontsize=12, color='red')
    # plt.text(2021, 1600, gimeUZS2021, fontsize=12, color='red')
    # plt.text(2022-0.1, 1250, gimeUZS2022, fontsize=12, color='red')
    # plt.title('Gimusių vaikų Lietuvoje ir užsienyje skaičių palyginimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Vaikų skaičius')
    # plt.legend()
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    # # Gimusiu lietuviu vaiku LT-UZS 2018-2022 m. vidurkio palyginimo "pie" diagrama
    #
    # gimeLT_5m_vid = np.average(y6)
    # gimeUZS_5m_vid = np.average(y7)
    # gime_salys_5m_vid = np.array([int(gimeLT_5m_vid), int(gimeUZS_5m_vid)])
    # fig, ax = plt.subplots(figsize=(8, 6))
    # myexplode = [0.1, 0]
    # mycolors = ['#247b61', '#ff8c14']
    # ax.pie(gime_salys_5m_vid, labels=gime_salys_5m_vid, colors=mycolors, autopct='%1.1f%%', startangle=335,
    # explode=myexplode)
    # ax.axis('equal')
    # plt.title('2018-2022 m. gimusių vaikų Lietuvoje ir užsienyje vidurkių palyginimas')
    # plt.legend(['Lietuvoje', 'Užsienyje'])
    # plt.show()
    #
    # # Gimusiu lietuviu vaiku ivairiose uzsienio salyse skaiciu palyginamoji linijine diagrama
    #
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
    # plt.title('Užsienio šalyse gimusių vaikų skaičių palyginimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimusių vaikų skaičius')
    # plt.legend()
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    #
    # # 4. Mirusiu zmoniu Lietuvoje analize
    #
    # # 2018-2022 m. mirusiu zmoniu skaiciu pagal lyti vidurkiu "pie" diagrama
    #
    # x = np.array(list_of_years)
    # y18 = np.array(list_of_mirev)
    # y19 = np.array(list_of_mirem)
    # mirev_5m_vid = np.average(y18)
    # mirem_5m_vid = np.average(y19)
    # mire_lytis_5m_vid = np.array([int(mirev_5m_vid), int(mirem_5m_vid)])
    # fig, ax = plt.subplots(figsize=(8, 6))
    # myexplode = [0.1, 0]
    # mycolors = ['#247b61', '#ff8c14']
    # ax.pie(mire_lytis_5m_vid, labels=mire_lytis_5m_vid, colors=mycolors, autopct='%1.1f%%', startangle=270,
    # explode=myexplode)
    # ax.axis('equal')
    # plt.title('2018-2022 m. mirusių žmonių pagal lytį vidurkis')
    # plt.legend(['Vyrai', 'Moterys'])
    # plt.show()
    #
    #
    # # Bendro ir pagal amziaus grupes mirtingumo analize
    #
    # x = np.array(list_of_years)
    # y17 = np.array(list_of_mireviso)
    # y20 = np.array(list_of_mire18)
    # y21 = np.array(list_of_mire40)
    # y22 = np.array(list_of_mire60)
    # y23 = np.array(list_of_mire80)
    # y24 = np.array(list_of_mire99)
    # mireviso2018 = (y17[0])
    # mireviso2019 = (y17[1])
    # mireviso2020 = (y17[2])
    # mireviso2021 = (y17[3])
    # mireviso2022 = (y17[4])
    # mire18_2018 = (y20[0])
    # mire18_2019 = (y20[1])
    # mire18_2020 = (y20[2])
    # mire18_2021 = (y20[3])
    # mire18_2022 = (y20[4])
    # mire40_2018 = (y21[0])
    # mire40_2019 = (y21[1])
    # mire40_2020 = (y21[2])
    # mire40_2021 = (y21[3])
    # mire40_2022 = (y21[4])
    # mire60_2018 = (y22[0])
    # mire60_2019 = (y22[1])
    # mire60_2020 = (y22[2])
    # mire60_2021 = (y22[3])
    # mire60_2022 = (y22[4])
    # mire80_2018 = (y23[0])
    # mire80_2019 = (y23[1])
    # mire80_2020 = (y23[2])
    # mire80_2021 = (y23[3])
    # mire80_2022 = (y23[4])
    # mire99_2018 = (y24[0])
    # mire99_2019 = (y24[1])
    # mire99_2020 = (y24[2])
    # mire99_2021 = (y24[3])
    # mire99_2022 = (y24[4])
    # mire18_5m_suma = np.sum(y20)
    # mire40_5m_suma = np.sum(y21)
    # mire60_5m_suma = np.sum(y22)
    # mire80_5m_suma = np.sum(y23)
    # mire99_5m_suma = np.sum(y24)
    # mire18_5m_vid = np.average(y20)
    # mire40_5m_vid = np.average(y21)
    # mire60_5m_vid = np.average(y22)
    # mire80_5m_vid = np.average(y23)
    # mire99_5m_vid = np.average(y24)
    # mirc_5m_suma = np.sum(y17)
    # mirc_5m_min = np.min(y17)
    # mirc_5m_max = np.max(y17)
    # mirc_5m_avg = np.average(y17)
    #
    # # 2018-2022 m. bendrieji mirtingumo rodikliai
    #
    # # spausdiname sum, min, max, average rodiklius
    # print(f'2018-2022 metais mirusių žmonių skaičius yra: {mirc_5m_suma}')
    # print(f'2018-2022 metais mažiausiai ({mirc_5m_min}) žmonių mirė 2019 metais')
    # print(f'2018-2022 metais daugiausiai ({mirc_5m_max}) žmonių mirė 2021 metais')
    # print(f'2018-2022 metais vidutiniškai per metus mirdavo {int(mirc_5m_avg)} žmonių')
    #
    # # Bendro mirtingumo linijine-stulpeline diagrama
    #
    # font1 = {'family': 'sans', 'color': '#000000', 'size': 14}
    # font2 = {'family': 'sans', 'color': '#000000', 'size': 12}
    # plt.figure(figsize=(12, 6))
    # plt.plot(x, y17, color='#000000', marker='o', linewidth='2', label='Bendras mirusių žmonių skaičius')
    # plt.bar(x, y17, color = '#666666', width = 0.4)
    # plt.text(2018 - 0.15, 37000, mireviso2018, fontsize=14, color='#ffffff')
    # plt.text(2019 - 0.15, 35700, mireviso2019, fontsize=14, color='#ffffff')
    # plt.text(2020 - 0.15, 40800, mireviso2020, fontsize=14, color='#ffffff')
    # plt.text(2021 - 0.15, 45000, mireviso2021, fontsize=14, color='#ffffff')
    # plt.text(2022 - 0.15, 40100, mireviso2022, fontsize=14, color='#ffffff')
    # plt.title('Bendro mirusių per metus žmonių skaičiaus kitimas', fontdict=font1)
    # plt.xlabel('Metai', fontdict=font2)
    # plt.ylabel('Mirusių žmonių skaičius', fontdict=font2)
    # plt.legend()
    # plt.show()
    #
    # # Mirtingumo metinis procentinis rodiklis, ivertinantis salies gyventoju skaiciu
    #
    # x = np.array(list_of_years)
    # y17 = np.array(list_of_mireviso)
    # y0 = np.array(list_of_gyvsk)
    # mirciu_metinis_pokytis = (y17 / y0) * 100
    #
    # # spausdiname
    # for i in range(mirciu_metinis_pokytis.size):
    #     print(f'{i + 2018} metų mirčių procentinis rodiklis: {round(mirciu_metinis_pokytis[i], 2)} %')
    #
    # # Linijine diagrama
    #
    # plt.plot(x, mirciu_metinis_pokytis, color='#800000', marker='o')
    # plt.title('Procentinio metinio mirčių rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirčių procentinis rodiklis %')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    # # Analize pagal amziaus grupes
    #
    # # Zmoniu nuo 0 iki 60 metu mirtingumo linijines diagramos (trys amziaus grupe)
    #
    # plt.figure(figsize=(10, 12))
    # plt.subplot(3, 1, 1)
    # plt.plot(x, y20, marker='o', color='#e80000', linewidth='2.5')
    # plt.text(2018 - 0.1, 195, mire18_2018, fontsize = 14, color='#e80000')
    # plt.text(2019, 188, mire18_2019, fontsize= 14, color='#e80000')
    # plt.text(2020, 175, mire18_2020, fontsize= 14, color='#e80000')
    # plt.text(2021, 162, mire18_2021, fontsize= 14, color='#e80000')
    # plt.text(2022 - 0.1, 140, mire18_2022, fontsize= 14, color='#e80000')
    # plt.title('Nuo 0 iki 18 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.subplot(3, 1, 2)
    # plt.plot(x, y21, marker='o', color='#e80000', linewidth='2.5')
    # plt.text(2018 + 0.25, 1120, mire40_2018, fontsize = 14, color='#e80000')
    # plt.text(2019, 1030, mire40_2019, fontsize= 14, color='#e80000')
    # plt.text(2020 + 0.2, 1000, mire40_2020, fontsize= 14, color='#e80000')
    # plt.text(2021 + 0.15, 1100, mire40_2021, fontsize= 14, color='#e80000')
    # plt.text(2022 - 0.4, 980, mire40_2022, fontsize= 14, color='#e80000')
    # plt.title('Nuo 19 iki 40 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.subplot(3, 1, 3)
    # plt.plot(x, y22, marker='o', color='#e80000', linewidth='2.5')
    # plt.text(2018, 5550, mire60_2018, fontsize = 14, color='#e80000')
    # plt.text(2019 + 0.2, 5350, mire60_2019, fontsize= 14, color='#e80000')
    # plt.text(2020, 6000, mire60_2020, fontsize= 14, color='#e80000')
    # plt.text(2021 + 0.2, 6350, mire60_2021, fontsize= 14, color='#e80000')
    # plt.text(2022 - 0.4, 5400, mire60_2022, fontsize= 14, color='#e80000')
    # plt.title('Nuo 41 iki 60 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.suptitle('Žmonių iki 60 metų mirtingumas Lietuvoje')
    # plt.show()
    #
    # # Zmoniu vyresniu nei 60 metu mirtingumo linijines diagramos (dvi amziaus grupes)
    #
    # plt.figure(figsize=(10, 10))
    # plt.subplot(2, 1, 1)
    # plt.plot(x, y23, marker='o', color='#990000', linewidth='2.5')
    # plt.text(2018, 15750, mire80_2018, fontsize = 14, color='#e80000')
    # plt.text(2019 + 0.2, 15000, mire80_2019, fontsize= 14, color='#e80000')
    # plt.text(2020 + 0.1, 17000, mire80_2020, fontsize= 14, color='#e80000')
    # plt.text(2021 + 0.15, 18900, mire80_2021, fontsize= 14, color='#e80000')
    # plt.text(2022 - 0.2, 16600, mire80_2022, fontsize= 14, color='#e80000')
    # plt.title('Nuo 61 iki 80 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.subplot(2, 1, 2)
    # plt.plot(x, y24, marker='o', color='#990000', linewidth='2.5')
    # plt.text(2018, 17500, mire99_2018, fontsize = 14, color='#e80000')
    # plt.text(2019 + 0.2, 16800, mire99_2019, fontsize= 14, color='#e80000')
    # plt.text(2020 + 0.08, 18700, mire99_2020, fontsize= 14, color='#e80000')
    # plt.text(2021 + 0.2, 20900, mire99_2021, fontsize= 14, color='#e80000')
    # plt.text(2022 - 0.2, 18900, mire99_2022, fontsize= 14, color='#e80000')
    # plt.title('Vyresnių nei 80 metų', loc = 'left')
    # plt.xlabel('Metai')
    # plt.ylabel('Mirusių žmonių skaičius')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.suptitle('Žmonių vyresnių nei 60 metų mirtingumas Lietuvoje')
    # plt.show()
    #
    # # 2018-2022 m. mirusiu zmoniu suminiu skaiciu ir vidurkio pagal amziu grupes palyginamoji "pie" diagrama
    #
    # mire_5m_proc = np.array([mire18_5m_suma, mire40_5m_suma, mire60_5m_suma, mire80_5m_suma, mire99_5m_suma])
    # fig, ax = plt.subplots(figsize=(8, 6))
    # myexplode = [0.2, 0.2, 0.05, 0.05, 0.05]
    # mycolors = ['#0b2a75', '#c4121a', '#065535', '#794044', '#696969']
    # ax.pie(mire_5m_proc, labels=mire_5m_proc, colors=mycolors, autopct='%1.1f%%', startangle=0, explode=myexplode)
    # ax.axis('equal')
    # plt.title('2018-2022 m. mirusių žmonių suminiai skaičiai ir vidurkiai pagal amžiaus grupes')
    # plt.text(1.48, 0, int(mire18_5m_vid), fontsize=10, color='#cc0000')
    # plt.text(1.5, 0.12, int(mire40_5m_vid), fontsize=10, color='#cc0000')
    # plt.text(1.22, 0.638, int(mire60_5m_vid), fontsize=10, color='#cc0000')
    # plt.text(-1.245, 0.852, int(mire80_5m_vid), fontsize=10, color='#cc0000')
    # plt.text(0.485, -1.147, int(mire99_5m_vid), fontsize=10, color='#cc0000')
    # plt.text(-1.737, -1.233, 'xxx - metinis vidurkis', fontsize=10, color='#cc0000')
    # plt.legend(['iki 18 metų', '19-40 metų', '41-60 metų', '61-80 metų', '>80 metų'], loc=(-0.1, 0))
    # plt.show()
    #
    # # 2018-2022 m. Lietuvos zmoniu mirciu pagal mirties priezasti analize
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
    # # Mirtingumo pagal mirties priezasti 2018-2022 m. stulpeline diagrama
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
    #
    # # 2018-2022 m. Lietuvos zmoniu mirciu pagal mirties priezasti sumos
    #
    # # spausdiname
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
    # # 2018-2022 m. mirciu sumu pagal mirties priezasti "pie" diagrama
    #
    # mire_5m_ligos_proc = np.array([mirc_infekc_suma, mirc_diabet_suma, mirc_krauj_suma, mirc_navik_suma,
    #                                mirc_kvepav_suma, mirc_paskend_suma, mirc_virskin_suma, mirc_alkoh_suma,
    #                                mirc_isorpr_suma, mirc_transp_suma, mirc_kitospr_suma, mirc_nukrit_suma,
    #                                mirc_savizud_suma, mirc_nuzud_suma, mirc_covid_suma])
    # fig, ax = plt.subplots(figsize=(9, 6))
    # myexplode = [0.5, 0.5, 0.03, 0.02, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    # mycolors = ['#0b2a75', '#c4121a', '#065535', '#794044', '#696969', '#8a2be2', '#daa520', '#0e2f44', '#ff6666',
    #             '#660066', '#c39797', '#468499', '#f08080', '#20b2aa', '#cbbeb5']
    # ax.pie(mire_5m_ligos_proc, labels=mire_5m_ligos_proc, colors=mycolors, autopct='%1.1f%%', startangle=30,
    #        explode=myexplode)
    # ax.axis('equal')
    # plt.title('2018-2022 m. mirusių žmonių skaičiaus palyginimas pagal mirties priežastį')
    # plt.legend(['Infekcinės ligos', 'Cukrinis diabetas', 'Kraujotakos ligos', 'Piktybiniai navikai', 'Kvėpavimo ligos',
    #             'Paskendimas', 'Virškinimo ligos', 'Alkoholio poveikis', 'Išorinės priežastys', 'Transporto įvykiai',
    #             'Kitos priežastys', 'Nukritimai', 'Savižudybė', 'Nužudymas', 'Covid-19'], loc=(-0.1, 0))
    # plt.show()
    #
    #
    # # 5.Gimimu ir mirciu bendro rezultato analize
    #
    # x = np.array(list_of_years)
    # y0 = np.array(list_of_gyvsk)
    # y3 = np.array(list_of_gimev)
    # y17 = np.array(list_of_mireviso)
    # rezultatas = y3 - y17
    #
    # # spausdiname 2018-2022 m. bendrus rezultatus
    # for i in range(rezultatas.size):
    #     print(f'{i + 2018} metų gimimų-mirčių suminis rezultatas: {round(rezultatas[i], 2)}')
    #
    # # Gimimu-mirciu rezultatu linijine diagrama
    #
    # plt.figure(figsize=(12, 8))
    # plt.plot(x, rezultatas, color='#8a2be2', marker='o', linewidth='3')
    # plt.text(2018, -12200, (rezultatas[0]), fontsize = 13, color='#5e0c67')
    # plt.text(2019 + 0.1, -11000, (rezultatas[1]), fontsize= 13, color='#5e0c67')
    # plt.text(2020, -18000, (rezultatas[2]), fontsize= 13, color='#5e0c67')
    # plt.text(2021 - 0.4, -24500, (rezultatas[3]), fontsize= 13, color='#5e0c67')
    # plt.text(2022 - 0.25, -20500, (rezultatas[4]), fontsize= 13, color='#5e0c67')
    # plt.title('Metinio gimimo-mirčių rezultato kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Metinis gimimų-mirčių rezultatas')
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()
    #
    # # Rezultato kitimo per 2018-2022 metus procentine israika
    #
    # gimimu_metinis_pokytis = (y3 / y0) * 100
    # mirciu_metinis_pokytis = (y17 / y0) * 100
    # rezultatas_proc = gimimu_metinis_pokytis - mirciu_metinis_pokytis
    #
    # # spausdiname procentini rodikli
    # for i in range(rezultatas_proc.size):
    #     print(f'{i + 2018} metų gimimų-mirčių suminis procentinis rodiklis: {round(rezultatas_proc[i], 2)} %')
    #
    # # Suminio procentinio rodiklio kitimo ir prognozes linijine diagrama
    #
    # plt.plot(x, rezultatas_proc, color='#8a2be2', marker='o', linewidth='3', label='Rodiklis')
    # plt.title('Gimimų-mirčių suminio procentinio rodiklio kitimas')
    # plt.xlabel('Metai')
    # plt.ylabel('Gimimų-mirčių suminis procentinis rodiklis %')
    # tendencija = np.polyfit(x, rezultatas_proc, 1)
    # prognoze = np.polyval(tendencija, x)
    # plt.plot(x, prognoze, color='red', label='Prognozė')
    # plt.legend()
    # plt.xlim([2018-0.25, 2022+0.25])
    # plt.xticks(range(2018, 2023, 1))
    # plt.grid()
    # plt.show()


def main():
    file = 'gimst_mirstam.csv'
    data = load_data(file)
if __name__ == '__main__':
    main()
