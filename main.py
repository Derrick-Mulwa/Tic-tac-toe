#Tictactoe game on the terminal
#create the layout

numbered_layout = f" 1 | 2 | 3 \n"\
                  f"___|___|___\n" \
                  f" 4 | 5 | 6 \n" \
                  f"___|___|___\n" \
                  f" 7 | 8 | 9 \n" \
                  f"   |   |   \n"

# Lists to store users values

played = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
guide_list = ['1', '2', '3', '4', '5', '6', '7', '8',"9"]


# Function to check whether user input is a previously selected cell with data in it
def verify_grid(num):
    if played[num] == ' ':
        return True
    else:
        return False


# Function to get a valid user input, no letters, wrong numbers, or previously selected cells
def get_valid_input():
    valid = False

    while valid is False:
        user_input = input("Enter cell to play: ")

        try:
            user_input = int(user_input) - 1

            if 0 <= user_input < 9:
                if verify_grid(user_input) is True:
                    return user_input
                else:
                    print(f"The selected cell has been used! Refer to this grid and select unused cell")
                    display_unused_grids()
            else:
                print(f"{user_input} is an invalid cell! Refer to this grid and select unused cell")
                display_unused_grids()
        except:
            print(f"{user_input} is an invalid cell! Refer to this grid and select unused cell")
            display_unused_grids()


# Function to update the lists that store users values for player X
def x_play(num):
    played[num] = "X"
    guide_list[num] = "X"


# Function to update the lists that store users values for player O
def o_play(num):
    played[num] = "O"
    guide_list[num] = "O"


# Function to display the updated grid with updated values after a player plays
def display_game():
    play_layout = f" {played[0]} | {played[1]} | {played[2]} \n" \
                  f"___|___|___\n" \
                  f" {played[3]} | {played[4]} | {played[5]} \n" \
                  f"___|___|___\n" \
                  f" {played[6]} | {played[7]} | {played[8]} \n" \
                  f"   |   |   \n"
    return play_layout


# Function to show the grid with numbers on empty cells.
# This is for guiding players who forgot cell labeling
def display_unused_grids():
    play_layout = f" {guide_list[0]} | {guide_list[1]} | {guide_list[2]} \n" \
                  f"___|___|___\n" \
                  f" {guide_list[3]} | {guide_list[4]} | {guide_list[5]} \n" \
                  f"___|___|___\n" \
                  f" {guide_list[6]} | {guide_list[7]} | {guide_list[8]} \n" \
                  f"   |   |   \n"
    print(play_layout)


# Function to update changes when players change
def update_changes(turn, num):
    if turn == "X":
        x_play(num)
    else:
        o_play(num)


# Function to find whose player's turn it is
def get_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


# Function to reset all variables when a new game begins
def reset_status():
    for i in range(len(played)):
        played[i] = ' '

    for i in range(len(guide_list)):
        guide_list[i] = f"{i+1}"

    turn = 1


# Function to check whether there is a combination for a win
def check_win():
    combinations = ['012', '345', '678', '036', '147', '258', '048', '246']
    win = 0

    for combination in combinations:
        pattern = played[int(combination[0])] + played[int(combination[1])] + played[int(combination[2])]
        if pattern in ["XXX", "OOO"]:
            win += 1
            win_pattern = pattern
        else:
            continue

    if win >= 1:
        return True, win_pattern
    else:
        return False


# Function to play the game and link all functions
def play():

    games = 1
    x, y,z = 0, 0, 0
    playing = True

    while playing is True:
        played = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        guide_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        turn = 1

        if games == 1:
            print("Welcome to Tictactoe. Select a cell using the template below.")
            display_unused_grids()
        else:
            print(f"\nROUND {games}!\nX : {x}|Draw : {z}| O : {y}")

        while check_win() is False:
            if turn <= 9:
                player = get_turn(turn)
                print(display_game())
                print(f"{player}'s turn!")
                user_input = get_valid_input()
                update_changes(player, user_input)

                turn += 1


            else:
                z += 1
                break

        if check_win() is False:
            print(display_game())
            if_continue = input(f"Out of moves! Game ends at a Draw!\nX : {x}|Draw : {z}| O : {y}\n\n"
                                f"Press 1 to play another round or any other key to EXIT: ")
        else:
            print(display_game())
            winner = check_win()
            winner = winner[1]
            if winner == "XXX":

                x += 1
                if_continue = input(f"X WINS THIS ROUND!\nX : {x}|Draw : {z}| O : {y}\n\n"
                                    f"Press 1 to play another round or any other key to EXIT: ")
            else:
                y += 1
                if_continue = input(f"O WINS THIS ROUND!\nX : {x}|Draw : {z}| O : {y}\n\n"
                                    f"Press 1 to play another round or any other key to EXIT: ")

# Check if player want to play or quit
        if if_continue == "1":
            games += 1
            reset_status()

        else:
            playing = False

            
# Run the play function to play
play()

