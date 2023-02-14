from launch import LaunchDescription
from launch_ros.actions import Node

# Path and steering markers for RVIZ

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nissan_bringup',
            executable='path_and_steering',
            name='path_and_steering_mark1',
            output='screen',
            parameters=[
                {
                    'pose_topic1': '/gps/duro/current_pose',
                    'path_topic1': '/marker_path_current',
                    'path_size': '500',
                    'publish_steer_marker': 'true',
                    'hz': '20',
                }
            ],
        ),
        Node(
            package='nissan_bringup',
            executable='path_and_steering',
            name='path_and_steering_mark2',
            output='screen',
            parameters=[
                {
                    # 'pose_topic1': '/gps/nova/current_pose',
                    'pose_topic1': '/estimated_pose',
                    'path_topic1': '/marker_path_estimated',
                    'path_size': '500',
                    'publish_steer_marker': 'false',
                    'hz': '20',
                }
            ],
        ),
    ])
