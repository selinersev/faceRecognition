import face_recognition
import cv2

def main():
    path = "/Users/selinersev/Desktop/SeniorProject/group_dataset/"

    for i in range(1,11):
        img_path = str(path)+str(i)+'.png'
        frame = cv2.imread(img_path)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Display the resulting image
        cv2.imshow(str(i), frame)
        cv2.waitKey(10)

    cv2.waitKey(0)


def print_result(filename, location):
    top, right, bottom, left = location
    print("{},{},{},{},{}".format(filename, top, right, bottom, left))


if __name__ == "__main__":
    main()

