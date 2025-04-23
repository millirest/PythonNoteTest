import csv

data1 = {}
with open('test2.csv', encoding="utf-8") as f:
    reader = csv.DictReader(f,delimiter=";")
    for row in reader:
        print(row)
    data1 = list(reader)
print("")

print(data1)
print("")
# Сортируем участников по убыванию баллов
sorted_filter_player = dict(sorted(data1.items(), key=lambda x: x[0], reverse=True))
print(sorted_filter_player)
for id, tittle, body, time in sorted_filter_player.items():
    print(f"{id}) {tittle} {body}, {time}\n")
# Открываем файл second_tour.txt для записи
# with open("second_tour.txt", "w") as file:
# # Записываем данные участников с нумерацией
#     for id, tittle, body, time in sorted_filter_player.items():
#         file.write(f"{id}) {tittle} {body}, {time}\n")