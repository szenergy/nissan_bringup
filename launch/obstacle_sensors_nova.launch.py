from launch import LaunchDescription
from launch_ros.actions import Node
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
                    'ouster_right.launch.py'
                )
            )
        ),
        # Start Nova
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'tf_setup',
                    'tf_nova_static.launch.py'
                )
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'gps.duro.launch.py'
                )
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'tf_setup',
                    'tf_static.launch.py'
                )
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('can_leaf_driver'),
                    'launch',
                    'nissan_can_control.launch.py'
                )
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'gps.nova.launch.py'
                )
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('ros_guis'),
                    'launch',
                    'temporary.launch.py'
                )
            )
        ),

        # params
        Node(
            package='nissan_bringup',
            executable='global_parameter',
            name='obstacle_duro_params',
            parameters=[
                {
                    'gps': 'nova',
                    'waypoint_file_name': '/mnt/storage_1tb/waypoint/zala_egyetemi_demo_nova.csv',
                }
            ],
        ),
    ])
