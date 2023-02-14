from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from os import path

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('camera_name', default_value=TextSubstitution(text='zed1')),
        DeclareLaunchArgument('camera_model', default_value=TextSubstitution(text='zed')), # 'zed' or 'zedm' or 'zed2'
        DeclareLaunchArgument('node_name', default_value=TextSubstitution(text='zed_node')),
        
        # Load SVO file
        DeclareLaunchArgument('svo_file', default_value=TextSubstitution(text='')),
        DeclareLaunchArgument('stream', default_value=TextSubstitution(text='')), # DeclareLaunchArgument('stream', default_value=TextSubstitution(text='<ip_address>:<port>')),
        
        # Base frame
        DeclareLaunchArgument('base_frame', default_value=TextSubstitution(text='base_link')),
        DeclareLaunchArgument('publish_urdf', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('camera_id', default_value=TextSubstitution(text='0')),
        DeclareLaunchArgument('gpu_id', default_value=TextSubstitution(text='-1')),
        
        # Position respect to base frame (i.e. 'base_link)
        DeclareLaunchArgument('cam_pos_x', default_value=TextSubstitution(text='0.0')),
        DeclareLaunchArgument('cam_pos_y', default_value=TextSubstitution(text='0.0')),
        DeclareLaunchArgument('cam_pos_z', default_value=TextSubstitution(text='0.0')),
        
        # Orientation respect to base frame (i.e. 'base_link)
        DeclareLaunchArgument('cam_roll', default_value=TextSubstitution(text='0.0')),
        DeclareLaunchArgument('cam_pitch', default_value=TextSubstitution(text='0.0')),
        DeclareLaunchArgument('cam_yaw', default_value=TextSubstitution(text='0.0')),
        
        Node(
            package='zed_wrapper',
            executable='zed_wrapper_node',
            name=LaunchConfiguration('node_name'),
            parameters=[
                path.join(
                    get_package_share_directory('zed_wrapper'),
                    'params',
                    'common.yaml',
                ),
                path.join(
                    get_package_share_directory('zed_wrapper'),
                    'params',
                    f'{LaunchConfiguration("camera_model")}.yaml',
                ),

                {
                    # Camera name
                    'general/camera_name': LaunchConfiguration('camera_name'),

                    # Base frame
                    'general/base_frame': LaunchConfiguration('base_frame'),

                    # SVO file path
                    'svo_file': LaunchConfiguration('svo_file'),

                    # Remote stream
                    'stream': LaunchConfiguration('stream'),

                    # Camera ID
                    'general/zed_id': LaunchConfiguration('camera_id'),

                    # GPU ID
                    'general/gpu_id': LaunchConfiguration('gpu_id'),

                    # Disable TF publishing
                    'pos_tracking/publish_tf': 'false',
                    'pos_tracking/publish_map_tf': 'false',
                }
            ],
        ),
    ])
