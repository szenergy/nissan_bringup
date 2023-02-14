from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gps_tf_publisher',
            executable='gps_tf_publisher',
            name='duro_leaf_tf_publisher',
            output='screen',
            remappings=[
                ('gps/current_pose', 'gps/duro/current_pose'),
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='duro_static_tf_publisher',
            output='screen',
            remappings=[
                ('gps/current_pose', 'gps/duro/current_pose'),
            ],
            arguments=['0.196', '0.0', '-1.1', '0.0', '0.0', '0.0', 'gps', 'base_link'],
        ),
    ])