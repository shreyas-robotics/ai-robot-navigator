# AI Robot Navigator (ROS2)

Autonomous robot navigation using LiDAR.

## How it works

1. Robot reads LiDAR data from /scan
2. If obstacle distance < 0.5m → STOP
3. If path clear → MOVE FORWARD

## ROS2 Topics

Subscribe:
 /scan

Publish:
 /cmd_vel

## Node

navigator