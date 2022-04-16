import numpy as np   # pentru vectori si shuffle
import statistics    # pentru calcularea mediei
import math          # pentru radicalul de la deviatie
import matplotlib.pyplot as plt   # pentru grafice


# retinem intr-un vector datele din fisierul numit "Vin.txt" de tip string, pe care le separam prin punct si virgula

data = np.loadtxt("Vin.txt", dtype='str', delimiter=";")

np.random.shuffle(data)   # dam shuffle la elementele din vector

data = np.asarray(data, dtype=float)   # modificam din str in float ca sa putem lucra cu ele


# declaram un vector pentru fiecare atribut al vinului rosu

Aciditate_Fixa = []

Aciditate_Volatila = []

Aciditate_Citrica = []

Zahar_Rezidual = []

Cloruri = []

Dioxid_de_sulf_total = []

Dioxid_de_sulf_liber = []

Densitate = []

ph = []

Sulfat = []

Alcool = []

Calitate = []


# parcurgem vectorul si retinem valorile de pe linie in functie de atribut

for i in range(0, 200):
    Aciditate_Fixa.append(data[i][0])
    Aciditate_Volatila.append(data[i][1])
    Aciditate_Citrica.append(data[i][2])
    Zahar_Rezidual.append(data[i][3])
    Cloruri.append(data[i][4])
    Dioxid_de_sulf_liber.append(data[i][5])
    Dioxid_de_sulf_total.append(data[i][6])
    Densitate.append(data[i][7])
    ph.append(data[i][8])
    Sulfat.append(data[i][9])
    Alcool.append(data[i][10])
    Calitate.append(data[i][11])


def media(x):                           # facem media
    return statistics.mean(x)



print("Media:")
print("\n")


print("Aciditate fixa medie: ", media(Aciditate_Fixa))
print("\n")

print("Aciditate volatila medie: ", media(Aciditate_Volatila))
print("\n")

print("Aciditate citrica medie: ", media(Aciditate_Citrica))
print("\n")

print("Media cantitatii de zahar rezidual: ", media(Zahar_Rezidual))
print("\n")

print("Media cantitatii de cloruri: ", media(Cloruri))
print("\n")

print("Media cantitatii de dioxid de sulf liber: ", media(Dioxid_de_sulf_liber))
print("\n")

print("Media cantitatii de dioxid de sulf total: ", media(Dioxid_de_sulf_total))
print("\n")

print("Densitatea medie: ", media(Densitate))
print("\n")

print("Media pH-ului: ", media(ph))
print("\n")

print("Media cantitatii de sulfat: ", media(Sulfat))
print("\n")

print("Media procentului de alcool", media(Alcool))
print("\n")

print("Calitatea medie: ", media(Calitate))
print("\n")

print("\n \n \n")


def dispersia(lst):                 # facem dispersia
    m = media(lst)
    d = []
    for i in lst:
        d.append((m - i) ** 2)
    return media(d)


print("Dispersia:")
print("\n")


print("Dispersia aciditatii fixe: ", "{:.3f}".format(dispersia(Aciditate_Fixa)))
print("\n")

print("Dispersia aciditatii volatile: ", "{:.3f}".format(dispersia(Aciditate_Volatila)))
print("\n")

print("Dispersia aciditatii citrice: ", "{:.3f}".format(dispersia(Aciditate_Citrica)))
print("\n")

print("Dispersia cantitatii de zahar rezidual: ", "{:.3f}".format(dispersia(Zahar_Rezidual)))
print("\n")

print("Dispersia cantitatii de cloruri: ", "{:.3f}".format(dispersia(Cloruri)))
print("\n")

print("Dispersia dioxidului de sulf liber: ", "{:.3f}".format(dispersia(Dioxid_de_sulf_liber)))
print("\n")

print("Dispersia dioxidului de sulf total: ", "{:.3f}".format(dispersia(Dioxid_de_sulf_total)))
print("\n")

print("Dispersia densitatii: ", "{:.3f}".format(dispersia(Densitate)))
print("\n")

print("Dispersia pH-ului: ", "{:.3f}".format(dispersia(ph)))
print("\n")

print("Dispersia cantitatii de sulfat: ", "{:.3f}".format(dispersia(Sulfat)))
print("\n")

print("Dispersia alcoolului: ", "{:.3f}".format(dispersia(Alcool)))
print("\n")

print("Dispersia calitatii: ", "{:.3f}".format(dispersia(Calitate)))
print("\n")

print("\n \n \n")


def deviatia_standard(x):                   # facem deviatia standard
    return math.sqrt(dispersia(x))


print("Deviatia Standard:")
print("\n")

