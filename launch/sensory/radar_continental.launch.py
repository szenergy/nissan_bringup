from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='radar_conti',
            executable='radar_conti',
            name='radar_conti_1',
            output='screen',
        ),
    ])
