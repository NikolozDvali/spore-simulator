from typing import Self

from sporesimulator.game.character.character import Character
from sporesimulator.game.character.managers import (
    AppendageManager,
    CharacterStatsManager,
    PositionManager,
)


class CharacterBuilder:
    def __init__(self):
        self.position_manager = PositionManager()
        self.stats_manager = CharacterStatsManager()
        self.appendage_manager = AppendageManager()
        self.name = None

    def with_name(self, name: str) -> Self:
        self.name = name
        return self

    def with_position(self, position: int) -> Self:
        self.position_manager.position = position
        return self

    def with_health(self, base_health: int) -> Self:
        self.stats_manager.health = base_health
        return self

    def with_attack_power(self, base_attack_power: int) -> Self:
        self.stats_manager.base_attack_power = base_attack_power
        return self

    def with_stamina(self, base_stamina: int) -> Self:
        self.stats_manager.stamina = base_stamina
        return self

    def with_legs(self, count: int) -> Self:
        self.appendage_manager.leg_count = count
        return self

    def with_wings(self, count: int) -> Self:
        self.appendage_manager.wing_count = count
        return self

    def with_claws(self, level: int) -> Self:
        self.appendage_manager.claw_level = level
        return self

    def with_teeth(self, level: int) -> Self:
        self.appendage_manager.teeth_level = level
        return self

    def build(self) -> Character:
        return Character(
            name=self.name,
            position_manager=self.position_manager,
            stats_manager=self.stats_manager,
            appendage_manager=self.appendage_manager,
        )
