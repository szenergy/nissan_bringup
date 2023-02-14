from launch import LaunchDescription
from launch_ros.actions import Node

# Simple Demo launch - following waypoints with MPC

def generate_launch_description():
    return LaunchDescription([
        # Load waypoints csv and necessary publish topics fro MPC waypoint converter
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
        # TODO: umiklos
        Node(
            package='nissan_bringup',
            executable='waypoint_loader.py',
            name='waypoint_loader_py',
            output='screen',
        ),
    ])
