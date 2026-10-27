from Employer import Employer


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employers: list[Employer] = []

    def get_name(self) -> str:
        return self.name

    def add_employer(self, employer: Employer):
        self.employers.append(employer)

    def remove_employer(self, employer_id: int):
        self.employers = [e for e in self.employers if e.id != employer_id]

    def get_employers(self) -> list[Employer]:
        return self.employers

    def __repr__(self):
        return f"Department(name='{self.name}', employers={len(self.employers)})"
