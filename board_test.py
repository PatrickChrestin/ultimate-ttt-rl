import board

def test_board_initial_state():
    b = board.TTTBoard()
    assert all([x == board.GridStates.EMPTY for row in b.board for x in row])

def test_should_be_active_initially():
    b = board.TTTBoard()
    assert b.getBoardDecision() == board.TTTBoardDecision.ACTIVE

def test_x_should_win_in_a_row():
    b = board.TTTBoard()
    b.makeMove(board.GridStates.PLAYER_X, 0, 0)
    b.makeMove(board.GridStates.PLAYER_X, 0, 1)
    b.makeMove(board.GridStates.PLAYER_X, 0, 2)
    assert b.getBoardDecision() == board.TTTBoardDecision.WON_X

def test_o_should_win_in_a_column():
    b = board.TTTBoard()
    b.makeMove(board.GridStates.PLAYER_O, 0, 0)
    b.makeMove(board.GridStates.PLAYER_O, 1, 0)
    b.makeMove(board.GridStates.PLAYER_O, 2, 0)
    assert b.getBoardDecision() == board.TTTBoardDecision.WON_O

def test_x_should_win_in_a_diagonal():
    b = board.TTTBoard()
    b.makeMove(board.GridStates.PLAYER_X, 0, 0)
    b.makeMove(board.GridStates.PLAYER_X, 1, 1)
    b.makeMove(board.GridStates.PLAYER_X, 2, 2)
    assert b.getBoardDecision() == board.TTTBoardDecision.WON_X

def test_o_should_win_in_the_counter_diagonal():
    b = board.TTTBoard()
    b.makeMove(board.GridStates.PLAYER_O, 0, 2)
    b.makeMove(board.GridStates.PLAYER_O, 1, 1)
    b.makeMove(board.GridStates.PLAYER_O, 2, 0)
    assert b.getBoardDecision() == board.TTTBoardDecision.WON_O

def test_draw():
    b = board.TTTBoard()
    b.makeMove(board.GridStates.PLAYER_X, 0, 0)
    b.makeMove(board.GridStates.PLAYER_O, 0, 1)
    b.makeMove(board.GridStates.PLAYER_X, 0, 2)
    b.makeMove(board.GridStates.PLAYER_X, 1, 0)
    b.makeMove(board.GridStates.PLAYER_O, 1, 1)
    b.makeMove(board.GridStates.PLAYER_X, 1, 2)
    b.makeMove(board.GridStates.PLAYER_O, 2, 0)
    b.makeMove(board.GridStates.PLAYER_X, 2, 1)
    b.makeMove(board.GridStates.PLAYER_O, 2, 2)
    assert b.getBoardDecision() == board.TTTBoardDecision.DRAW

if __name__ == '__main__':
    test_board_initial_state()
    test_should_be_active_initially()
    test_x_should_win_in_a_row()
    test_o_should_win_in_a_column()
    test_x_should_win_in_a_diagonal()
    test_o_should_win_in_the_counter_diagonal()
    test_draw()
    print('✔ Board Test: All tests passed!')

