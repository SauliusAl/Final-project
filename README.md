**_Final-project_**
Projekto Autoriai:
Saulius Stankevičius
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
Šiam projektui atlikti duomenys buvo paimti iš oficialios Lietuvoje veikiančios statistikos departamento pateikiamos
internetinės svetainės.

**Techniniai reikalavimai**

Projekto atlikimui reikalinga pasinaudoti: "pandas", "numpy", "matplotlib" ar "Seaborn". Siekiant atlikti išsamią 
analizę reikalinga naudotis Git biblioteka. Projekto metu reikalinga atlikti šiuos veiksmus:
1) Duomenų rinkimas;
2) Duomenų valymas ir transformacija;
3) Statistinė analizė;
4) Vizualizacija;
5) Išvados.

**Duomenų rinkimas ir analizė**

Lietuvoje oficiali staistinė informacija pateikiama internetiniame puslapyje www.stat.gov.lt. Projekto atlikimui
buvp pasirinktas metų intervalas 2018-2022 metai. Duomenų atrinkimas, filtravimas, rūšiavimas ir perkėlimas buvo
vykdomas pasinaudojus Excel.
Pradžioje duomenys buvo suskirstyti pagal temas atskiruose puslapiuose. Duomenų perkėlimui į Python programą 
ir jų apdorojimui duomenys sukelti į vieną Excel puslapį ir konvertuoti csv formatu.
Python programoje pradžioje buvo sukurta funkcija duomenų nuskaitymui nuo csv failo.
Kiekvienam duomanų faile esamam stulpeliui buvo sukurti sąrašai (list), panaudodami funkciją "to_list()".
Iš gautų sąrašų "numpy" funkcijos array pagalba kuriame reikiamus kintamuosius. Taip pat pasinaudoję "numpy"
funkcijomis (sum, min, max, average) atliekame keletą statistinių skaičiavimų duomenų vizualizacijai.


**Duomenų valymas ir transformacija**

Pagrindinis duomenų valymas ir korekcija buvo atlikti Excel lentelėje. Kaip buvo paminėta duomenų rinkimo ir analizės
skiltyje, duomenų transformacija buvo atlikta csv formate į Python programą.


**Duomenų vizualizacija**

Matplotlib bibliotekų (pie, bar) pagalba kuriamos reikiamos diagramos, turimas sąrašas išskaidomas į atskirus elementus,
kad pritaikius sąrašo indeksus palyginame vieno sąrašo elementą su kito sąrašo elementu.
Projekto metu buvo sukurtos šios diagramos:
- gimusių vaikų analizė (dvi diagramos (skaitinė išraiška ir procentinė išraiška nuo bendro gyventojų skaičiaus));
- gimusių lietuvių vaikų užsienyje duomenų analizė, palyginimas su vaikų gimimu Lietuvoje (penkios pie diagramos);
- vidutinio gimdančių moterų amžiaus vidurkio analizė (viena diagrama);
- užsienyje gimusių vaikų duomenys pagal atskiras šalis (viena linijinė diagrama);
- bendras mirusiųjų žmonių skaičius kiekvienais metais (viena stulpelinė diagrama);
- procentinė mirusių žmonių išraiška palygiminui su žmonių skaičiumi Lietuvoje (viena linijinė diagrama);
- mirusiųjų žmonių išskirstymas pagal lytis kiekvienais metais (penkios pie diagramos);
- bendras mirusių žmonių skaičiaus kitimas per 5 metus (viena linijinė diagrama);
- mirčių analizė pagal amžiaus grupes (penkios linijinės diagramos);
- mirčių analizė pagal pagrindines priežastis (viena stulpelinė diagrama);
- metinė gimimo-mirčių kitimo diagrama (viena linijinė diagrama);
- gimimo-mirčių suminė procentinė analizė kartu su prognoze (viena linijinė diagrama)


**Išvados**

