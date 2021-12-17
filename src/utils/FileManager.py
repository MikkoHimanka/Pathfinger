import csv
from math import sqrt


class FileManager:
    """Luokka tiedostojen kasittelyyn"""

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
        """Avaa tiedoston ja palauttaa sen yksiuloitteisena
        list-rakenteena"""
        extension = name[-3::1]
        result = []
        try:
            with open(name, newline="") as file:
                if extension == "csv":
                    reader = csv.reader(file)
                    for row in reader:
                        result += row
                elif extension == "map":
                    file = open(name)
                    file.readline()
                    next_line = file.readline()
                    height = int(next_line.strip().split(' ')[1])
                    next_line = file.readline()
                    width = int(next_line.strip().split(' ')[1])
                    if height > 512:
                        raise ValueError("Map is too large")
                    file.readline()
                    while True:
                        row = []
                        next_line = file.readline().strip()
                        if not next_line:
                            break
                        for char in next_line:
                            if char == '@':
                                row.append('1')
                            if char == '.':
                                row.append('0')
                        if height > width:
                            row += ['1' for _ in range(height - width)]
                        result += row
                    if width > height:
                        result += ['1' for _ in range(width)] * (width - height)
        except Exception:
            raise FileNotFoundError("File not found")

        try:
            for elem in result:
                int(elem)
        except Exception:
            raise ValueError("File contains invalid values")

        return result
