"""
Name: Sagar Patel
UPI: 16159
Description: The game 'Sokoban' is being played.
"""


class Sokoban:

    def __init__(self, board):
        self.__board = board
        self.__steps = []
        self.__copy = list(list(row) for row in self.__board)
        self.__previous = []

    def restart(self):
        self.__steps = []
        new_board = self.__copy
        self.__board = new_board
        self.__copy = list(list(row) for row in self.__board)



    def undo(self):
        before = self.__previous[-1]
        self.__board = before
        self.__previous.pop(-1)
        self.__steps.append(-1)



    def find_player(self):
        boards_list = self.__board
        row = 99999
        index = 0
        while row == 99999:
            if "P" in boards_list[index]:
                row = index
                index +=1
            else:
                index += 1
        total = 0
        col = 99999
        row_list = boards_list[row]
        for item in row_list:
            if item == "P":
                col = total
                total += 1
            total +=1
        a_tuple = (row, col)
        return a_tuple


    def get_steps(self):
        a_list = self.__steps
        total = 0
        for item in a_list:
            total += item
        return total


    def complete(self):
        total = 0
        boards_list = self.__board
        for i in range(len(boards_list)):
            current = boards_list[i]
            if "o" in current:
                total += 1
        if total == 0:
            return True
        else:
            return False

    def __str__(self):
        boards_list = self.__board
        msg = ""
        for i in range(len(boards_list)):
            current = boards_list[i]
            for item in current:
                msg = msg + item
                msg = msg + " "
            msg = msg + "\n"
        return msg

    def move_up(self, direction):
        boards_list = self.__board
        player = self.find_player()
        row = player[0]
        col = player[1]
        length = len(self.__board)
        if row == 0:
            to_check = length - 1
            if boards_list[to_check][col] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[to_check][col] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return
            elif boards_list[to_check][col] == "*" or boards_list[to_check][col] == "o":
                return
            elif boards_list[to_check][col] == "#":
                above = to_check - 1
                if boards_list[above][col] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[above][col] = "#"
                    boards_list[to_check][col] = "P"
                    boards_list[row][col] = " "
                    self.__steps.append(1)
                    return

                elif boards_list[above][col] == "*":
                    return

                elif boards_list[above][col] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[above][col] = " "
                    boards_list[row][col] = " "
                    boards_list[to_check][col] = "P"
                    self.__steps.append(1)
                    return
            return

        top = row - 1
        if boards_list[top][col] == "*" or boards_list[top][col] == "o":
            return

        if boards_list[top][col] == " ":
            board_before = list(list(row) for row in boards_list)
            self.__previous.append(board_before)
            boards_list[top][col] = "P"
            boards_list[row][col] = " "
            self.__steps.append(1)
            return

        if boards_list[top][col] == "#":
            if top == 0:
                to_check = length - 1
                if boards_list[to_check][col] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[to_check][col] = "#"
                    boards_list[row][col] = " "
                    boards_list[top][col] = "P"
                    self.__steps.append(1)
                    return

                elif boards_list[to_check][col] == "*":
                    return

                elif boards_list[to_check][col] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[to_check][col] = " "
                    boards_list[row][col] = " "
                    boards_list[top][col] = "P"
                    self.__steps.append(1)
                    return

            before_top = top - 1
            if boards_list[before_top][col] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[before_top][col] = "#"
                boards_list[top][col] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

            if boards_list[before_top][col] == "o":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[before_top][col] = " "
                boards_list[top][col] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

            if boards_list[before_top][col] == "*":
                return

    def move_down(self):
        boards_list = self.__board
        player = self.find_player()
        row = player[0]
        col = player[1]
        length = len(self.__board)
        if row == (length - 1):
            to_check = 0
            if boards_list[to_check][col] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[to_check][col] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return
            elif boards_list[to_check][col] == "*" or boards_list[to_check][col] == "o":
                return
            elif boards_list[to_check][col] == "#":
                above = to_check + 1
                if boards_list[above][col] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[above][col] = "#"
                    boards_list[to_check][col] = "P"
                    boards_list[row][col] = " "
                    self.__steps.append(1)
                    return

                elif boards_list[above][col] == "*":
                    return

                elif boards_list[above][col] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[above][col] = " "
                    boards_list[row][col] = " "
                    boards_list[to_check][col] = "P"
                    self.__steps.append(1)
                    return
            return
        bottom = row + 1
        if boards_list[bottom][col] == "*" or boards_list[bottom][col] == "o":
            return

        if boards_list[bottom][col] == ' ':
            board_before = list(list(row) for row in boards_list)
            self.__previous.append(board_before)
            boards_list[bottom][col] = "P"
            boards_list[row][col] = " "
            self.__steps.append(1)
            return

        if boards_list[bottom][col] == "#":
            if bottom == (length - 1):
                to_check = 0
                if boards_list[to_check][col] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[to_check][col] = "#"
                    boards_list[row][col] = " "
                    boards_list[bottom][col] = "P"
                    self.__steps.append(1)
                    return

                elif boards_list[to_check][col] == "*":
                    return

                elif boards_list[to_check][col] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[to_check][col] = " "
                    boards_list[row][col] = " "
                    boards_list[bottom][col] = "P"
                    self.__steps.append(1)
                    return

            under_bottom = bottom + 1
            if boards_list[under_bottom][col] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[under_bottom][col] = "#"
                boards_list[row][col] = " "
                boards_list[bottom][col] = "P"
                self.__steps.append(1)
                return

            if boards_list[under_bottom][col] == "*":
                return

            if boards_list[under_bottom][col] == "o":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[under_bottom][col] = " "
                boards_list[bottom][col] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

    def move_left(self):
        boards_list = self.__board
        player = self.find_player()
        row = player[0]
        col = player[1]
        length = len(self.__board)
        col_length = 0
        col_length_test = boards_list[row]
        for item in col_length_test:
            col_length += 1

        if col == 0:
            to_check = col_length - 1
            if boards_list[row][to_check] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][to_check] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return
            elif boards_list[row][to_check] == "*" or boards_list[row][to_check] == "o":
                return
            elif boards_list[row][to_check] == "#":
                above = to_check - 1
                if boards_list[row][above] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][above] = "#"
                    boards_list[row][to_check] = "P"
                    boards_list[row][col] = " "
                    self.__steps.append(1)
                    return

                elif boards_list[row][above] == "*":
                    return

                elif boards_list[row][above] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][col] = " "
                    boards_list[row][above] = " "
                    boards_list[row][to_check] = "P"
                    self.__steps.append(1)
                    return
            return
        left = col - 1
        if boards_list[row][left] == "*" or boards_list[row][left] == "o":
            return
        if boards_list[row][left] == " ":
            board_before = list(list(row) for row in boards_list)
            self.__previous.append(board_before)
            boards_list[row][left] = "P"
            boards_list[row][col] = " "
            self.__steps.append(1)
            return

        if boards_list[row][left] == "#":
            if left == 0:
                to_check = col_length - 1
                if boards_list[row][to_check] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][to_check] = "#"
                    boards_list[row][col] = " "
                    boards_list[row][left] = "P"
                    self.__steps.append(1)
                    return

                elif boards_list[row][to_check] == "*":
                    return

                elif boards_list[row][to_check] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][to_check] = " "
                    boards_list[row][col] = " "
                    boards_list[row][left] = "P"
                    self.__steps.append(1)
                    return

            to_left = left - 1
            if boards_list[row][to_left] == "*":
                return
            if boards_list[row][to_left] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][left] = "P"
                boards_list[row][to_left] = "#"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

            if boards_list[row][to_left] == "o":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][left] = "P"
                boards_list[row][to_left] = " "
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

    def move_right(self):
        boards_list = self.__board
        player = self.find_player()
        row = player[0]
        col = player[1]
        length = len(self.__board)
        col_length = 0
        col_length_test = boards_list[row]
        for item in col_length_test:
            col_length += 1

        if col == (col_length - 1):
            to_check = 0
            if boards_list[row][to_check] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][to_check] = "P"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return
            elif boards_list[row][to_check] == "*" or boards_list[row][to_check] == "o":
                return
            elif boards_list[row][to_check] == "#":
                above = to_check + 1
                if boards_list[row][above] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][above] = "#"
                    boards_list[row][to_check] = "P"
                    boards_list[row][col] = " "
                    self.__steps.append(1)
                    return

                elif boards_list[row][above] == "*":
                    return

                elif boards_list[row][above] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][col] = " "
                    boards_list[row][above] = " "
                    boards_list[row][to_check] = "P"
                    self.__steps.append(1)
                return
        right = col + 1
        if boards_list[row][right] == "*" or boards_list[row][right] == "o":
            return
        if boards_list[row][right] == " ":
            board_before = list(list(row) for row in boards_list)
            self.__previous.append(board_before)
            boards_list[row][right] = "P"
            boards_list[row][col] = " "
            self.__steps.append(1)
            return

        if boards_list[row][right] == "#":

            if right == (col_length - 1):
                to_check = 0
                if boards_list[row][to_check] == " ":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][to_check] = "#"
                    boards_list[row][col] = " "
                    boards_list[row][right] = "P"
                    self.__steps.append(1)
                    return

                elif boards_list[row][to_check] == "*":
                    return

                elif boards_list[row][to_check] == "o":
                    board_before = list(list(row) for row in boards_list)
                    self.__previous.append(board_before)
                    boards_list[row][to_check] = " "
                    boards_list[row][col] = " "
                    boards_list[row][right] = "P"
                    self.__steps.append(1)
                    return

            to_right = right + 1
            if boards_list[row][to_right] == "*":
                return
            if boards_list[row][to_right] == " ":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][right] = "P"
                boards_list[row][to_right] = "#"
                boards_list[row][col] = " "
                self.__steps.append(1)
                return

            if boards_list[row][to_right] == "o":
                board_before = list(list(row) for row in boards_list)
                self.__previous.append(board_before)
                boards_list[row][right] = "P"
                boards_list[row][to_right] = " "
                boards_list[row][col] = " "
                self.__steps.append(1)
                return


    def move(self, direction):

        if direction == "w":
            self.move_up("w")

        if direction == "a":
            self.move_left()

        if direction == "s":
           self.move_down()


        if direction == "d":
            self.move_right()

def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')

main(test_board)
