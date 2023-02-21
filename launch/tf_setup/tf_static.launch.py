from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from os import path

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='gyor0_tf_publisher',
            output='screen',
            ##  Old-style arguments are deprecated, parameters should be used, but this does not work TODO
            arguments=['697237.0', '5285644.0', '0.0','0', '0', '0', '1','map','map_gyor_0'],
            #parameters=[{'translation.x': 697237.0, 'translation.y': 5285644.0, 'translation.z': 0.0, 'rotation.x': 0.0, 'rotation.y': 0.0, 'rotation.z': 0.0, 'rotation.w': 1.0, 'frame_id': 'map', 'child_frame_id': 'map_gyor_0'}]
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='zala0_tf_publisher',
            output='screen',
            arguments=['639770.0', '5195040.0', '0.0','0', '0', '0', '1','map','map_zala_0'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='duro_gps_tf_publisher',
            output='screen',
            arguments=['0.0', '0.0', '0.2', '0.0261799', '0.0', '0.0', 'base_link','duro_gps'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='velodyne_left_tf_publisher',
            output='screen',
            arguments=['1.749', '0.703', '1.166', '0.0', '0.0', '-1.0471975511965976', 'base_link', 'velodyne_left'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='zed2_camera_center_tf_publisher',
            output='screen',
            arguments=['1.874', '0.0', '1.286', '0.0', '0.0', '0.0', 'base_link', 'zed2_camera_center'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='velodyne_right_tf_publisher',
            output='screen',
            arguments=['1.749', '-0.703', '1.166', '0.0', '0.0', '1.0471975511965976', 'base_link', 'velodyne_right'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='sick_tf_publisher',
            output='screen',
            arguments=['3.707', '-0.351', '0.113', '0.0', '0.0', '0.0', 'base_link', 'laser'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='conti_tf_publisher',
            output='screen',
            arguments=['3.707', '', '0.360', '0.113', '0.0', '0.0', '0.0', 'base_link', 'radar'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='duro_gps_imu_tf_publisher',
            output='screen',
            arguments=['0.0', '0.0', '0.2', '0.0', '0.0', '0.0', 'base_link', 'duro_gps_imu'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='base_link_ground_link_publisher',
            output='screen',
            arguments=['0.0', '0.0', '-0.316', '0.0', '0.0', '0.0', 'base_link', 'ground_link'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_left_tf_publisher',
            output='screen',
            arguments=['1.769', '0.58', '1.278', '0.0', '0.0', '0.0', 'base_link', 'os_left'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_right_tf_publisher',
            output='screen',
            arguments=['1.769', '-0.58', '1.278', '0.0', '0.0', '0.0', 'base_link', 'os_right'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_sensor_lidar_left',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'os_left', 'os_left_data_frame'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_sensor_imu_left',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'os_left', 'os_left_imu_data_frame'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_sensor_lidar_right',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'os_right', 'os_right_data_frame'],
        ),
        Node(
            package='tf2_ros',
            #namespace='nissan1',
            executable='static_transform_publisher',
            name='os_sensor_imu_right',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'os_right', 'os_right_imu_data_frame'],
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                path.join(
                    get_package_share_directory('nissan_bringup'),
                    'launch',
                    '3d_nissan.launch.py'
                )
            )
        ),
        # TODO: launch and executeable file missing
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         path.join(
        #             get_package_share_directory('nissan_bringup'),
        #             'launch',
        #             'path_and_steering_marker.launch.py'
        #         )
        #     )
        # ),
    ])