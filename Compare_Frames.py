from PIL import Image
import os

frame_count = 0
difference = 0
sum = 0


image1 = Image.open(os.path.join("Frames", "frame_0.jpg"))

pixels = image1.width * image1.height

for path in os.listdir("Frames"):

    image1 = Image.open(os.path.join("Frames", f'frame_{frame_count}.jpg'))
    image2 = Image.open(os.path.join("Frames", f'frame_{frame_count+1}.jpg'))
                    
    pixels1 = list(image1.getdata())
    pixels2 = list(image2.getdata())

    for pixel1, pixel2 in zip(pixels1, pixels2):
        for c1, c2 in zip(pixel1, pixel2):
            sum += abs(c1 - c2)

        difference += sum
        sum = 0
    
    average_difference = difference / pixels
        
    print(f"Average Pixel-Wise Difference: {average_difference}")
    difference = 0
    frame_count += 1
