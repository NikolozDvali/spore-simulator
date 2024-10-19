from sporesimulator.game.character.character import Character
from sporesimulator.game.movement.move import MovementAgent, GreedyMovementAgent


class GameConfig:
    def __init__(self, predator: Character | None = None,
                 prey: Character | None = None,
                 predator_movement_agent: MovementAgent | None = GreedyMovementAgent(),
                 prey_movement_agent: MovementAgent | None = GreedyMovementAgent()):
        self.predator: Character | None = predator
        self.prey: Character | None = prey
        self.predator_movement_agent: MovementAgent = predator_movement_agent
        self.prey_movement_agent: MovementAgent = prey_movement_agent

    def set_predator(self, predator: Character):
        self.predator = predator

    def set_prey(self, prey: Character):
        self.prey = prey