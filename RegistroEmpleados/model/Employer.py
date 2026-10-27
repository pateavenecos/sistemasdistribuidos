class Employer:
    def __init__(self, id: int, name: str, phone: str, address: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_phone(self) -> str:
        return self.phone

    def get_address(self) -> str:
        return self.address

    def __repr__(self):
        return f"Employer(id={self.id}, name='{self.name}')"
