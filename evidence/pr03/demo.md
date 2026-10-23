
# PR03 — Demonstration

## 1. Build

Command:
colcon build --symlink-install --packages-select patrol

## 2. Broken connection

Command:
ros2 run patrol patrol

Result:
The turtle does not move because the topic names
do not match.

## 3. Fixed connection

Command:
ros2 run patrol patrol --ros-args -r cmd_vel:=/turtle1/cmd_vel

Result:
The turtle moves along a curved path.

## 4. Verification

Commands:
ros2 topic echo /turtle1/pose --once
ros2 topic echo /turtle1/cmd_vel --once
ros2 topic hz /turtle1/cmd_vel

Expected frequency: approximately 10 Hz.
