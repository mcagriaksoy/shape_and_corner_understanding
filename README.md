# shape_and_corner_understanding
This program understands the which shape is it from its corner number.

For preprocessing step, I have gatherred the image as grayscale and do the averaging filtering on image with my unique filter mask. As we know, low pass filters are using the blur the images to remove some noise and some undesired parts.

Then with the Help of Canny edge detection algorithm I have found the edges and displayed on screen. After that, corner harris method show me some corners and help me a lot for the displaying corners on the input images. But I have used another approach instead of corner harris to calculate the corner number or/nor lines of the given shape.

I have used the approxPolyDP function from openCV for aspect ratio approximation for detecting the shape, It is useful for detecting shape and working good. It uses Douglas-Peucker algorithm that moves a curve closer to another curve with less angles so that the distance between them is less than or equal to the specified precision. Also, arcLength is calculating the curve length from the shape’s perimeter.

Then finally, with many conditions I can detect and label the shapes from input image. I tested all shapes on the dataset and get acceptable results.  

