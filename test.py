#Файл, в котором, очевидно из названия, проводятся всякие тесты
import cv2

img = cv2.imread('Images/chipap.png')
#cv2.imshow('Penis', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Nigger', gray)

haar_cascade = cv2.CascadeClassifier('haar_faces.xml')
haar_cascade_profile = cv2.CascadeClassifier('haar_profile_faces.xml')
haar_cascade_body = cv2.CascadeClassifier('haar_body.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=3)
faces_rect_profile = haar_cascade_profile.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)
body_rect = haar_cascade_body.detectMultiScale(gray, scaleFactor=1.045, minNeighbors=3)

print(len(faces_rect), len(faces_rect_profile), len(body_rect))
print(faces_rect)
print(faces_rect_profile)
print(body_rect)

#  |  Попытка сделать обнаружение ч/з каскады хаара (профиль + анфас, т. к. модели для головы нету).
#  |  Часто срабатывает "анфас" и "профиль" одновременно, следовательно, ставится лишний прямоугольник.
#  V  Костыль на костыле и костылём погоняет.
if len(faces_rect) == len(faces_rect_profile) == 0:
    print('Рож не найдено')

elif len(faces_rect) >= len(faces_rect_profile):
    print('faces_rect >= faces_rect_profile')
    for (x, y, w, h) in faces_rect:
        f = True
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        if len(faces_rect_profile) > 0:
            for (xp, yp, wp, hp) in faces_rect_profile:
                if abs(xp - x) >= 50 and abs(yp - y) >= 50 == False:
                    f = False
            if f:
                cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (0, 255, 0), thickness=2)

else:
    print('faces_rect_profile > faces_rect')
    for (xp, yp, wp, hp) in faces_rect_profile:
        f = True
        cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (0, 255, 0), thickness=2)
        if len(faces_rect) > 0:
            for (x, y, w, h) in faces_rect:
                if abs(xp - x) >= 50 and abs(yp - y) >= 50 == False:
                    f = False
            if f:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

#  V Full-Body (хуита)
#for (x, y, w, h) in body_rect:
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255),thickness=2)

cv2.imshow('Rect faces', img)
cv2.waitKey(0)