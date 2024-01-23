#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

void printBoard(vector<vector<int>> board) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == 0) {
                cout << "  ";
            }
            if (board[i][j] == 1) {
                cout << "x  ";
            }
            if (board[i][j] == 2) {
                cout << "o  ";
            }


            if (j != 2) {
                cout << "| ";
            }
           

        }
        cout << endl;
        if (i != 2) {
            cout << "----------" << endl;
        }

    }
}


vector<vector<int>> createBoard() {

    vector<vector<int>> board
    {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };

    return board;
}
bool checkIfGameDone(vector<vector<int>> board) {

    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == board[i][1]) && (board[i][1] == board[i][2]) && (board[i][0] == board[i][2]) && board[i][0] != 0) {

            return true;
        }
    }
    for (int i = 0; i < 3; i++) {
        if ((board[0][i] == board[1][i]) && (board[1][i] == board[2][i]) && (board[0][i] == board[2][i]) && board[0][i] != 0) {

            return true;
        }
    }

    if ((board[0][0] == board[1][1]) && (board[1][1] == board[2][2]) && (board[0][0] == board[2][2]) && board[0][0] != 0) {

        return true;
    }
    if ((board[0][2] == board[1][1]) && (board[1][1] == board[2][0]) && (board[0][2] == board[2][0]) && board[0][2] != 0) {

        return true;
    }
    return false;
}

vector<vector<int>> checkIfWinning(vector<vector<int>> board, int player) {
    int counter1 = 0;
    int counter2 = 0;
    int opponent = 0;
    if (player == 1) {
        opponent = 2;
    }
    else {
        opponent = 1;
    }
    int emptyRow = 0;
    int emptyColumn = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == player) {
                counter1++;
            }
            if (board[i][j] == opponent) {
                counter2++;
            }
            if (board[i][j] == 0) {
                emptyRow = i;
                emptyColumn = j;
            }

        }
        if ((counter1 == 2 && counter2 != 1)) {
            board[emptyRow][emptyColumn] = 2;
            return board;
        }
        counter1 = 0;
        counter2 = 0;

    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[j][i] == player) {
                counter1++;
            }
            if (board[j][i] == opponent) {
                counter2++;
            }
            if (board[j][i] == 0) {
                emptyRow = j;
                emptyColumn = i;
            }

        }
        if ((counter1 == 2 && counter2 != 1)) {
            board[emptyRow][emptyColumn] = 2;
            return board;
        }
        counter1 = 0;
        counter2 = 0;
    }
    for (int i = 0; i < 3; i++) {

        if (board[i][i] == player) {
            counter1++;
        }
        if (board[i][i] == opponent) {
            counter2++;
        }
        if (board[i][i] == 0) {
            emptyRow = i;
            emptyColumn = i;
        }

    }

    if ((counter1 == 2 && counter2 != 1)) {
        board[emptyRow][emptyColumn] = 2;
        return board;
    }
    counter1 = 0;
    counter2 = 0;


    for (int i = 0; i < 3; i++) {

        if (board[i][2 - i] == player) {
            counter1++;
        }
        if (board[i][2 - i] == opponent) {
            counter2++;
        }
        if (board[i][2 - i] == 0) {
            emptyRow = i;
            emptyColumn = 2 - i;
        }

    }

    if ((counter1 == 2 && counter2 != 1)) {
        board[emptyRow][emptyColumn] = 2;
        return board;
    }
    counter1 = 0;
    counter2 = 0;

    return board;
}


vector<vector<int>> computerMove(vector<vector<int>> board) {
    vector<vector<int>> initialBoard = board;
    board = checkIfWinning(board, 2);
    if (initialBoard != board) {
        return board;
    }
    board = checkIfWinning(board, 1);
    if (initialBoard != board) {
        return board;
    }
    int row = 0;
    int column = 0;
    do {
        row = rand() % 3;
        column = rand() % 3;

    } while (board[row][column] != 0);

    board[row][column] = 2;
    return board;
}


int main()
{
    srand(time(0));
    vector<vector<int>> board = createBoard();
    printBoard(board);
    bool gameDone = false;
    int row;
    int column;
    while (!gameDone) {
        if (checkIfGameDone(board)) {
            gameDone = true;
            cout << "COMPUTER WON" << endl;
            break;
        }
        cout << "Choose a row: ";

        cin >> row;
        cout << "Choose a column: ";
        cin >> column;
        board[row - 1][column - 1] = 1;
        if (checkIfGameDone(board)) {
            gameDone = true;
            cout << "YOU WON" << endl;
            printBoard(board);
            break;
        }
        board = computerMove(board);
        printBoard(board);

    }



    return 0;
}