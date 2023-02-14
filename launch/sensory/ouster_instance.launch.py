from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('sensor_hostname', default_value=TextSubstitution(text=''), description='hostname or IP in dotted decimal form of the sensor'),
        DeclareLaunchArgument('udp_dest', default_value=TextSubstitution(text='192.168.1.5'), description='hostname or IP where the sensor will send data packets'),
        DeclareLaunchArgument('lidar_port', default_value=TextSubstitution(text=''), description='port to which the sensor should send lidar data'),
        DeclareLaunchArgument('imu_port', default_value=TextSubstitution(text=''), description='port to which the sensor should send imu data'),
        DeclareLaunchArgument('replay', default_value=TextSubstitution(text='false'), description='do not connect to a sensor; expect /os_node/{lidar,imu}_packets from replay'),
        DeclareLaunchArgument('lidar_mode', default_value=TextSubstitution(text='512x20'), description='resolution and rate: either 512x10, 512x20, 1024x10, 1024x20, or 2048x10'),
        DeclareLaunchArgument('timestamp_mode', default_value=TextSubstitution(text=''), description='method used to timestamp measurements: TIME_FROM_INTERNAL_OSC, TIME_FROM_SYNC_PULSE_IN, TIME_FROM_PTP_1588'),
        DeclareLaunchArgument('metadata', default_value=TextSubstitution(text=''), description='override default metadata file for replays'),
        DeclareLaunchArgument('viz', default_value=TextSubstitution(text='false'), description='whether to run a simple visualizer'),
        DeclareLaunchArgument('image', default_value=TextSubstitution(text='false'), description='publish range/intensity/noise image topic'),
        DeclareLaunchArgument('tf_prefix', default_value=TextSubstitution(text=''), description='namespace for tf transforms'),
        DeclareLaunchArgument('publish_transforms', default_value=TextSubstitution(text='false'), description='publish (broadcast) transforms tf'),
        
        Node(
            package='ouster_ros',
            executable='os_node',
            output='screen',
            parameters=[
                {
                    '~/lidar_mode': LaunchConfiguration('lidar_mode'),
                    '~/timestamp_mode': LaunchConfiguration('timestamp_mode'),
                    '~/replay': LaunchConfiguration('replay'),
                    '~/sensor_hostname': LaunchConfiguration('sensor_hostname'),
                    '~/udp_dest': LaunchConfiguration('udp_dest'),
                    '~/lidar_port': LaunchConfiguration('lidar_port'),
                    '~/imu_port': LaunchConfiguration('imu_port'),
                    '~/metadata': LaunchConfiguration('metadata'),
                }
            ]
        ),
        Node(
            package='ouster_ros',
            executable='os_cloud_node',
            name='os1_cloud_node',
            output='screen',
            parameters=[
                {
                    '~/tf_prefix': LaunchConfiguration('tf_prefix')
                }
            ],
            remappings=[
                ('~/os_config', 'os_node/os_config'),
                ('~/lidar_packets', 'os_node/lidar_packets'),
                ('~/imu_packets', 'os_node/imu_packets'),
                ('~/lidar_packets', 'os_node/lidar_packets'),
            ],
        ),
        Node(
            package='ouster_ros',
            executable='viz_node',
            name='viz_node',
            output='screen',
            remappings=[
                ('~/os_config', 'os_node/os_config'),
                ('~/points', 'os_cloud_node/points'),
            ],
            condition=IfCondition(LaunchConfiguration('viz'))
        ),
        Node(
            package='ouster_ros',
            executable='img_node',
            name='img_node',
            output='screen',
            remappings=[
                ('~/os1_config', '/os1_node/os1_config'),
                ('~/points', 'os1_cloud_node/points'),
            ],
            condition=IfCondition(LaunchConfiguration('image'))
        ),
        
    ])
