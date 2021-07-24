from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

punk = Actor(
    char="o",
    color=(63, 127, 63),
    name="Punk",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
thug = Actor(
    char="T",
    color=(0, 127, 0),
    name="Thug",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)