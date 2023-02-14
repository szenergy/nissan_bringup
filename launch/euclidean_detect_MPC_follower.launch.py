from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('points_node', default_value=TextSubstitution(text='/points_no_ground')), # CHANGE THIS TO READ WHETHER FROM VSCAN OR POINTS_RAW
        DeclareLaunchArgument('remove_ground', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('downsample_cloud', default_value=TextSubstitution(text='false')), # Apply VoxelGrid Filter with the value given by 'leaf_size'
        DeclareLaunchArgument('leaf_size', default_value=TextSubstitution(text='0.12')), # Voxel Grid Filter leaf size
        DeclareLaunchArgument('cluster_size_min', default_value=TextSubstitution(text='5')), # Minimum number of points to consider a cluster as valid
        DeclareLaunchArgument('cluster_size_max', default_value=TextSubstitution(text='800')), # Maximum number of points to allow inside a cluster
        DeclareLaunchArgument('sync', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('use_diffnormals', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('pose_estimation', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('clip_min_height', default_value=TextSubstitution(text='-1.3')),
        DeclareLaunchArgument('clip_max_height', default_value=TextSubstitution(text='0.5')),

        DeclareLaunchArgument('keep_lanes', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('keep_lane_left_distance', default_value=TextSubstitution(text='5')),
        DeclareLaunchArgument('keep_lane_right_distance', default_value=TextSubstitution(text='5')),
        DeclareLaunchArgument('cluster_merge_threshold', default_value=TextSubstitution(text='1.5')),
        DeclareLaunchArgument('clustering_distance', default_value=TextSubstitution(text='0.85')),

        DeclareLaunchArgument('use_vector_map', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('wayarea_gridmap_layer', default_value=TextSubstitution(text='wayarea')),

        DeclareLaunchArgument('output_frame', default_value=TextSubstitution(text='left_os1/os1_sensor')),

        DeclareLaunchArgument('remove_points_upto', default_value=TextSubstitution(text='0.0')),

        DeclareLaunchArgument('use_gpu', default_value=TextSubstitution(text='true')),

        DeclareLaunchArgument('use_multiple_thres', default_value=TextSubstitution(text='false')),
        DeclareLaunchArgument('clustering_ranges', default_value=TextSubstitution(text='[15,30,45,60]')), # Distances to segment pointcloud
        DeclareLaunchArgument('clustering_distances', default_value=TextSubstitution(text='[0.5,1.1,1.6,2.1,2.6]')), # Euclidean Clustering threshold distance for each segment
        
        Node(
            package='lidar_euclidean_cluster_detect',
            executable='lidar_euclidean_cluster_detect',
            name='lidar_euclidean_cluster_detect',
            output='screen',
            parameters=[
                {
                    'points_node': LaunchConfiguration('points_node'), # Can be used to select which pointcloud node will be used as input for the clustering
                    'remove_ground': LaunchConfiguration('remove_ground'),
                    'downsample_cloud': LaunchConfiguration('downsample_cloud'),
                    'leaf_size': LaunchConfiguration('leaf_size'),
                    'cluster_size_min': LaunchConfiguration('cluster_size_min'),
                    'cluster_size_max': LaunchConfiguration('cluster_size_max'),
                    'use_diffnormals': LaunchConfiguration('use_diffnormals'),
                    'pose_estimation': LaunchConfiguration('pose_estimation'),
                    'keep_lanes': LaunchConfiguration('keep_lanes'),
                    'keep_lane_left_distance': LaunchConfiguration('keep_lane_left_distance'),
                    'keep_lane_right_distance': LaunchConfiguration('keep_lane_right_distance'),
                    'clip_min_height': LaunchConfiguration('clip_min_height'),
                    'clip_max_height': LaunchConfiguration('clip_max_height'),
                    'output_frame': LaunchConfiguration('output_frame'),
                    'remove_points_upto': LaunchConfiguration('remove_points_upto'),
                    'clustering_distance': LaunchConfiguration('clustering_distance'),
                    'cluster_merge_threshold': LaunchConfiguration('cluster_merge_threshold'),
                    'use_gpu': LaunchConfiguration('use_gpu'),
                    'use_multiple_thres': LaunchConfiguration('use_multiple_thres'),
                    'clustering_ranges': LaunchConfiguration('clustering_ranges'), # Distances to segment pointcloud
                    'clustering_distances': LaunchConfiguration('clustering_distances'), # Euclidean Clustering threshold distance for each segment
                }
            ],
        ),
        Node(
            package='roi_object_filter',
            namespace='/detection/lidar_detector',
            executable='roi_object_filter',
            name='object_roi_filter_clustering',
            output='screen',
            condition=IfCondition(LaunchConfiguration('use_vector_map')),

            parameters=[
                {
                    'objects_src_topic': '/objects',
                    'wayarea_gridmap_layer': LaunchConfiguration('wayarea_gridmap_layer'),
                    'sync_topics': 'false',
                    'exception_list': '[person, bicycle]',
                }
            ],
        ),
        Node(
            package='detected_objects_visualizer',
            namespace='/detection/lidar_detector',
            executable='visualize_detected_objects',
            name='cluster_detect_visualization_01',
            output='screen',
            condition=UnlessCondition(LaunchConfiguration('use_vector_map')),

            parameters=[
                {
                    'objects_src_topic': '/objects',
                }
            ],
        ),

        # MPC
        Node(
            package='mpc_follower',
            executable='mpc_waypoints_converter',
            name='mpc_waypoints_converter',
            output='screen',
        ),
        Node(
            package='mpc_follower',
            executable='mpc_follower',
            name='mpc_follower',
            output='screen',
            parameters=[
                {
                    "ctrl_cmd_interface": "all",
                    "in_waypoints_name": "/mpc_waypoints",
                    "in_vehicle_status_name": "/vehicle_status",
                    "in_selfpose_name": "/current_pose",
                    "out_twist_name": "/twist_raw",
                    "out_vehicle_cmd_name": "/ctrl_raw",

                    # parameters
                    "ctrl_period": "0.03",
                    "traj_resample_dist": "0.1",
                    "admisible_position_error": "5",
                    "admisible_yaw_error_deg": "90",
                    "path_smoothing_times": "1",
                    "show_debug_info": "false",
                    "enable_yaw_recalculation": "true",
                    "enable_path_smoothing": "true",
                    "path_filter_moving_ave_num": "35",
                    "curvature_smoothing_num": "35",
                    "steering_lpf_cutoff_hz": "3",
                    "qp_solver_type": "unconstraint_fast",
                    "qpoases_max_iter": "500",
                    "vehicle_model_type": "kinematics_no_delay",
                    "mpc_prediction_horizon": "70",
                    "mpc_prediction_sampling_time": "0.1",
                    "mpc_weight_lat_error": "5",
                    "mpc_weight_heading_error": "0",
                    "mpc_weight_heading_error_squared_vel_coeff": "5",
                    "mpc_weight_steering_input": "1",
                    "mpc_weight_steering_input_squared_vel_coeff": "2.5",
                    "mpc_weight_lat_jerk": "0",
                    "mpc_weight_terminal_lat_error": "0",
                    "mpc_weight_terminal_heading_error": "0",
                    "mpc_zero_ff_steer_deg": "2",
                    "delay_compensation_time": "0.1",
                    "vehicle_model_steer_tau": "0.001",
                    "vehicle_model_wheelbase": "2.7",
                    "steer_lim_deg": " 32",
                    "steering_gear_ratio": "20",
                }
            ],
        ),

    ])
