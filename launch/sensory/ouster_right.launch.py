# Copyright 2023 Ouster, Inc.

"""Launch a sensor node along with os_cloud and os_"""

from pathlib import Path
import launch
import lifecycle_msgs.msg
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node, LifecycleNode
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            RegisterEventHandler, EmitEvent, LogInfo)
from launch.substitutions import LaunchConfiguration
from launch.events import matches_action
from launch_ros.events.lifecycle import ChangeState
from launch_ros.event_handlers import OnStateTransition
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
    """
    Generate launch description for running ouster_ros components separately each
    component will run in a separate process).
    """
    nissan_bringup_pkg_dir = get_package_share_directory('nissan_bringup')
    default_params_file = \
        Path(nissan_bringup_pkg_dir) / 'config' / 'ouster_config.yaml'
    params_file = LaunchConfiguration('params_file')
    params_file_arg = DeclareLaunchArgument('params_file',
                                            default_value=str(
                                                default_params_file),
                                            description='name or path to the parameters file to use.')

    os_driver = LifecycleNode(
        package='ouster_ros',
        executable='os_driver',
        name="os_driver",
        namespace="",
        parameters=[params_file],
        output='screen',
    )

    sensor_configure_event = EmitEvent(
        event=ChangeState(
            lifecycle_node_matcher=matches_action(os_driver),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_CONFIGURE,
        )
    )

    sensor_activate_event = RegisterEventHandler(
        OnStateTransition(
            target_lifecycle_node=os_driver, goal_state='inactive',
            entities=[
                LogInfo(msg="os_driver (os_right) activating..."),
                EmitEvent(event=ChangeState(
                    lifecycle_node_matcher=matches_action(os_driver),
                    transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVATE,
                )),
            ],
            handle_once=True
        )
    )

    # TODO: figure out why registering for on_shutdown event causes an exception
    # and error handling
    # shutdown_event = RegisterEventHandler(
    #     OnShutdown(
    #         on_shutdown=[
    #             EmitEvent(event=ChangeState(
    #               lifecycle_node_matcher=matches_node_name(node_name=F"/ouster/os_sensor"),
    #               transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVE_SHUTDOWN,
    #             )),
    #             LogInfo(msg="os_sensor node exiting..."),
    #         ],
    #     )
    # )

    return launch.LaunchDescription([
        GroupAction(
            actions=[
                PushRosNamespace('os_right'),

                params_file_arg,
                os_driver,
                sensor_configure_event,
                sensor_activate_event,
                # shutdown_event
            ]
        )
    ])
