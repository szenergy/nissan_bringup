from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from os import path

def generate_launch_description():
    return LaunchDescription([
        GroupAction(
            actions=[
                PushRosNamespace(LaunchConfiguration('right_os1')),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        path.join(
                            get_package_share_directory('nissan_bringup'),
                            'launch',
                            'sensory',
                            'ouster_instance.launch.py'
                        )
                    ),
                    launch_arguments={
                        'sensor_hostname': '192.168.2.16',
                        'udp_dest': '192.168.2.1',
                        'lidar_port': '7504',
                        'imu_port': '7505',
                        'tf_prefix': 'right_os1',
                    }
                ),
            ]
        ),
    ]
)
