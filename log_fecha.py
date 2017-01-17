import datetime

f = open("l:\\log.txt", "a")
feacha_actual= datetime.date.today(.strftime("%d-%m-%a"))
f.write(fecha_actual + "\n")




