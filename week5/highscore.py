
def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


def is_high_score_and_save(score):

    # Get the current high score
    high_score = get_high_score()

    # set variable to true if high score
    is_high_score = score > high_score

    # Only save score if its a high score
    if is_high_score:
        save_high_score(score)

    # return the result
    return is_high_score


def main():
    """ Main program is here. """

    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for his/her score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if is_high_score_and_save(current_score):
        # We do! Save to disk
        print("Yea! New high score!")
        # save_high_score(current_score)
    else:
        print("Better luck next time.")

# Call the main function, start up the game
if __name__ == "__main__":
    main()
