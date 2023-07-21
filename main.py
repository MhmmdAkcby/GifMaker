from PIL import Image, ImageDraw

def create_gif(image_list, output_path, duration=200):

    images = [Image.open(image) for image in image_list]

    gif_image = images[0]

    gif_image.save(
        fp=output_path,
        format='GIF',
        append_images=images[1:],
        save_all=True,
        duration=duration,
        loop=0
    )

image_list = ['image.png', 'image2.png', 'image3.png']

output_path = 'output.gif'

create_gif(image_list, output_path)
