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
                    'gps.duro.launch.py'
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
                    get_package_share_directory('zed_wrapper'),
                    'launch',
                    'zed_no_tf.launch.py'
                )
            )
        ),
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
                    'nissan_can_control.launch.py',
                )
            )
        ),
        
        Node(
            package='nissan_bringup',
            executable='steering_path_marker',
            name='steering_path_marker_py',
        ),
        Node(
            package='nissan_bringup',
            executable='current_pose_from_tf',
            name='current_pose_from_tf',
        ),
        Node(
            package='topic_tools',
            executable='relay',
            name='cmd_relay',
            arguments=['/ctrl_raw', '/ctrl_cmd']
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'car_parameters_leaf.launch.py',
                )
            )
        ),
    ])