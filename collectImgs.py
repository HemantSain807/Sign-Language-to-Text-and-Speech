import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Only 26 alphabets
classes = [chr(i) for i in range(65, 91)]  # ['A', 'B', ..., 'Z']
dataset_size = 100  # recommended for better accuracy

cap = cv2.VideoCapture(0)

for class_name in classes:
    class_path = os.path.join(DATA_DIR, class_name)
    if not os.path.exists(class_path):
        os.makedirs(class_path)

    print(f'\nCollecting data for class "{class_name}"')

    # Wait for user to start
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Class: {class_name} - Press "Q" to Start', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Start collecting
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_path, f'{counter}.jpg'), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
