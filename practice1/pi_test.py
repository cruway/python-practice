import time

from PIL import Image
from picharsso import new_drawer
from picharsso.utils import clear_screen, terminal_size


if __name__ == "__main__":
    # Open image
    image = Image.open("img_1.png")

    # Get terminal height
    height, _ = terminal_size()

    # Define drawer
    drawer = new_drawer("braille", height=height, colorize=True, threshold=0)

    # Iterate over frames
    texts = []
    for frame_id in range(image.n_frames):
        # Select frame
        image.seek(frame_id)

        # Save output for frame
        texts.append(drawer(image))

    # Iterate over saved outputs in a circular manner
    num_frames = len(texts)
    counter = 0
    while True:
        # Refresh
        clear_screen()

        # Print output
        print(texts[counter])

        # Set a delay between frames
        time.sleep(1 / num_frames)

        # Circular increment
        counter = (counter + 1) % num_frames