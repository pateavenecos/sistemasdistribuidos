from Department import Department


class Company:
    def __init__(self, name: str):
        self.name = name
        self.departments: list[Department] = []

    def get_name(self) -> str:
        return self.name

    def add_department(self, department: Department):
        self.departments.append(department)

    def remove_department(self, department_name: str):
        self.departments = [d for d in self.departments if d.name != department_name]

    def get_departments(self) -> list[Department]:
        return self.departments

    def __repr__(self):
        return f"Company(name='{self.name}', departments={len(self.departments)})"
