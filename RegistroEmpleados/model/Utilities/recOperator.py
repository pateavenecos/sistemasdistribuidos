import csv

class RecOperator:
    def __init__(self, csv_file='employers.csv'):
        self.csv_file = csv_file
        try:
            with open(csv_file, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'name', 'phone', 'address', 'department'])
        except FileExistsError:
            pass

    def add(self, id, name, phone, address, department):
        data = self._read_all()
        if any(row['id'] == id for row in data):
            raise ValueError("ID already exists")
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id, name, phone, address, department])

    def read(self, id=None):
        data = self._read_all()
        if id is None:
            return data
        for row in data:
            if row['id'] == id:
                return row
        raise KeyError("ID not found")

    def update(self, id, **kwargs):
        if 'id' in kwargs:
            raise ValueError("Cannot update ID")
        data = self._read_all()
        found = False
        for i, row in enumerate(data):
            if row['id'] == id:
                for key, value in kwargs.items():
                    if key in row:
                        row[key] = value
                found = True
                break
        if not found:
            raise KeyError("ID not found")
        self._write_all(data)

    def delete(self, id):
        data = self._read_all()
        new_data = [row for row in data if row['id'] != id]
        if len(new_data) == len(data):
            raise KeyError("ID not found")
        self._write_all(new_data)

    def _read_all(self):
        with open(self.csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _write_all(self, data):
        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'phone', 'address', 'department'])
            writer.writeheader()
            writer.writerows(data)