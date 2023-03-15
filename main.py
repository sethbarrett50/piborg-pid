import time
import cv2
import numpy as np
import tborg as ThunderBorg
from pid import PID

# Initialize the ThunderBorg motor controller
TB = ThunderBorg.ThunderBorg()
TB.Init()

# Initialize the OpenCV camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set desired distance (in meters)
desired_distance = 0.5

# Set PID constants
Kp = 1.0
Ki = 0.1
Kd = 0.05

# Set motor power limit
max_power = 1.0


pid = PID(Kp, Ki, Kd)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # Detect edges in the image
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edges image
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour and its centroid
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        moment = cv2.moments(largest_contour)
        if moment["m00"] > 0:
            cx = int(moment["m10"] / moment["m00"])
            cy = int(moment["m01"] / moment["m00"])
        else:
            cx, cy = 0, 0

        # Calculate the distance to the object
        # You will need to set the focal length and sensor size of your camera here
        focal_length = 500
        real_object_height = 150
        object_height = largest_contour.shape[0]
        sensor_height = 3.68
        distance = focal_length * real_object_height * frame.shape[0] / object_height / sensor_height / 1000

        # Calculate error (desired distance - current distance)
        error = desired_distance - distance

        # Update PID controller and get output value
        output_value = pid.update(error)

        # Convert output value to motor power
        motor_power = output_value * max_power

        # Set motor speed based on output value
        if motor_power > 0:
            TB.SetMotor1(motor_power)
            TB.SetMotor2(motor_power)
        else:
            TB.SetMotor1(-motor_power)
            TB.SetMotor2(-motor_power)

    time.sleep(0.1)

cap.release()
TB.SetMotor1(0)
TB.SetMotor2(0)
TB.Exit()