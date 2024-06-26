from datetime import datetime

ftm = '%d/%m/%Y'

data = datetime.strptime('2022-12-13 07:56:22', "%Y-%m-%d %H:%M:%S")
print(data.strftime(ftm))
print(data.strftime(f"{ftm} %H:%M"))
print(data.strftime(f"{ftm} %H:%M:%S"))
print(data.strftime("%Y"))