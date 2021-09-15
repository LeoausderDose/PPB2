import numpy as np
import pandas as pd
from scipy import optimize as opt
import matplotlib.pyplot as plt

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

#Plot machen
plt.plot(df['Dicke'],df['Zaehlrate (1/s)'], marker = 'x', color = 'r', ls = 'None')
plt.plot(np.linspace(0,df.iloc[-1,0]*1.1,100),Zerfall(np.linspace(0,df.iloc[-1,0]*1.1,100),popt[0],popt[1],popt[2]))
plt.show()