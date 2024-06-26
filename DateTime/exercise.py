from datetime import datetime
from dateutil.relativedelta import relativedelta
total_value = 1_000_000

data_emprestimo = datetime.now()
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

num_parcelas = len(data_parcelas)
valor_parcela = total_value / num_parcelas
for data in data_parcelas:
    print(data.strftime("%d/%m/%Y"), f"R${valor_parcela:,.2f}")

print(num_parcelas)