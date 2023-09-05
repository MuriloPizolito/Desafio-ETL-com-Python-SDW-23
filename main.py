import pandas as pd
import matplotlib.pyplot as plt 

arquivo_pedidos = 'pedidos.xlsx'
arquivo_valores = 'valores.xlsx'

df_pedidos = pd.read_excel(arquivo_pedidos)
df_valores = pd.read_excel(arquivo_valores)

#print (df_pedidos, df_valores)

df_total = df_pedidos.merge(df_valores, on=('ID'))


print (df_total)


df_total.groupby('ID').sum().plot(kind='bar')


plt.show()