print("Deviatia standard a aciditatii fixe: ", "{:.3f}".format(deviatia_standard(Aciditate_Fixa)))
print("\n")

print("Deviatia standard a aciditatii volatile: ", "{:.3f}".format(deviatia_standard(Aciditate_Volatila)))
print("\n")

print("Deviatia standard a aciditatii citrice: ", "{:.3f}".format(deviatia_standard(Aciditate_Citrica)))
print("\n")

print("Deviatia standard a cantitatii de zahar rezidual: ", "{:.3f}".format(deviatia_standard(Zahar_Rezidual)))
print("\n")

print("Deviatia standard a cantitatii de cloruri: ", "{:.3f}".format(deviatia_standard(Cloruri)))
print("\n")

print("Deviatia standard a dioxidului de sulf liber: ", "{:.3f}".format(deviatia_standard(Dioxid_de_sulf_liber)))
print("\n")

print("Deviatia standard a dioxidului de sulf total: ", "{:.3f}".format(deviatia_standard(Dioxid_de_sulf_total)))
print("\n")

print("Deviatia standard a densitatii: ", "{:.3f}".format(deviatia_standard(Densitate)))
print("\n")

print("Deviatia standard a pH-ului: ", "{:.3f}".format(deviatia_standard(ph)))
print("\n")

print("Deviatia standard a cantitatii de sulfat: ", "{:.3f}".format(deviatia_standard(Sulfat)))
print("\n")

print("Deviatia standard a alcoolului: ", "{:.3f}".format(deviatia_standard(Alcool)))
print("\n")

print("Deviatia standard a calitatii: ", "{:.3f}".format(deviatia_standard(Calitate)))
print("\n")

print("\n \n \n")


def interval_de_incredere(x):                       # facem intervalul de incredere
    s = media(x) - 2 * deviatia_standard(x)
    d = media(x) + 2 * deviatia_standard(x)
    return ["{:.3f}".format(s), "{:.3f}".format(d)]


print("Intervalul de Incredere:")
print("\n")


print("Intervalul de incredere al aciditatii fixe: ", interval_de_incredere(Aciditate_Fixa))
print("\n")

print("Intervalul de incredere al aciditatii volatile: ", interval_de_incredere(Aciditate_Volatila))
print("\n")

print("Intervalul de incredere al aciditatii citrice: ", interval_de_incredere(Aciditate_Citrica))
print("\n")

print("Intervalul de incredere al cantitatii de zahar rezidual: ", interval_de_incredere(Zahar_Rezidual))
print("\n")

print("Intervalul de incredere al cantitatii de cloruri: ", interval_de_incredere(Cloruri))
print("\n")

print("Intervalul de incredere al cantitatii de dioxid de sulf liber: ", interval_de_incredere(Dioxid_de_sulf_liber))
print("\n")

print("Intervalul de incredere al cantitatii de dioxid de sulf total: ", interval_de_incredere(Dioxid_de_sulf_total))
print("\n")

print("Intervalul de incredere al densitatii: ", interval_de_incredere(Densitate))
print("\n")

print("Intervalul de incredere al pH-ului: ", interval_de_incredere(ph))
print("\n")

print("Intervalul de incredere al cantitatii de sulfat: ", interval_de_incredere(Sulfat))
print("\n")

print("Intervalul de incredere al procentului de alcool", interval_de_incredere(Alcool))
print("\n")

print("Intervalul de incredere al calitatii: ", interval_de_incredere(Calitate))
print("\n")

print("\n \n \n")



plt.scatter(Calitate,Alcool)   #Grafic pentru a observa raportul Calitate/Alcool:
plt.xlabel('Calitate')
plt.ylabel('Alcool')
plt.suptitle('Calitate/Alcool')
plt.show()



plt.scatter(Calitate,Zahar_Rezidual)   #Grafic pentru a observa raportul Calitate/Zahar:
plt.xlabel('Calitate')
plt.ylabel('Zahar rezidual')
plt.suptitle('Calitate/Zahar rezidual')
plt.show()



plt.scatter(Calitate,Densitate)   # Grafic pentru a observa raportul Calitate/Densitate:
plt.xlabel('Calitate')
plt.ylabel('Densitate')
plt.suptitle('Calitate/Densitate')
plt.show()



plt.scatter(Calitate,Cloruri)   #Grafic pentru a observa raportul Calitate/Cloruri:
plt.xlabel('Calitate')
plt.ylabel('Cloruri')
plt.suptitle('Calitate/Cloruri')
plt.show()



plt.scatter(Calitate,ph)   #Grafic pentru a observa raportul Calitate/pH:
plt.xlabel('Calitate')
plt.ylabel('pH')
plt.suptitle('Calitate/pH')
plt.show()
