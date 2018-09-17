# Face-detection
A]For face detection using opencv following libraries must be installed 
   1.OpenCV (Obviously)
   2.Matplotlib 

B]While working with OpenCV following things must kept in head:
1. OpenCV reads any image in BGR color-space
2. As many operations in OpenCV are performed in grayscale(for better performance) so we have to convert image read by OpenCV(which are in BGR color-space) into grayscale

c]Classifiers in OpenCV: 
   A classifier is program which decides wheather an image a positive image(face image) or negetive image(non-face image).A classifier is trained on hundreds of thousands of face and non-face images to learn how to classify a new image correctly.There are two types of classifiers present in OpenCV: 1}  Harr classifier , 2}LBP classifier
