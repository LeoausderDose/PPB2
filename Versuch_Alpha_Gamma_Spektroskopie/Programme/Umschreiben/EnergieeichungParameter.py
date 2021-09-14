import numpy as np
import pandas as pd

daten = 'Versuch_Alpha_Gamma_Spektroskopie/Umschreiben/Energieeichung.csv'
df = pd.read_csv(daten)

print(df)

parameter = np.polyfit(df['Topf'], df['Energie'],1)
print(parameter)