# `nissan_bringup` ROS2 package
🚗 ROS2 package for basic functions on Nissan Leaf


## Install:
```
cd ~/ros2_ws/src
git clone https://github.com/szenergy/nissan_bringup
cd ~/ros2_ws
colcon build --packages-select nissan_bringup
```

# Other packages

## Links
- [ZED](https://github.com/stereolabs/zed-ros2-wrapper)
- [ouster](https://github.com/ros-drivers/ros2_ouster_drivers/tree/humble)
- [duro gps](https://github.com/szenergy/duro_gps_driver/tree/ros2-humble)
- [novatel gps](https://github.com/novatel/novatel_oem7_driver/tree/humble)
- [SICK lidar](https://github.com/szenergy/sick_scan2)

## Zed 
```
colcon build --symlink-install --packages-select zed_interfaces zed_components zed_wrapper zed_ros2 --cmake-args=-DCMAKE_BUILD_TYPE=Release
```

![](https://raw.githubusercontent.com/szenergy/nissan_leaf_ros/master/nissan_bringup/meshes/Nissan_Leaf_Simulation_02_06.png)
