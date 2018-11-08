def fill(board):
    nBoard=[]
    for v in board:
        nBoard.append(list(v))
    for i in range(1, len(nBoard)-1):
        for j in range(1, len(nBoard[i])-1):
            if nBoard[i][j] != '*':
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if nBoard[i+x][j+y] != '+' and nBoard[i+x][j+y] != '|' and nBoard[i+x][j+y] != '-' and nBoard[i+x][j+y] == '*':
                            if nBoard[i][j] == " ":
                                nBoard[i][j]= "1";
                            else:
                                nBoard[i][j] = str(int(nBoard[i][j]) + 1)

    res = []
    for v in nBoard:
        res.append(''.join(v))
    return res;

def test_board(board, expected):
    result = fill(board)
    if result == expected:
        print("OK")
        return
    print("========== Fail ===========")
    print("Input:")
    print("\n".join(board))
    print()
    print("Expected:")
    print("\n".join(expected))
    print()
    print("Result:")
    print("\n".join(result))
    print()
    # assert False


board = [
    "+-----+",
    "|     |",
    "+-----+",
]
expected = [
    "+-----+",
    "|     |",
    "+-----+",
]
test_board(board, expected)

board = [
    "+-----+",
    "| *   |",
    "+-----+",
]
expected = [
    "+-----+",
    "|1*1  |",
    "+-----+",
]
test_board(board, expected)

board = [
    "+-----+",
    "|     |",
    "|     |",
    "|     |",
    "+-----+",
]
expected = [
    "+-----+",
    "|     |",
    "|     |",
    "|     |",
    "+-----+",
]

test_board(board, expected)

board = [
    "+-----+",
    "|     |",
    "|     |",
    "|    *|",
    "+-----+",
]
expected = [
    "+-----+",
    "|     |",
    "|   11|",
    "|   1*|",
    "+-----+",
]
test_board(board, expected)

board = [
    "+--------+",
    "|        |",
    "|        |",
    "|        |",
    "|   *    |",
    "|        |",
    "|        |",
    "|        |",
    "|        |",
    "+--------+",
]
expected = [
    "+--------+",
    "|        |",
    "|        |",
    "|  111   |",
    "|  1*1   |",
    "|  111   |",
    "|        |",
    "|        |",
    "|        |",
    "+--------+",
]

test_board(board, expected)


board = [
    "+-----+",
    "| * * |",
    "+-----+",
]
expected = [
    "+-----+",
    "|1*2*1|",
    "+-----+",
]

test_board(board, expected)

board = [
    "+------+",
    "| *  * |",
    "|  *   |",
    "|    * |",
    "|   * *|",
    "| *  * |",
    "|      |",
    "+------+",
]
expected = [
    "+------+",
    "|1*22*1|",
    "|12*322|",
    "| 123*2|",
    "|112*4*|",
    "|1*22*2|",
    "|111111|",
    "+------+",
]

test_board(board, expected)

board = [
    "+-----+",
    "| * * |",
    "|     |",
    "|   * |",
    "|  * *|",
    "| * * |",
    "+-----+",
]
expected = [
    "+-----+",
    "|1*2*1|",
    "|11322|",
    "| 12*2|",
    "|12*4*|",
    "|1*3*2|",
    "+-----+",
]

test_board(board, expected)

board = [
    "+-----+",
    "| * * |",
    "+-----+",
]
expected = [
    "+-----+",
    "|1*2*1|",
    "+-----+",
]

test_board(board, expected)

board = [
    "+-+",
    "|*|",
    "| |",
    "|*|",
    "| |",
    "| |",
    "+-+",
]
expected = [
    "+-+",
    "|*|",
    "|2|",
    "|*|",
    "|1|",
    "| |",
    "+-+",
]

test_board(board, expected)

board = [
    "+-+",
    "|*|",
    "+-+",
]
expected = [
    "+-+",
    "|*|",
    "+-+",
]

test_board(board, expected)

board = [
    "+--+",
    "|**|",
    "|**|",
    "+--+",
]
expected = [
    "+--+",
    "|**|",
    "|**|",
    "+--+",
]

test_board(board, expected)

board = [
    "+---+",
    "|***|",
    "|* *|",
    "|***|",
    "+---+",
]
expected = [
    "+---+",
    "|***|",
    "|*8*|",
    "|***|",
    "+---+",
]

test_board(board, expected)

board = [
    "+-----+",
    "|     |",
    "|   * |",
    "|     |",
    "|     |",
    "| *   |",
    "+-----+",
]
expected = [
    "+-----+",
    "|  111|",
    "|  1*1|",
    "|  111|",
    "|111  |",
    "|1*1  |",
    "+-----+",
]

test_board(board, expected)