# `nissan_bringup` ROS2 package
🚗 ROS2 package for basic functions on Nissan Leaf


Terminal 1:
```
cd ~/ros2_ws/src
git clone https://github.com/szenergy/nissan_bringup
cd ~/ros2_ws
colcon build --packages-select nissan_bringup
```

Terminal 2:
```
source ~/ros2_ws/install/local_setup.bash && source ~/ros2_ws/install/setup.bash
ros2 launch nissan_bringup nissan.leaf.bringup.2020.A.launch.py
```


## Zed 
```
colcon build --symlink-install --packages-select zed_interfaces zed_components zed_wrapper zed_ros2 --cmake-args=-DCMAKE_BUILD_TYPE=Release
```

![](https://raw.githubusercontent.com/szenergy/nissan_leaf_ros/master/nissan_bringup/meshes/Nissan_Leaf_Simulation_02_06.png)
