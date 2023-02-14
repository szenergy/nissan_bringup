from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('hostname', default_value=TextSubstitution(text='192.168.1.12')),
        
        Node(
            package='sick_scan',
            executable='sick_generic_caller',
            name='sick_lms_1xx',
            respawn=True,
            output='screen',
            parameters=[
                {
                    'frame_id': 'laser',
                    'use_binary_protocol': True,
                    'scanner_type': 'sick_lms_1xx',
                    'device_number': 1,
                    'range_max': 25.0,
                    'hostname': LaunchConfiguration('hostname'),
                    'port': '2112',
                    'timelimit': 5,
                    'scan_freq': 25,
                    'ang_res': 0.25,
                }
        ]),
        
    ])
