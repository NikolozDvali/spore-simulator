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

    @property
    def stamina(self):
        return self.stats_manager.stamina

    @stamina.setter
    def stamina(self, stamina: int) -> None:
        self.stats_manager.stamina = stamina

    @property
    def position(self) -> int:
        return self.position_manager.position

    @position.setter
    def position(self, new_position: int) -> None:
        self.position_manager.position = new_position

    @property
    def attack_power(self) -> int:
        return self.appendage_manager.calculate_attack_power(self.stats_manager.attacking_power)

    @property
    def health(self) -> int:
        return self.stats_manager.health

    @health.setter
    def health(self, health: int) -> None:
        self.stats_manager.health = health
        if self.stats_manager.health <= 0:
            self.stats_manager.health = 0

    """Common methods"""

    def attack(self, victim: 'Character'):
        victim.health -= self.attack_power

    def move(self, movement_protocol: type[Move], direction: Direction):
        new_position = self.position + movement_protocol.speed * direction.value

        if not self.appendage_manager.supports_movement(movement_protocol):
            raise ValueError("Character appendages don't support that movement")
        if not self.stats_manager.can_use_stamina(movement_protocol.requires_stamina):
            raise ValueError("Character doesn't have enough stamina")
        if not self.position_manager.can_move_to(new_position):
            raise ValueError("Character cant move there")

        self.position_manager.move(new_position)
        self.stats_manager.use_stamina(movement_protocol.uses_stamina, movement_protocol.requires_stamina)

