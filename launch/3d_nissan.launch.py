from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nissan_bringup',
            executable='global_parameter',
            name='car_parameters',
            parameters=[
                {
                    'robot_description': PathJoinSubstitution([
                        get_package_share_directory('nissan_bringup'),
                        'param',
                        'nissan_leaf_robotdescription.ref.xml'
                    ])
                }
            ],
        ),
    ])
