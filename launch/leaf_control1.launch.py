from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_guis',
            executable='leaf_control1.py',
            name='leaf_control1_launch',
            output='screen',
        ),
    ])