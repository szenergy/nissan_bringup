from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from os import path

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'velodyne_left.launch.py'
                ),
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'velodyne_right.launch.py'
                ),
            ),
        ),
    ]
)
