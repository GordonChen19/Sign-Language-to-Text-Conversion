import os

import cv2

dataset_size = 200

cap = cv2.VideoCapture(0) #Continuity Camera

classes=[chr(i+97) for i in range(26)]
classes.append('space')

print(classes)
dataset_path='dataset'

for letter in classes:
    if not os.path.exists(os.path.join(dataset_path,letter)):
        os.makedirs(os.path.join(dataset_path,letter))

    print('Collecting data for letter {}'.format(letter))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "q" !', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(dataset_path, str(letter), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()