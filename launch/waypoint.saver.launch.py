from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition

# 'roslaunch', 'waypoint_maker', 'waypoint_saver.launch', 'save_finename:=/mnt/storage_1tb/waypoint/del1.csv', 'input_type:=0', 'save_velocity:=True', 'interval:=1', 'lane_topic:=/lane_waypoints_array'

def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('input_type', default_value=TextSubstitution(text='0')),
        # DeclareLaunchArgument('save_finename', default_value=TextSubstitution(text='/tmp/saved_waypoints.csv')),
        DeclareLaunchArgument('interval', default_value=TextSubstitution(text='1')),
        DeclareLaunchArgument('pose_topic', default_value=TextSubstitution(text='current_pose')),
        DeclareLaunchArgument('velocity_topic', default_value=TextSubstitution(text='current_velocity')),
        DeclareLaunchArgument('save_velocity', default_value=TextSubstitution(text='true')),
        DeclareLaunchArgument('lane_topic', default_value=TextSubstitution(text='/lane_waypoints_array')),
        
        Node(
            package='waypoint_maker',
            executable='waypoint_saver',
            name='waypoint_saver',
            output='screen',
            condition=UnlessCondition(LaunchConfiguration('input_type')),

            parameters=[
                {
                    'interval': LaunchConfiguration('interval'),
                    'velocity_topic': LaunchConfiguration('velocity_topic'),
                    'pose_topic': LaunchConfiguration('pose_topic'),
                    'save_velocity': LaunchConfiguration('save_velocity'),
                }
        ]),
        Node(
            package='waypoint_maker',
            executable='waypoint_extractor',
            name='waypoint_extractor',
            output='screen',
            condition=IfCondition(LaunchConfiguration('input_type')),

            parameters=[
                {
                    # 'lane_csv': LaunchConfiguration('save_finename'),
                    'lane_topic': LaunchConfiguration('lane_topic'),
                }
        ]),
        
    ])
