import csv


def get_words():
    words=[]
    with open('words.csv',newline='')as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            words.append(row[0])

        print(len(words))
    return words

