from sporesimulator.game.character.managers import PositionManager, AppendageManager, CharacterStatsManager
from sporesimulator.game.move.move import Move, Direction


class Character:
    def __init__(self,
                 position_manager: PositionManager = PositionManager(),
                 stats_manager: CharacterStatsManager = CharacterStatsManager(),
                 appendage_manager: AppendageManager = AppendageManager()) -> None:
        self.position_manager = position_manager
        self.stats_manager = stats_manager
        self.appendage_manager = appendage_manager

    """Common attribute getters"""

    @property
    def stamina(self):
        return self.stats_manager.stamina

    @property
    def position(self) -> int:
        return self.position_manager.position

    @property
    def attack_power(self) -> int:
        return self.appendage_manager.calculate_attack_power(self.stats_manager.attacking_power)

    @property
    def health(self) -> int:
        return self.stats_manager.health

    """Common attribute setters"""

    @position.setter
    def position(self, new_position: int) -> None:
        self.position_manager.position = new_position

    @health.setter
    def health(self, health: int) -> None:
        self.stats_manager.health = health
        if self.stats_manager.health <= 0:
            self.stats_manager.health = 0

    @stamina.setter
    def stamina(self, stamina: int) -> None:
        self.stats_manager.stamina = stamina

    """Common methods"""

    def attack(self, victim: 'Character'):
        victim.health -= self.attack_power

    def move(self, movement_protocol: type[Move], direction: Direction):
        if self.stamina < movement_protocol.requires_stamina:
            raise ValueError("Not enough stamina!")
        new_position = self.position + (movement_protocol.speed * direction.value)
        if new_position < 0:
            raise ValueError("Can't move to negative position!")
        self.position = new_position
        self.stamina -= movement_protocol.uses_stamina
