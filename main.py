from game.process.game_config import GameConfig
from game.process.phase import Phase, EvolutionPhase, ChasePhase, FightPhase


class SporeGame:
    def __init__(self) -> None:
        self.config: GameConfig = GameConfig()
        self.current_phase: Phase = self.setup_phases()

    def setup_phases(self) -> Phase:
        evolution_phase: Phase = EvolutionPhase(self.config)
        chase_phase: Phase = ChasePhase(self.config)
        fight_phase: Phase = FightPhase(self.config)

        evolution_phase.next_phase = chase_phase
        chase_phase.next_phase = fight_phase
        return evolution_phase

    def start(self) -> None:
        self.current_phase.start()


if __name__ == "__main__":
    game = SporeGame()
    game.start()
