from typing import Optional, Protocol

class Phase(Protocol):
    def __init__(self, next_phase: Optional['Phase'] = None) -> None:
        self.next_phase = next_phase or NullPhase()

    def start(self) -> None:
        pass

class NullPhase(Phase):
    def start(self) -> None:
        print("Simulation final")

class EvolutionPhase(Phase):
    def start(self) -> None:
        print("Starting Evolution Phase.")

        pass

        self.next_phase.start()

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