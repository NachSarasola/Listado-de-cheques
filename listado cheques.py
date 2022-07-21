import pandas as pd
import sys
from datetime import datetime

data = pd.read_csv('cheques.csv')
dt = datetime.now()

DNI = int(input('Ingrese su DNI: '))

if DNI not in data['DNI'].values.tolist():
    print('DNI inexistente, intentelo de nuevo')
    sys.exit()

tipoCheque = input('Ingrese el tipo de cheque (EMITIDO O DEPOSITADO): ').upper()

if tipoCheque not in data['Tipo'].values.tolist():
    print('Cheque inexistente, intentelo de nuevo')
    sys.exit()

estadoCheque = input('Ingrese el estado del cheque (APROBADO, RECHAZADO o PENDIENTE): ').upper()

if estadoCheque not in data['Estado'].values.tolist():
    print('Cheque inexistente, intentelo de nuevo')
    sys.exit()

datoCliente = data[(data["DNI"] == (DNI)) & (data["Tipo"].str.contains(tipoCheque)) &(data["Estado"].str.contains(estadoCheque))]

# str.contains revisa un dato tipo string

salida = input('Ingrese el formato de salida de los datos(PANTALLA o CSV): ').upper()
if salida == 'PANTALLA':
 print(datoCliente)
elif salida == 'CSV':
 datoCliente.to_csv(f'{DNI}-{dt}.csv')
 print('Archivo CSV creado con éxito')