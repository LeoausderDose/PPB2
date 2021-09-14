import numpy as np
import pandas as pd
from scipy import optimize as opt

#Deklaration
def Zerfall(x, A0, mu, rausch):
    return A0*np.exp(-x*mu)+rausch







daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/CSV/AbsobtionskoeffizeintAlu.csv'
df = pd.read_csv(daten)

df['Zaehlrate (1/s)'] = df['Integral']/df['Zeit']

#Fitten des Graphen
popt, pcov = opt.curve_fit(Zerfall, df['Dicke'],df['Zaehlrate (1/s)'])

perr = np.sqrt(np.diag(pcov))

print(popt)
print(perr)