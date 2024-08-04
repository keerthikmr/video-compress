import imageio
import os

video_reader = imageio.get_reader('C:\\Users\\Admin\\Downloads\\Video\\Sports_360P-1d5c.mkv')

output_directory = 'Frames'

frame_number = 0

for frame in video_reader:
    frame_filename = os.path.join(output_directory, f'frame_{frame_number}.jpg')
    imageio.imwrite(frame_filename, frame)
    frame_number += 1
