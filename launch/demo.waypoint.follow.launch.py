from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Load waypoints csv and necessary publish topics fro MPC waypoint converter
        Node(
            package='nissan_bringup',
            executable='bare_planner.py',
            name='bare_planner_py',
        ),
        Node(
            package='nissan_bringup',
            executable='global_waypoint_monitor.py',
            name='waypoint_loader_py',
        ),
        Node(
            package='nissan_bringup',
            executable='waypoint_loader.py',
            name='global_waypoint_monitor_py',
            output='screen',
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
                    'ctrl_cmd_interface': 'all',
                    'in_waypoints_name': '/mpc_waypoints',
                    'in_vehicle_status_name': '/vehicle_status',
                    'in_selfpose_name': '/current_pose',
                    'out_twist_name': '/twist_raw',
                    'out_vehicle_cmd_name': '/ctrl_raw',

                    # parameters
                    'ctrl_period': '0.03',
                    'traj_resample_dist': '0.1',
                    'admisible_position_error': '5',
                    'admisible_yaw_error_deg': '90',
                    'path_smoothing_times': '1',
                    'show_debug_info': 'false',
                    'enable_yaw_recalculation': 'true',
                    'enable_path_smoothing': 'true',
                    'path_filter_moving_ave_num': '35',
                    'curvature_smoothing_num': '35',
                    'steering_lpf_cutoff_hz': '3',
                    'qp_solver_type': 'unconstraint_fast',
                    'qpoases_max_iter': '500',
                    'vehicle_model_type': 'kinematics_no_delay',
                    'mpc_prediction_horizon': '70',
                    'mpc_prediction_sampling_time': '0.1',
                    'mpc_weight_lat_error': '5',
                    'mpc_weight_heading_error': '0',
                    'mpc_weight_heading_error_squared_vel_coeff': '5',
                    'mpc_weight_steering_input': '1',
                    'mpc_weight_steering_input_squared_vel_coeff': '2.5',
                    'mpc_weight_lat_jerk': '0',
                    'mpc_weight_terminal_lat_error': '0',
                    'mpc_weight_terminal_heading_error': '0',
                    'mpc_zero_ff_steer_deg': '2',
                    'delay_compensation_time': '0.1',
                    'vehicle_model_steer_tau': '0.001',
                    'vehicle_model_wheelbase': '2.7',
                    'steer_lim_deg': ' 32',
                    'steering_gear_ratio': '20',
                }
            ],
        ),
    ])
