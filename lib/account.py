from dataclasses import dataclass

@dataclass
class Account:
    id: int
    username: str
    email_address: str