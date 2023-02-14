from launch import LaunchDescription
from launch_ros.actions import Node

# Launch nodes for Shell parking challange.

def generate_launch_description():
    return LaunchDescription([
        # publish necessary topics for MPC waypoint converter
        Node(
            package='nissan_bringup',
            executable='bare_planner.py',
            name='bare_planner_py',
        ),
        Node(
            package='nissan_bringup',
            executable='global_waypoint_monitor.py',
            name='global_waypoint_monitor_py',
        ),
    ])
