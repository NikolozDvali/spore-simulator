from sporesimulator.game.phase.phase import EvolutionPhase, WorldState, Phase


class SporeGame:
    def __init__(self):
        self.state: WorldState = WorldState()
        self.current_phase: Phase = EvolutionPhase(self.state)

    def start(self):
        self.current_phase.start()


if __name__ == "__main__":
    game = SporeGame()
    game.start()
