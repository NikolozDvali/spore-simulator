from game.character.builder import CharacterBuilder
from game.character.character import Character
from game.movement.move import MovementAgent, GreedyMovementAgent


class GameConfig:
    def __init__(
        self,
        predator: Character | None = None,
        prey: Character | None = None,
        predator_movement_agent: MovementAgent | None = None,
        prey_movement_agent: MovementAgent | None = None,
    ):
        self.predator: Character = predator if predator else CharacterBuilder().build()
        self.prey: Character = prey if prey else CharacterBuilder().build()
        self.predator_movement_agent: MovementAgent = (
            predator_movement_agent
            if predator_movement_agent
            else GreedyMovementAgent()
        )
        self.prey_movement_agent: MovementAgent = (
            prey_movement_agent if prey_movement_agent else GreedyMovementAgent()
        )

    def set_predator(self, predator: Character):
        self.predator = predator

    def set_prey(self, prey: Character):
        self.prey = prey
