from launch import LaunchDescription
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from os import path

def generate_launch_description():
    return LaunchDescription([
        GroupAction(
            actions=[
                PushRosNamespace(LaunchConfiguration('velodyne_left')),

                Node(
                    package='nodelet',
                    executable='nodelet',
                    name='lidar_nodelet_manager',
                    output='screen',
                    arguments=['manager'],
                ),
                Node(
                    package='nodelet',
                    executable='nodelet',
                    name='velodyne_left_driver',
                    arguments=['load velodyne_driver/DriverNodelet lidar_nodelet_manager'],
                    parameters=[
                        {
                            'device_ip': '192.168.1.13',
                            'port': '1272',
                            'frame_id': 'velodyne_left',
                            'manager': 'lidar_nodelet_manager',
                            'model': 'VLP16',
                            'pcap': '',
                            'rpm': '1200',
                            'cut_angle': '0.01',
                            'read_fast': 'false',
                            'read_once': 'false',
                            'read_once': '0.0',
                        }
                    ],
                ),
                Node(
                    package='nodelet',
                    executable='nodelet',
                    name='cloud_nodelet',
                    arguments=['load velodyne_pointcloud/CloudNodelet lidar_nodelet_manager'],
                    parameters=[
                        {
                            'calibration': path.join(
                                get_package_share_directory('velodyne_pointcloud'),
                                'params',
                                'VLP16db.yaml',
                            ),
                            'max_range': '130.0',
                            'min_range': '0.4',
                            'manager': 'lidar_nodelet_manager',
                        }
                    ],
                ),
            ]
        ),
    ])
