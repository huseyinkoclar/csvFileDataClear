#script what delete rows from csv file if the second column is in a text file

fileName = "inputforcheck.csv"
textName = "inputforcontains.txt"

#read textname file and store in a list
with open(textName) as file:
    txt = file.read().splitlines()


#read csv file and store in a list
with open(fileName) as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]

#create and fill csv file 
with open('output.csv', 'w') as file:
    file.write(header[0])
    for row in rows:
        if len(row.split(',')) > 1:
            if not row.split(',')[1] in txt:
                file.write(row)
            else:
                print(row.split(',')[1] + " is in the list")
