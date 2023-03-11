# PyBorg PID Distance Control
This repository contains Python code for controlling a PiBorg robot using OpenCV, a PID controller, and the ThunderBorg library. The robot is designed to follow a lead car at a set distance.

## Requirements
To use this code, you will need:
-Raspberry Pi with Raspbian OS
-PiBorg ThunderBorg motor controller
-Raspberry Pi camera module
-OpenCV library
-Python 3.x

## Usage
To use the code, follow these steps:

1.Clone the repository to your Raspberry Pi.
1.Install the required libraries (OpenCV and ThunderBorg) using their respective installation 1.instructions.
1.Connect the Raspberry Pi camera module and the ThunderBorg motor controller to the Raspberry Pi.
1.Connect the motor controller to the robot's motors.
1.Modify the desired_distance variable in the pid_loop function to set the desired distance between the lead car and the robot.
1.Run the pid_controller.py file with Python 3.x.

## License
This repository is licensed with the Unlicense, which means you can use the code for any purpose without any restrictions. See the LICENSE file for more information.

## Acknowledgements
This code was developed as the final project for a PHD Cyber Physical Systems class. It is intended to be used by the GenCyber camp during their summer camp, and may also be used for a personal publishable research paper.

