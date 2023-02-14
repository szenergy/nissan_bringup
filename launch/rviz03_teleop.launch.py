from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rviz',
            executable='rviz',
            name='rviz_nissan',
            arguments=[
                '-d',
                os.path.join(
                    get_package_share_directory('nissan_bringup'),
                    'rviz',
                    'leaf03_teleop.rviz'
                )
            ],
        ),
    ])
