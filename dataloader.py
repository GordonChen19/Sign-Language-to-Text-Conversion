import os
import mediapipe as mp
import cv2
import pickle

DataDirectory = '/Users/gordonchen/Desktop/Signalife/dataset/'

data=[]
labels=[] #Delete

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

print("Unpacking data...")
for target_class in os.listdir(DataDirectory):
    print(target_class)
    print(DataDirectory)
    class_image_path = os.path.join(DataDirectory,target_class)
    if target_class.startswith('.'):
        continue
    
    for img in os.listdir(class_image_path):
        data_aux = []

        x_ = []
        y_ = []
        
        img_path = os.path.join(class_image_path,img)
        print(f'reading {img_path}')
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results= hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(target_class)

f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
