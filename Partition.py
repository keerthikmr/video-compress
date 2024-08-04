import os
from PIL import Image

frame = Image.open('Frames\\frame_0.jpg')

rows, cols = 2, 2
frame_count = 0
seg_num = 0

segment_height = frame.size[1] // rows
segment_width = frame.size[0] // cols

output_directory = "Segments"


for path in os.listdir("Frames"):
    frame = Image.open(os.path.join("Frames", f'frame_{frame_count}.jpg'))

    for row in range(rows):
        for col in range(cols):
            x1, y1 = col * segment_width, row * segment_height
            x2, y2 = (col + 1) * segment_width, (row + 1) * segment_height
            segment = frame.crop((x1, y1, x2, y2))

            segment_filename = os.path.join("Segments", f'segment_{seg_num}.jpg')
            segment.save(segment_filename)
            seg_num += 1
    
    frame_count += 1