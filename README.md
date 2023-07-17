**_Final-project_**
Projekto autoriai:
Saulius Stankevičius,
Saulius Aleksa

Projekto tema: "Gimusių ir mirusių žmonių analizė Lietuvoje"

**Turinys**
    * Projekto apžvalga;
    * Techniniai reikalavimai;
    * Duomenų rinkimas ir analizė;
    * Duomenų vizualizacija;
    * Išvados;
    * Duomenų šaltiniai.

**Projekto apžvalga**

Pagrindinė projekto užduotis išanalizuoti Lietuvos gyventojų gimstamumo ir mirštamumo duomenis, juos vizualizuoti
grafiškai ir pristatyti išvadas.
Šiam projektui atlikti duomenys buvo paimti iš oficialios statistikos portalo.

**Techniniai reikalavimai**

Projekto atlikimui reikia pasinaudoti: "pandas", "numpy", "matplotlib" ar "seaborn" bibliotekomis. Siekiant atlikti  
išsamią analizę, reikia naudotis Git biblioteka. Projekto metu reikia atlikti šiuos veiksmus:
1) Duomenų rinkimas;
2) Duomenų valymas ir transformacija;
3) Statistinė analizė;
4) Vizualizacija;
5) Išvados.

**Duomenų rinkimas ir analizė**

Lietuvoje oficiali staistinė informacija pateikiama internetiniame puslapyje www.osp.stat.gov.lt. Projekto atlikimui
buvp pasirinktas metų intervalas 2018-2022 metai. Duomenų atrinkimas, filtravimas, rūšiavimas ir perkėlimas buvo
vykdomas pasinaudojus Excel.
Pradžioje duomenys buvo suskirstyti pagal temas atskiruose puslapiuose. Duomenų perkėlimui į Python programą 
ir jų apdorojimui duomenys sukelti į vieną Excel puslapį ir konvertuoti į csv formatą.
Python programoje pradžioje buvo sukurta funkcija duomenų nuskaitymui iš csv failo.
Kiekvienam duomenų faile esamam stulpeliui buvo sukurtas sąrašas (list), panaudodami funkcija "to_list()".
Iš gautų sąrašų "numpy" funkcijos array pagalba sukurėme reikiamus kintamuosius. Taip pat pasinaudoję "numpy"
funkcijomis (sum, min, max, average) atlikome keletą statistinių skaičiavimų duomenų vizualizacijai.


**Duomenų valymas ir transformacija**

Pagrindinis duomenų valymas ir korekcija buvo atlikti Excel lentelėje. Kaip buvo paminėta duomenų rinkimo ir analizės
skiltyje, duomenų transformacija buvo atlikta csv formatu į Python programą.


**Duomenų vizualizacija**

Matplotlib bibliotekos pagalba buvo kuriamos reikiamos diagramos (line, pie, bar), turimas sąrašas išskaidomas
į atskirus elementus, kad pritaikius sąrašo indeksus galėtume palyginti vieno sąrašo elementą su kito sąrašo elementu.
Projekto metu buvo sukurtos šios diagramos:
- vidutinio gimdančių moterų amžiaus analizė (viena linijinė diagrama);
- gimusių vaikų analizė (dvi linijinės diagramos (skaitinė išraiška ir procentinė išraiška nuo bendro gyventojų skaičiaus));
- gimusių lietuvių vaikų užsienyje duomenų analizė (palyginamoji linijinė diagrama), 
  bei palyginimas su vaikų gimimu Lietuvoje (pie diagrama, išvestas 5m vidurkis);
- užsienyje gimusių vaikų duomenys pagal atskiras šalis (viena linijinė diagrama);
- 2018-2022m mirusių žmonių Lietuvoje pagal lytį vidurkis (pie diagrama);
- bendra mirusiųjų žmonių analizė Lietuvoje kiekvienais metais (stulpelinė diagrama);
- mirčių analizė Lietuvoje pagal amžiaus grupes (penkios linijinės diagramos ir viena pie diagrama);
- mirčių analizė Lietuvoje pagal mirties priežastis (stulpelinė diagrama, pie diagrama);
- metinė gimimo-mirčių Lietuvoje suminė diagrama (linijinė diagrama);
- gimimo-mirčių Lietuvoje suminė procentinė analizė (linijinė diagrama).


**Išvados**

Atlikome Lietuvos gyventojų 2018 - 2022 metų gimimo ir mirties analizę. 
Remiantis pateikta informacija, Lietuvoje 2018-2022 metais gimsta vis mažiau vaikų. 2022 m. gimė 22 068 kūdikiai, 
tai yra net 21,6 proc. mažiau nei 2018 metais. O mirtingumas didėja. 2022 metais mirė 42 884 žmonės,
tai yra 8,4 proc. daugiau nei 2018 metais.

Ši tendencija yra susijusi su keliais veiksniais, įskaitant:

- Vyresnė populiacija. Lietuvos gyventojai sensta, o tai reiškia, kad miršta daugiau žmonių nei gimsta.
- Sumažėjęs gimstamumas. Lietuvos gimstamumas mažėja jau keletą metų. Tai susiję su įvairiais veiksniais, įskaitant 
ekonomikos sunkumus, darbo rinkos nestabilumą ir moterų sveikatos priežiūros prieinamumą.
- Padidėjusi emigracija. Daugelis jaunų žmonių iš Lietuvos išvyksta ieškoti geresnio gyvenimo kitose šalyse. 
Tai mažina šalies gyventojų skaičių ir taip pat turi įtakos gimstamumui.

Be to demografinė padėtis skaudžiai keičiasi regionuose. Gyventojai nuolat iš rajonų keliasi į didesnius miestus ar 
emigruoja. Tai susiję su darbo trūkumu regionuose.
Nors šis tiriamasis - analitinis projektas nepalietė tokių temų, kaip politiniai ar ekonominiai veiksniai gyventojų
demografijos klausimais, galima daryti prielaidą, kad šie veiksniai iš esmės yra kertiniai ir gali koreguoti  
situaciją tiek Lietuvoje, tiek ir atskiruose regionuose.

Situacija Lietuvoje nėra unikali. Daugelis kitų Europos šalių taip pat susiduria su panašiais iššūkiais. 
Ši tendencija greičiausiai tęsis ir ateityje, o tai turės rimtų pasekmių šalių ekonomikai ir socialinei gerovei.
