import csv


def delete_symbols(message):
    message = line.replace("\t", " ")
    message = line.replace("\r", " ")
    message = line.replace("\n", " ")
    return message


a = []
from_who = []
date = []
to = []
theme = []
messages = []

text = ""
with open("export.txt", "r", encoding="utf-8", newline='') as file:
    for line in file:
        # a.append(line)
        if "От:" in line:
            from_who.append(line[4:line.find("\r\n")])
            messages.append(text)
            text = ""
        elif "Отправлено:" in line:
            date.append(line[12:line.find("\r\n")])
        elif "Кому:" in line:
            to.append(line[6:line.find("\r\n")])
        elif "Тема:" in line:
            theme.append(line[6:line.find("\r\n")])
        else:
            line = delete_symbols(line)
            text += line
for message in messages:
    if message == "":
        messages.remove(message)

with open("export.csv", "w", newline="") as target_file:
    writer = csv.writer(target_file, delimiter=';')
    for from_who_items, date_items, to_items, theme_items, messages_items in zip(from_who, date, to, theme, messages):
        writer.writerow([from_who_items] + [date_items] + [to_items] + [theme_items] + [messages_items])


