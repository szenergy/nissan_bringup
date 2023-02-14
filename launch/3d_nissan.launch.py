from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nissan_bringup',
            executable='global_parameter',
            name='car_parameters',
            parameters=[
                {
                    'robot_description': PathJoinSubstitution([
                        LaunchConfiguration('nissan_bringup'),
                        'param',
                        'nissan_leaf_robotdescription.ref.xml'
                    ])
                }
            ],
        ),
    ])
