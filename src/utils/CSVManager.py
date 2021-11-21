import csv
from math import sqrt


class CSVManager:
    """Luokka csv-tiedostojen kasittelyyn"""

    def save_to_file(self, arr, name):
        """Tallentaa yksiulotteisen list-rakenteisen kartan tiedostoon
        annetulla nimella csv-muodossa"""
        length = int(sqrt(len(arr)))
        rows = []
        for x in range(length):
            rows.append(arr[x * length : (x + 1) * length])

        with open(name, "w", newline="") as f:
            write = csv.writer(f)
            write.writerows(rows)

    def open_file(self, name):
        """Avaa csv-muotoisen tiedoston ja palauttaa sen yksiuloitteisena
        list-rakenteena"""

        result = []
        try:
            with open(name, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    result += row
        except Exception:
            raise FileNotFoundError("File not found")

        try:
            for elem in result:
                int(elem)
        except Exception:
            raise ValueError("File contains invalid values")

        return result
