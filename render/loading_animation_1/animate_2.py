from PIL import Image
import os

def create_animated_gif(input_folder, output_file, duration=100):
    # Get list of PNG files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
    image_files.sort()  # Optional: Sort the files if they are named in sequence
    frames = [Image.open(f) for f in image_files]
    frames[0].save('test.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=40, loop=0, transparency=0)

if __name__ == "__main__":
    input_folder = os.getcwd()
    output_file = 'output.gif'
    duration = 40  # Duration of each frame in milliseconds
    create_animated_gif(input_folder, output_file, duration)
    print("...done!")
