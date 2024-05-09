from pygame import mixer


def load_audio(path):
    """A simple program for playing audio files using the pygame.mixer module.

    This script loads and plays an audio file specified by the user. It allows the user to interact
    with the audio by pausing, resuming, or exiting the program.

    Usage:
        - Specify the path to the audio file as an argument when calling the 'load_audio' function.
        - The program will play the specified audio file and provide options to pause, resume, or exit.

    Controls:
        - Press 'p' and enter to pause the audio.
        - Press 'r' and enter to resume the audio.
        - Press 'e' and enter to exit the audio program.

    Functions:
        - load_music(path): Loads and plays the audio file specified by the path argument.

    Args:
        - path (str): The path to the audio file to be loaded and played.

    Requirements:
        - Pygame library must be installed to run this script.

    Note:
        This script assumes a basic understanding of Pygame and audio file handling.
    """

    if path:
        mixer.init()

        mixer.music.load(path)
        mixer.music.set_volume(1.0)
        mixer.music.play()

        while True:
            print("Press 'p' key and enter to pause the Audio")
            print("Press 'r' key and enter to resume the Audio")
            print("Press 'e' key and enter to exit the Audio program")

            user_entry = input("")

            if user_entry == 'p' or user_entry == 'P':
                mixer.music.pause()
                print("Music paused, press 'r' key and enter to resume")
            elif user_entry == 'r' or user_entry == 'R':
                mixer.music.unpause()
            elif user_entry == 'e' or user_entry == 'E':
                mixer.music.stop()
                break
    else:
        print("Please, specify the audio path")

# load_audio("")
load_audio('Always-Pray-For-You.mp3')