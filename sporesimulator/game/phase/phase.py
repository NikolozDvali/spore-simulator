import random
from abc import ABC
from typing import Optional

from sporesimulator.game.character.builder import CharacterBuilder
from sporesimulator.game.character.character import Character
from sporesimulator.game.core.constants import MIN_STAMINA, MAX_STAMINA, MIN_HEALTH, MAX_HEALTH, MAX_POSITION, \
    MIN_POSITION, MIN_ATTACK_POWER, MAX_ATTACK_POWER, MAX_LEG_COUNT, MIN_LEG_COUNT, MIN_WING_COUNT, MAX_WING_COUNT, \
    MIN_CLAW_LEVEL, MIN_TEETH_LEVEL, MAX_TEETH_LEVEL, MAX_CLAW_LEVEL


class WorldState:
    def __init__(self, predator: Character | None, prey: Character | None):
        self.predator: Character | None = predator
        self.prey: Character | None = prey

    def set_predator(self, predator: Character):
        self.predator = predator

    def set_prey(self, prey: Character):
        self.prey = prey


class Phase(ABC):
    def __init__(self, game: Optional[WorldState] = None, next_phase: Optional['Phase'] = None) -> None:
        self.game: WorldState = game
        self.next_phase = next_phase or NullPhase()

    def start(self) -> None:
        pass

class NullPhase(Phase):
    def start(self) -> None:
        print("Simulation final")

class EvolutionPhase(Phase):
    def start(self) -> None:
        print("Starting Evolution Phase.")

        self.game.set_predator(self.generate_random_character())
        self.game.set_prey(self.generate_random_character())

        self.next_phase.start()

    def generate_random_character(self,):
        return (CharacterBuilder()
                .with_stamina(random.randint(MIN_STAMINA, MAX_STAMINA))
                .with_health(random.randint(MIN_HEALTH, MAX_HEALTH))
                .with_attack_power(random.randint(MIN_ATTACK_POWER, MAX_ATTACK_POWER))
                .with_position(random.randint(MIN_POSITION, MAX_POSITION))
                .with_legs(random.randint(MIN_LEG_COUNT, MAX_LEG_COUNT))
                .with_wings(random.randint(MIN_WING_COUNT, MAX_WING_COUNT))
                .with_claws(random.randint(MIN_CLAW_LEVEL, MAX_CLAW_LEVEL))
                .with_teeth(random.randint(MIN_TEETH_LEVEL, MAX_TEETH_LEVEL))
                ).build()

class ChasePhase(Phase):
    def start(self) -> None:
        print("Starting Chase Phase.")

        pass

        self.next_phase.start()

class FightPhase(Phase):
    def start(self) -> None:
        print("Starting Fight Phase.")

        pass

        self.next_phase.start()