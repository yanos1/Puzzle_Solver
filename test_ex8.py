##############################################################################
#                                 Tests                                      #
##############################################################################

from puzzle_solver import *


def test_max_seen_cells():
    picture_1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    assert max_seen_cells(picture_1, 0, 0) == 1
    assert max_seen_cells(picture_1, 1, 0) == 0
    assert max_seen_cells(picture_1, 1, 2) == 5
    assert max_seen_cells(picture_1, 1, 1) == 3
    assert max_seen_cells(picture_1, 2, 0) == 1
    assert max_seen_cells(picture_1, 2, 1) == 0
    assert max_seen_cells(picture_1, 2, 2) == 3
    assert max_seen_cells(picture_1, 0, 2) == 4
    assert max_seen_cells(picture_1, 1, 3) == 4
    picture_2 = [[-1, -1, -1], [-1, -1, -1]]
    for i in range(2):
        for j in range(3):
            assert max_seen_cells(picture_2, i, j) == 4
    picture_3 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert max_seen_cells(picture_3, 1, 1) == 0
    assert max_seen_cells(picture_3, 1, 0) == 1
    assert max_seen_cells(picture_3, 2, 1) == 1
    assert max_seen_cells(picture_3, 2, 2) == 0
    assert max_seen_cells(picture_3, 0, 2) == 0
    assert max_seen_cells(picture_3, 1, 2) == 1
    assert max_seen_cells([[0]], 0, 0) == 0
    assert max_seen_cells([[0, 1]], 0, 1) == 1
    assert max_seen_cells([[0], [1]], 1, 0) == 1
    assert max_seen_cells([[1], [0]], 0, 0) == 1


def test_min_seen_cells():
    picture_1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    assert min_seen_cells(picture_1, 0, 0) == 0
    assert min_seen_cells(picture_1, 1, 0) == 0
    assert min_seen_cells(picture_1, 1, 2) == 0
    assert min_seen_cells(picture_1, 1, 1) == 1
    assert min_seen_cells(picture_1, 2, 2) == 1
    assert min_seen_cells(picture_1, 1, 3) == 1
    assert min_seen_cells(picture_1, 0, 2) == 1
    assert min_seen_cells(picture_1, 0, 3) == 0
    picture_2 = [[-1, -1, -1], [-1, -1, -1]]
    for i in range(2):
        for j in range(3):
            assert min_seen_cells(picture_2, i, j) == 0
    picture_3 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert min_seen_cells(picture_3, 1, 1) == 0
    assert min_seen_cells(picture_3, 1, 0) == 1
    assert min_seen_cells(picture_3, 2, 1) == 1
    assert min_seen_cells(picture_3, 2, 2) == 0
    assert min_seen_cells(picture_3, 0, 2) == 0
    assert min_seen_cells(picture_3, 1, 2) == 1
    assert min_seen_cells([[0]], 0, 0) == 0
    assert min_seen_cells([[0]], 0, 0) == 0
    assert min_seen_cells([[0, 1]], 0, 1) == 1
    assert min_seen_cells([[0], [1]], 1, 0) == 1
    assert min_seen_cells([[1], [0]], 0, 0) == 1


def test_check_constraints():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2
    assert check_constraints(picture1, {(0, 0, 0)}) == 2
    assert check_constraints(picture2, {(0, 0, 0)}) == 1
    assert check_constraints(picture2, {(1, 1, 0)}) == 0
    print("dsafas")


def test_solve_puzzle():
    sol_1 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3,
                        4) == sol_1
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3,
                        4) is None
    sol_2a = [[0, 0, 1], [1, 1, 1], [1, 1, 1]]
    sol_2b = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == sol_2a \
           or solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == sol_2b
    print("I am proud of you")


def test_how_many_solutions():
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)},
                              3, 4) == 0
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3,
                        4) == 1
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1)}, 3,
                              4) == 2
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3) for j in range(
        3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64
    assert how_many_solutions({(2, 0, 1)}, 3, 4) == 2 ** 9
    assert how_many_solutions({(2, 0, 1)}, 4, 3) == 2 ** 8
    assert how_many_solutions({(2, 0, 1), (1, 2, 1)}, 4, 3) == 2 ** 4
    assert how_many_solutions({(0, 0, 1), (4, 0, 1), (0, 4, 1), (4, 4, 1)},
                              5, 5) == 2 ** 13
    assert how_many_solutions({(0, 0, 1), (4, 0, 1), (0, 4, 1), (4, 4, 1),
                               (2, 2, 1)}, 5, 5) == 2 ** 8


def test_generate_puzzle():
    picture = [[1, 0, 0], [1, 1, 1]]
    # assert generate_puzzle(picture) in [{(0, 0, 2), (1, 2, 3)},
    #                                     {(1, 0, 4), (0, 1, 0), (0, 2, 0)},
    #                                     {(1, 0, 4), (0, 0, 2), (0, 2, 0)},
    #                                     {(1, 0, 4), (1, 1, 3), (0, 2, 0)},
    #                                     {(1, 0, 4), (1, 1, 3), (1, 2, 3)},
    #                                     {(1, 0, 4), (0, 1, 0), (1, 2, 3)},
    #                                     {(0, 0, 2), (1, 1, 3), (0, 1, 0),
    #                                      (0, 2, 0)}]
    picture_2 = [[1, 1], [0, 1]]
    assert generate_puzzle(picture_2) in [{(0, 1, 3), (1, 1, 2)},
                                          {(1, 0, 0), (0, 1, 3)},
                                          {(1, 0, 0), (0, 0, 2), (1, 1, 2)}]
    # Last test may miss options.
    assert generate_puzzle([[0]]) == {(0, 0, 0)}
    assert generate_puzzle([[1]]) == {(0, 0, 1)}


def test_generate_solve_puzzle():
    assert how_many_solutions(generate_puzzle([[1, 0], [1, 1], [0, 0]]), 3, 2)\
           == 1
    assert how_many_solutions(generate_puzzle([[1, 1], [1, 1], [1, 1]]), 3, 2)\
        == 1
    assert how_many_solutions(generate_puzzle([[0, 0], [0, 0], [0, 0]]), 3, 2)\
           == 1
    assert solve_puzzle(generate_puzzle([[1, 0], [1, 1], [0, 0]]), 3, 2)\
           == [[1, 0], [1, 1], [0, 0]]
    #assert solve_puzzle(generate_puzzle([[1, 1], [1, 1], [1, 1]]), 3, 2) \
            #== [[1, 1], [1, 1], [1, 1]]
    assert solve_puzzle(generate_puzzle([[0, 0], [0, 0], [0, 0]]), 3, 2) \
           == [[0, 0], [0, 0], [0, 0]]
test_generate_solve_puzzle()
test_generate_puzzle()
test_how_many_solutions()
test_solve_puzzle()
test_check_constraints()
test_min_seen_cells()
test_max_seen_cells()