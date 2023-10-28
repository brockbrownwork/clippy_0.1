from PIL import Image
import os

def create_animated_gif(input_folder, output_file, duration=100):
    # Get list of PNG files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
    image_files.sort()  # Optional: Sort the files if they are named in sequence
    
    # Open the image files
    images = [Image.open(os.path.join(input_folder, img_file)) for img_file in image_files]
    
    # Convert images to RGBA (if not already in this mode)
    images = [img.convert('RGBA') for img in images]
    
    # Save as an animated GIF
    images[0].save(output_file, save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0, transparency=0)

if __name__ == "__main__":
    input_folder = os.getcwd()
    output_file = 'output.gif'
    duration = 40  # Duration of each frame in milliseconds
    create_animated_gif(input_folder, output_file, duration)

    frames = [Image.open('red.png'), Image.open('green.png'), Image.open('blue.png')]

    frames = [frame.convert('PA') for frame in frames]

    frames[0].save('test.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=200, loop=0, transparency=0)
