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

    def __getattr__(self, attr_name: str):
        stats_attributes = {
            'stamina': self.stats_manager.stamina,
            'health': self.stats_manager.health,
            'attack_power': self.stats_manager.calculate_attack_power(self.appendage_manager),
            'position': self.position_manager.position,
        }
        if attr_name in stats_attributes:
            return stats_attributes[attr_name]
        else:
            raise AttributeError(f"{attr_name} is not a valid attribute")

    def __setattr__(self, attr_name: str, value):
        if attr_name in ['stamina', 'health']:
            self.stats_manager.__setattr__(attr_name, value)
        elif attr_name == 'position':
            self.position_manager.position = value
        else:
            object.__setattr__(self, attr_name, value)

    def __str__(self):
        return (
            f"Creature name: {self.name}\n"
            f"Position: {str(self.position_manager)}\n"
            f"Stats: {self.stats_manager.str_with_appendages(self.appendage_manager)}\n"
            f"Appendages: {str(self.appendage_manager)}"
        )