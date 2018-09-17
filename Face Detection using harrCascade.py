
# coding: utf-8

# In[ ]:


import cv2 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


def face_detection(image,classifier,scale):
    img = image.copy() #this makes the copy of original image
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #coverts 
    faces_found = classifier.detectMultiScale(img_gray,scaleFactor=scale,minNeighbors=5)
    print('Faces found',len(faces_found))
    for (x,y,w,h) in faces_found:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    img  = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)    
    return img    


# In[ ]:


path_of_image = input()
test  = cv2.imread(path_for_image)
path_of_harrcascade = input()
haar_face_cascade = cv2.CascadeClassifier(path_of_harrcascade)


# In[ ]:


x = face_detection(test,haar_face_cascade,1.1) 


# In[ ]:


plt.imshow(x)

