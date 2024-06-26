from dataclasses import dataclass, asdict, astuple,field


@dataclass
class Person:
    name: str = field(default="Missing")
    last_name: str = field(default="Not Send")
    age: int = field(default=0)
    addresses: list[int] = field(default_factory=list)
    


if __name__ == "__main__":
    p1 = Person("John", "Doe", 31)
    print(p1)
    print(asdict(p1))
    print(astuple(p1))
    p2 = Person()
    print(p2)