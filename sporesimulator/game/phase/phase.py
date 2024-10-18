import random
from abc import ABC
from typing import Optional

from sporesimulator.game.character.builder import CharacterBuilder
from sporesimulator.game.character.character import Character
from sporesimulator.game.core.constants import MIN_STAMINA, MAX_STAMINA, MIN_HEALTH, MAX_HEALTH, MAX_POSITION, \
    MIN_ATTACK_POWER, MAX_ATTACK_POWER, MAX_LEG_COUNT, MIN_LEG_COUNT, MIN_WING_COUNT, MAX_WING_COUNT, \
    MIN_CLAW_LEVEL, MIN_TEETH_LEVEL, MAX_TEETH_LEVEL, MAX_CLAW_LEVEL
from sporesimulator.game.utils.console import ConsoleFormatter


class WorldState:
    def __init__(self, predator: Character | None = None, prey: Character | None = None):
        self.predator: Character | None = predator
        self.prey: Character | None = prey

    def set_predator(self, predator: Character):
        self.predator = predator

    def set_prey(self, prey: Character):
        self.prey = prey

class Phase(ABC):
    def __init__(self, world_state: WorldState, next_phase: Optional['Phase'] = None) -> None:
        self.world = world_state
        self.next_phase = next_phase or NullPhase(world_state)

    def start(self) -> None:
        pass

class NullPhase(Phase):
    # noinspection PyMissingConstructor
    def __init__(self, world_state: WorldState):
        pass

    def start(self) -> None:
        pass  # Does nothing

class EvolutionPhase(Phase):
    def start(self) -> None:
        ConsoleFormatter.print_section_header("Starting Evolution Phase")

        random_predator = self.generate_random_character("Predator", 0)
        self.world.set_predator(random_predator)
        ConsoleFormatter.print_subheader("Predator Evolved")
        print(random_predator)

        random_prey = self.generate_random_character("Prey")
        self.world.set_prey(random_prey)
        ConsoleFormatter.print_subheader("Prey Evolved")
        print(random_prey)

        self.next_phase.start()

    def generate_random_character(self, name: str, position: int = random.randint(0, MAX_POSITION)) -> Character:
        return (CharacterBuilder()
                .with_name(name)
                .with_stamina(random.randint(MIN_STAMINA, MAX_STAMINA))
                .with_health(random.randint(MIN_HEALTH, MAX_HEALTH))
                .with_attack_power(random.randint(MIN_ATTACK_POWER, MAX_ATTACK_POWER))
                .with_position(position)
                .with_legs(random.randint(MIN_LEG_COUNT, MAX_LEG_COUNT))
                .with_wings(random.randint(MIN_WING_COUNT, MAX_WING_COUNT))
                .with_claws(random.randint(MIN_CLAW_LEVEL, MAX_CLAW_LEVEL))
                .with_teeth(random.randint(MIN_TEETH_LEVEL, MAX_TEETH_LEVEL))
                ).build()

class ChasePhase(Phase):
    def start(self) -> None:
        ConsoleFormatter.print_section_header("Starting Chase Phase.")
        #
        # predator = self.world.predator
        # prey = self.world.prey
        #
        # while True:
        #     if predator.stamina == 0:
        #         print("Prey ran into infinity")
        #         return

        self.next_phase.start()

class FightPhase(Phase):
    def start(self) -> None:
        ConsoleFormatter.print_section_header("Starting Fight Phase.")

        pass

        self.next_phase.start()
