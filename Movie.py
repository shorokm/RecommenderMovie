import csv
                    
with open('userReviews.csv', encoding='utf-8-sig') as reviews:
  reader = csv.DictReader(reviews,delimiter= ';')
  data = list(reader)

# Puts the values of the column Author in the list X
X = list()
for row in data:
  X.append(row['Author'])

print(X)

#Filters reviews based on a specific movie and puts it in list Y
Y = list()
for row in data:
  if row['movieName'] == 'harry-potter-and-the-order-of-the-phoenix':
    Y.append(row['Author'])

print(Y)

#Looks for the other movies autors in list Y have watched and puts it in list Z
Z = list()
for row in data:
  if row['Author'] in Y:
    Z.append(row['movieName'])
    
print(Z)


#Makes a textfile with the results of Z
textfile = open('resultsZ.txt','w')
for element in Z:
    textfile.write(element+"\n")
textfile.close()