Atlikome Lietuvos gyventojų gimimo ir mirties analizę 2018 - 2022 metais. Iš atrinktų duomenų galima daryti bendrines
išvadas, kad gyventojų skaičius Lietuvoje tendencingai mažėja. Iš pateiktų vizualiai matomų duomenų matyti, kad 
mažėja vaikų gimstamumas ir didėja žmonių mirštamumas, t.y. bendras gimimo - mirčių balansas yra neigiams, t.y. šalies
gyventojų mirtingumas kiekvienais metais auga, o gimstamumas atvirkščiai - krinta.
Viena vertus, tai susiję su mažu suminio gimstamymo rodikliu, t.y. mažu rodikliu, kiek vidutiniškai viena moteris 
pagimdo vaikų. Kita vertus, yra bendras gyventojų skaičiaus mažėjimas, kuris dalinai susijęs ir su emigracija, ir su 
ekonominiais šalies rodikliais.
Tuo tarpu mirusiųjų gyventojų skaičius gana didelis ir jis didėja kiekvienais metais. Tiesa, 2022 metų mirčių rodiklius
koregavo nauja liga - Covid pandemija.
Demografinė padėtis skaudžiai keičiasi regionuose. Gyventojai nuolat iš rajonų keliasi į didesnius miestus ar aplamai
emigruoja. tai susiję su darbo trūkumu regionuose.
Nors šis tiriamasis - analitinis projektas nepalietė tokių temų, kaip politikiai / ekonominiai veiksniai gyventojų
demografijos klausimais, galima daryti prielaidą, kad šie veiksniai iš esmės yra kertiniai ir gali keisti bendrą 
situaciją tiek Lietuvoje, tiek ir atskiruose regionuose.







8. Kuriant "pie" diagrama, reikės turimą sąrašą išskaidyti į atskirus elementus, tad pritaikius sąrašo indeksus, galėsim nesunkiai vieno sąrašo elementą palyginti su kito sąrašo elementu.
9. Pirma kuriama diagrama - gimdžiusių moterų vidutinio amžiaus analizė.
10. Antra diagrama - gimusių vaikų skaičiaus analizė, greta diagramos pateikiamos statistinių paskaičiavimų (sum, min, max ir average) formulės.
11. Greta aktualios vaikų gimimo skaičiaus diagramos dar pateikiam metinį procentinį gimstamumo rodiklį (gimusių vaikų skaičius padalintas iš šalies gyventojų skaičiaus sausio 01 dienai).
12. Tuomet bandome sukurti "pie" diagramą, pavaizduoti lietuvių vaikų, gimusių užsienyje, skaičiaus palyginimą su gimusiais Lietuvoje per penkių analizuojamų metų laikotarpį.
13. Tada sukuriame diagramą, kurioje pateiksime užsienyje gimusių vaikų skaičius, pagal šalis ir papildomai sumą visų užsienyje gimusių vaikų.
14. Tuomet analizuojame mirusių statistinius duomenis. Kuriame mirusių žmonių skaičiaus kitimo, per penkis metus, diagramą bei kitus statistinius paskaičiavimus (sum, min, max, average).
15. Sekanti diagrama - tai mirusių žmonių skaičiaus palyginimas su šalies gyventojų skaičiumi - gauname procentinį pokyčio rodiklį.
16. Toliau kuriame mirusių žmonių skaičiaus palyginimą pagal lytį "pie" diagramos pagalba.
17. Sekanti analizė - mirusių skaičiaus tyrimas, atsižvelgiant į amžiaus grupes.
18. Tuomet bandome paanalizuoti mirusių skaičių pagal mirties priežastį (stulpelinė diagrama), greta paskaičiuojame kiekvienos grupės mirčių sumą per visus tiriamus metus.
19. Ir pabaigai gimimų ir mirčių bendro palyginimo analizė - paskaičiuojame suminius gimimų-mirčių kasmetinius rezultatus ir nubraižome linijinė kitimo diagramą.
20. Tuomet dar kasmetinio pokyčio procentinį rodiklį ir jo kitimo per penkis metus linijinę diagramą.