import csv
from math import sqrt

class CSVManager():
    '''Luokka csv-tiedostojen kasittelyyn'''
    
    def saveToFile(self, arr, name):
        '''Tallentaa yksiulotteisen list-rakenteisen kartan tiedostoon annetulla nimella csv-muodossa'''
        length = int(sqrt(len(arr)))
        rows = []
        for x in range(length):
            rows.append(arr[x*length:(x+1)*length])

        with open(name, 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(rows)
        
    def openFile(self, name):
        '''Avaa csv-muotoisen tiedoston ja palauttaa sen yksiuloitteisena list-rakenteena'''
        
        result = []
        try:
            with open(name, newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        result += row
        except:
            raise FileNotFoundError("File not found")

        try:
            for elem in result:
                int(elem)
        except:
            raise ValueError("File contains invalid values")

        return result