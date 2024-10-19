from game.movement.move import (
    GreedyMovementAgent,
    Crawl,
    Hop,
    Walk,
    Run,
    Fly,
)


def test_greedy_movement_agent_no_possible_moves():
    agent = GreedyMovementAgent()
    assert agent.next_move([]) is None


def test_greedy_movement_agent_some_possible_moves():
    agent = GreedyMovementAgent()
    assert agent.next_move([Crawl, Hop]) == Hop


def test_greedy_movement_agent_all_possible_moves():
    agent = GreedyMovementAgent()
    assert agent.next_move([Crawl, Hop, Walk, Run, Fly]) == Fly
