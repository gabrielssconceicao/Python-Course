import enum


class Directions(enum.Enum):
    LEFT = 1
    RIGHT = 2
    UP = enum.auto()


print(Directions(1), Directions['LEFT'], Directions.LEFT)
print(Directions(2).name, Directions.RIGHT.value)


def move(direction: Directions):
    if not isinstance(direction,Directions):
        raise ValueError('Direction not found')
    
    print(f"Moving to {direction.name} ({direction.value})")
    

move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
