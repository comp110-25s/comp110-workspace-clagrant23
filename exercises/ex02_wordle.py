"""wordle exercise"""

__author__ = "730567639"


def contains_char(word: str, character: str) -> bool:
    """this function searches through word for char"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(
        word
    ):  # iterates while the index of the character is less than the word aimed at guessing.
        if word[idx] == character:
            return True
        else:
            idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess_word: str, secret_word: str) -> str:
    """This function uses contains_char to codify guesses with colors"""
    assert len(guess_word) == len(secret_word), "Guess must be same length as secret"
    index: int = 0  # declaring and initializing index variable
    wordle_str: str = (
        ""  # declaring and initializing empty string to add the box strings into to created codified box output on repl.
    )
    while index < len(
        secret_word
    ):  # iterates adding codifed emoji boxes as long as the index doesn't outgrow the secret word.
        if guess_word[index] == secret_word[index]:
            wordle_str += (
                GREEN_BOX  # adds a green box to the previous iteration of wordle_str
            )
        elif contains_char(secret_word, guess_word[index]):
            wordle_str += (
                YELLOW_BOX  # adds a yellow box to the previous iteration of wordle_str
            )
        else:
            wordle_str += (
                WHITE_BOX  # adds a white box to the previous iteration of wordle_str
            )
        index += 1
    return wordle_str  # return string made up of codified emoji boxes.


def input_guess(N: int) -> str:
    """Continue prompting player until they guess correct amount of chars"""
    player_input = str(
        input(f"Enter a {N} character word")
    )  # f string utilizing the value of N within the message
    if len(player_input) != int(
        N
    ):  # message for input by player with wrong number of characters than what was prompted
        print(f"That is not a {N} chars. Please try again!")
        return input_guess(N)
    correct_player_input = player_input
    return correct_player_input


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns_used = 0  # declare turns variable and assign it a value of 0 to iterate by one every turn
    length = len(secret)  # create variable to call input_guess with new parameter
    while (
        turns_used < 6
    ):  # only iterate loop while turns are still available to be used.
        turns_used += 1  # iterate turns_used by 1
        guess_wordle = input_guess(length)  # input_guess function call
        print(f"===Turn {turns_used}/6===")
        print(emojified(guess_wordle, secret))  # emojified function call
        if (
            guess_wordle == secret
        ):  # if function for displaying message for winning guess
            print(f"You won in {turns_used}/6 turns!")
            return None  # return None to exit if statement and while loop and return to function without printing loss message
    print("X/6 - Sorry, try again tomorrow!")  # loss message


if __name__ == "__main__":
    main(secret="codes")
