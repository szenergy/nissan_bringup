from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from os import path

# Nissan Bringup verison 2020.A:
# - LIDAR: 2 x Ouster OS1-64
# - LIDAR: 2 x Velodyne VLP-16
# - LIDAR: 1 x Sick LMS-111
# - RADAR: 1 x Continental ARS-408
# - GPS:   1 x SwiftNav Duro Inertial
# - GPS:   1 x NovAtel PW7720E1-DDD-RZN-TBE-P1 (map->base_link nova_global_frame_tf_publisher.launch) 
# - CAM:   1 x Stereolabs Zed
# - CAN:   nissan_can_control.launch
# - TF:    nissanleaf_statictf_launch.launch
# - Car parameters: car_parameters_leaf.launch

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'ouster_two_lidar.launch.py'
                )
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'velodyne_two_lidar.launch.py'
                )
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'sick_lms_111.nissan.launch.py'
                )
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'radar_continental.launch.py'
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

        ## Start Duro
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         path.join(
        #             get_package_share_directory('nissan_bringup'),
        #             'launch',
        #             'tf_setup',
        #             'tf_duro_static.launch.py'
        #         )
        #     )
        # ),

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

        # temporary fix TODO
        Node(
            package='nissan_bringup',
            executable='current_pose_from_tf',
            name='current_pose_from_tf',
        ),

        Node(
            package='topic_tools',
            executable='relay',
            name='cmd_relay',
            arguments=['/ctrl_raw', '/ctrl_cmd'],
        ),

        # Node(
        #     package='pcl_ros',
        #     executable='pcd_to_pointcloud',
        #     name='pcd_to_pointcloud',
        #     arguments=[get_package_share_directory('nissan_bringup') + '/utils/zala_egyetemi_ascii_demo_map.pcd', '10', '_frame_id:=map_zala_0'],
        # ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    'sensory',
                    'car_parameters_leaf.launch.py'
                )
            )
        ),
    ])
