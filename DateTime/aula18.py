from datetime import datetime

d1 = datetime(2024, 5, 12)
print(d1)
d1 = datetime(2024, 5, 12, 12, 56, 34)

# strptime("Data", "Formato")
d2 = datetime.strptime("12/5/2024", "%d/%m/%Y")
d3 = datetime.strptime("2012-09-21", "%Y-%m-%d")
print(d2)
print(d3)