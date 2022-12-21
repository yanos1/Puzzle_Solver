from typing import List, Tuple, Set, Optional

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    count = 0
    if picture[row][col] == 0:
        return count
    for i in range(col, len(picture[0])):
        if picture[row][i] != 0:
            count += 1
        else:
            break
    for i in range(col - 1, -1, -1):
        if picture[row][i] != 0:
            count += 1
        else:
            break
    for i in range(row + 1, len(picture)):
        if picture[i][col] != 0:
            count += 1
        else:
            break
    for i in range(row - 1, -1, -1):
        if picture[i][col] != 0:
            count += 1
        else:
            break
    return count


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    count = 0
    if picture[row][col] == 0 or picture[row][col] == -1:
        return count
    for i in range(col, len(picture[0])):
        if picture[row][i] == 1:
            count += 1
        else:
            break
    for i in range(col - 1, -1, -1):
        if picture[row][i] == 1:
            count += 1
        else:
            break
    for i in range(row + 1, len(picture)):
        if picture[i][col] == 1:
            count += 1
        else:
            break
    for i in range(row - 1, -1, -1):
        if picture[i][col] == 1:
            count += 1
        else:
            break
    return count


def check_constraints(picture: Picture,
                      constraints_set: Set[Constraint]) -> int:
    lst = []
    for constraint in constraints_set:
        mini = min_seen_cells(picture, constraint[0], constraint[1])
        maxi = max_seen_cells(picture, constraint[0], constraint[1])
        if mini == maxi == constraint[2]:
            lst.append(1)
        elif mini <= constraint[2] <= maxi:
            lst.append(2)
        else:
            return 0
    if 2 in lst:
        return 2
    else:
        return 1


def get_new_index(index, row, col):
    if index[1] + 1 == col and row != index[0] + 1:
        new_index = (index[0] + 1, 0)
    elif index[1] + 1 == col:
        new_index = (index[0] - 1, 0)
    else:
        new_index = (index[0], index[1] + 1)
    return new_index


def legal_move(index, board, constraints_set):
    modified_set = {item for item in constraints_set if
                    index[0] == item[0] or index[1] == item[1]}
    if len(modified_set) > 0:
        valid = check_constraints(board, modified_set)
        if valid != 0:
            return True
        else:
            return False
    else:
        return True


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[
    Picture]:
    initial_board = [[-1 for i in range(m)] for j in range(n)]
    dic_of_constraints_set = {(tup[0], tup[1]): tup[2] for tup in
                              constraints_set for i in tup}
    return solve_puzzle_helper(constraints_set, dic_of_constraints_set, n, m,
                               (0, 0), initial_board)


def solve_puzzle_helper(constraints_set, constraints_dic, row, col, index,
                        board):
    if -1 not in sum(board, []):
        sol = check_constraints(board, constraints_set)
        if sol != 0:
            return board

    if not legal_move(index, board, constraints_set):
        return

    for color in [0, 1]:
        if index in constraints_dic:
            if constraints_dic[index] != 0:
                board[index[0]][index[1]] = 1
            else:
                board[index[0]][index[1]] = 0
        else:
            board[index[0]][index[1]] = color
        new_index = get_new_index(index, row, col)
        if solve_puzzle_helper(constraints_set, constraints_dic, row, col,
                               new_index, board):
            return board
    board[index[0]][index[1]] = -1


def how_many_solutions(constraints_set: Set[Constraint], n: int,
                       m: int) -> int:
    initial_board = [[-1 for i in range(m)] for j in range(n)]
    return how_many_solutions_helper(initial_board, constraints_set, n, m,
                                     (0, 0), 0)


def how_many_solutions_helper(board, constrains_set, row, col, index, count):
    for i in (0, 1):
        board[index[0]][index[1]] = i
        if check_constraints(board, constrains_set) != 0:
            if index == (row - 1, col - 1) and check_constraints(board,
                                                                 constrains_set) == 1:
                count = count + 1
                continue
            new_index = get_new_index(index, row, col)
            count = how_many_solutions_helper(board, constrains_set, row, col,
                                              new_index, count)
    board[index[0]][index[1]] = -1
    return count


def generate_puzzle(picture: Picture):  # -> Set[Constraint]:
    se = set()
    dic_of_set = {(tup[0], tup[1]): tup[2] for tup in
                              se for i in tup}
    return generate_puzzle_help(picture, se, (0, 0),dic_of_set)


def generate_puzzle_help(picture, se, index,dic):
    if not legal_move(index,picture,se):
        return
    if how_many_solutions(se,len(picture),len(picture[0])) == 1:
        return se
    for i in range(0,len(picture) + len(picture[0])):
        dic_of_set = {(tup[0], tup[1]): tup[2] for tup in
                      se for i in tup}
        if index in dic_of_set:
            continue
        else:
            se.add((index[0],index[1],i))
        new = get_new_index(index,len(picture),len(picture[0]))
        if generate_puzzle_help(picture,se,new,dic):
            return se
        else:
            se.remove((index[0], index[1], i))


