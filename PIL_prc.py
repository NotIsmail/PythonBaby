

# Don't worry this code is way outta my league 

# it is about using library functions named PIL which help in visualizing images

from PIL import Image

# Provide the filenames directly within the script
image_filenames = ["spidey3.jpg", "spidey4.jpg"]  # Replace these with your image filenames

images = []
for filename in image_filenames:
    image = Image.open(filename)
    images.append(image)

# Assuming there are at least two images in the list
if len(images) >= 2:
    images[0].save(
        "spidey.gif", save_all=True, append_images=images[1:], duration=200, loop=0
    )
else:
    print("At least two images are required to create the GIF.")

