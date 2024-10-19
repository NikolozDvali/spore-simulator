import random
from abc import ABC
from typing import Optional

from sporesimulator.game.character.builder import CharacterBuilder
from sporesimulator.game.character.character import Character
from sporesimulator.game.core.constants import MIN_STAMINA, MAX_STAMINA, MIN_HEALTH, MAX_HEALTH, MAX_POSITION, \
    MIN_ATTACK_POWER, MAX_ATTACK_POWER, MAX_LEG_COUNT, MIN_LEG_COUNT, MIN_WING_COUNT, MAX_WING_COUNT, \
    MIN_CLAW_LEVEL, MIN_TEETH_LEVEL, MAX_TEETH_LEVEL, MAX_CLAW_LEVEL, \
    DIFFERENCE_BETWEEN_PREDATOR_AND_PREY_STAMINA_MODIFIER
from sporesimulator.game.movement.move import Direction
from sporesimulator.game.process.game_config import GameConfig


class Phase(ABC):
    def __init__(self, game_config: GameConfig, next_phase: Optional['Phase'] = None) -> None:
        self.game_config = game_config
        self.next_phase = next_phase or NullPhase(game_config)

    def start(self) -> None:
        pass

class NullPhase(Phase):
    # noinspection PyMissingConstructor
    def __init__(self, game_config: GameConfig):
        pass

    def start(self) -> None:
        print("\n--- All phases ended ---")

class EvolutionPhase(Phase):
    def start(self) -> None:
        print("--- Starting Evolution Phase ---")

        random_predator = self.generate_random_character("Predator", is_predator=True)
        self.game_config.set_predator(random_predator)
        print(f"Predator Evolved:\n{random_predator}")

        random_prey = self.generate_random_character("Prey", is_predator=False)
        self.game_config.set_prey(random_prey)
        print(f"Prey Evolved:\n{random_prey}\n")

        self.next_phase.start()

    def generate_random_character(self, name: str, is_predator: bool = False) -> Character:
        if is_predator:
            stamina_min = MIN_STAMINA + DIFFERENCE_BETWEEN_PREDATOR_AND_PREY_STAMINA_MODIFIER
            stamina_max = MAX_STAMINA + DIFFERENCE_BETWEEN_PREDATOR_AND_PREY_STAMINA_MODIFIER
            position = 0
        else:
            stamina_min = MIN_STAMINA
            stamina_max = MAX_STAMINA
            position = random.randint(0, MAX_POSITION)

        return (CharacterBuilder()
                .with_name(name)
                .with_stamina(random.randint(stamina_min, stamina_max))
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
        print("--- Starting Chase Phase ---")

        while not self.predator_caught_prey():
            if self.game_config.predator.stamina == 0:
                print("Prey ran into infinity")
                return

            self.move_predator()
            self.move_prey()

        print("Predator caught prey!\n")
        self.next_phase.start()

    def predator_caught_prey(self) -> bool:
        return self.game_config.predator.position == self.game_config.prey.position

    def move_predator(self) -> None:
        next_move = self.game_config.predator_movement_agent.next_move(self.game_config.predator.get_available_move_protocols())
        if next_move:
            self.game_config.predator.move(next_move, Direction.RIGHT)

    def move_prey(self) -> None:
        next_move = self.game_config.prey_movement_agent.next_move(self.game_config.prey.get_available_move_protocols())
        if next_move:
            self.game_config.prey.move(next_move, Direction.RIGHT)

class FightPhase(Phase):
    def start(self) -> None:
        print("--- Starting Fight Phase ---")

        predator = self.game_config.predator
        prey = self.game_config.prey

        while True:
            predator.attack(prey)
            if prey.health == 0:
                print("Some R-rated things have happened")
                break
            prey.attack(predator)
            if predator.health == 0:
                print("Prey ran into infinity")
                break

        self.next_phase.start()
