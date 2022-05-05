import csv
csv.register_dialect("Разделитель", delimiter=";", lineterminator="\n")
b = {}
lines2 = []
def write_in_file(dictionary):
    with open("export.csv", "a") as target_file:
        fieldnames = dictionary.keys()
        writer = csv.DictWriter(target_file, dialect='Разделитель', fieldnames=fieldnames)
        writer.writerow(dictionary)


with open("export2.txt", "r", encoding="utf-8") as file:
    lines = file.read().split("\n")
target_lines = []
for line in lines:
    print(line)
    if "Zabbix" in line:
        string = line
    elif "Мониторинг" in line:
        string += " " + line
        target_lines.append(string)
    else:
        target_lines.append(line)
print(target_lines)
# for line in target_lines:
#     if line == "":
#         target_lines.remove(line)
# lines2 = []
# for line in target_lines:
#     line2 = line.replace("\t", ' ')
#     lines2.append(line2)
# for line in lines2:
#     if "Малашенко" in line:
#         lines2.remove(line)
# print(lines2)