from PIL import Image
import os

def ascii_sum(string):
    return sum(ord(char) for char in string)

frame_count = 0
segment_count = 0
difference = 0
add = 0
row, col = 2, 2
inc = row * col

segment1 = Image.open(os.path.join("Segments", "segment_0.jpg"))
pixels = segment1.width * segment1.height


for path in sorted(os.listdir("Segments")):
    
    segment1 = Image.open(os.path.join("Segments", f'segment_{segment_count}.jpg'))
    segment2 = Image.open(os.path.join("Segments", f'segment_{segment_count + inc}.jpg'))
                 
    pixels1 = list(segment1.getdata())
    pixels2 = list(segment2.getdata())

    for pixel1, pixel2 in zip(pixels1, pixels2):
        for c1, c2 in zip(pixel1, pixel2):
            add += abs(c1 - c2)

        difference += add
        add = 0
    
    average_difference = difference / pixels
        
    print(f"Average Pixel-Wise Difference: {average_difference}")
    difference = 0
    segment_count += 1
