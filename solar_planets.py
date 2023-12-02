import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (120,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (195,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (390,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (570,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (790,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (980,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1120,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.imshow("result",img)

cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
