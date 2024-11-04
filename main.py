import cv2

capture = cv2.VideoCapture('Videos/BUS52.mp4')

haar_cascade = cv2.CascadeClassifier('haar_faces.xml')
haar_cascade_profile = cv2.CascadeClassifier('haar_profile_faces.xml')

while True:
    isTrue, frame = capture.read()

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # | Здесь можно баловаться со scaleFactor и minNeigbors для получения разного результата
    # V Изначально: scaleFactor=1.1, minNeighbors=3
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    faces_rect_profile = haar_cascade_profile.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    print(len(faces_rect), len(faces_rect_profile))
    print(faces_rect)
    print(faces_rect_profile)

    if len(faces_rect) == len(faces_rect_profile) == 0:
        print('Лиц не найдено')

    elif len(faces_rect) >= len(faces_rect_profile):
        print('faces_rect >= faces_rect_profile')
        for (x, y, w, h) in faces_rect:
            f = True
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            if len(faces_rect_profile) > 0:
                for (xp, yp, wp, hp) in faces_rect_profile:
                    if abs(xp - x) >= 50 and abs(yp - y) >= 50 == False:
                        f = False
                if f:
                    cv2.rectangle(frame, (xp, yp), (xp + wp, yp + hp), (0, 255, 0), thickness=2)

    else:
        print('faces_rect_profile > faces_rect')
        for (xp, yp, wp, hp) in faces_rect_profile:
            f = True
            cv2.rectangle(frame, (xp, yp), (xp + wp, yp + hp), (0, 255, 0), thickness=2)
            if len(faces_rect) > 0:
                for (x, y, w, h) in faces_rect:
                    if abs(xp - x) >= 50 and abs(yp - y) >= 50 == False:
                        f = False
                if f:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

    cv2.imshow('Nigger Killer', frame)

capture.release()
cv2.destroyAllWindows()