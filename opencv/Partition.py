import os
import cv2

frame = cv2.imread('Frames\\frame_0.jpg')

rows, cols = 2, 2

segment_width = frame.shape[1] // cols
segment_height = frame.shape[0] // rows

segments = []  # To store the extracted segments

frames_path = "Frames"
frame_count = 0

for path in os.listdir("Frames"):
    frame = cv2.imread(os.path.join("Frames", f'frame_{frame_count}.jpg'))

    for row in range(rows):
        for col in range(cols):
            # Calculate coordinates for the current segment
            x1 = col * segment_width
            y1 = row * segment_height
            x2 = (col + 1) * segment_width
            y2 = (row + 1) * segment_height

            # Extract the segment from the frame
            segment = frame[y1:y2, x1:x2]

            # Append the segment to the list
            segments.append(segment)

            segment_filename = os.path.join("Segments", f'frame_{frame_count}_segment_{row}_{col}.jpg')

            cv2.imwrite(segment_filename, segment)
        
    frame_count += 1
