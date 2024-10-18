from sporesimulator.game.character.managers import PositionManager, AppendageManager, CharacterStatsManager
from sporesimulator.game.move import MOVE_PROTOCOLS
from sporesimulator.game.move.move import Move, Direction


class Character:
    def __init__(self,
                 name: str = "Creature",
                 position_manager: PositionManager = PositionManager(),
                 stats_manager: CharacterStatsManager = CharacterStatsManager(),
                 appendage_manager: AppendageManager = AppendageManager()) -> None:
        self.name = name
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
        return self.stats_manager.calculate_attack_power(self.appendage_manager)

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

    def can_move(self, movement_protocol: type[Move], direction: Direction):
        if not self.appendage_manager.supports_movement(movement_protocol):
            return False
        if not self.stats_manager.can_use_stamina(movement_protocol.requires_stamina):
            return False
        if not self.position_manager.can_move_to(self.position + movement_protocol.speed * direction.value):
            return False
        return True

    def move(self, movement_protocol: type[Move], direction: Direction):
        if not self.can_move(movement_protocol, direction):
            raise ValueError("Can not move the character")
        self.position_manager.move(self.position + movement_protocol.speed * direction.value)
        self.stats_manager.use_stamina(movement_protocol.uses_stamina, movement_protocol.requires_stamina)

    def get_available_move_protocols(self) -> list[type[Move]]:
        return [move_protocol for move_protocol in MOVE_PROTOCOLS if self.can_move(move_protocol, Direction.NOWHERE)]

    """Helper methods"""

    def __str__(self):
        return f"Creature name: {self.name}\n\
                Position: {str(self.position_manager)}\n\
                Stats: {self.stats_manager.str_with_appendages(self.appendage_manager)}\n\
                Appendages: {str(self.appendage_manager)}"

