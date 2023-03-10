#!/usr/bin/python3
# Copyright 2020, Steve Macenski
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import GroupAction, IncludeLaunchDescription
from launch_ros.actions import SetRemap
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import PushRosNamespace

import os

def generate_launch_description():
    share_dir = get_package_share_directory('nissan_bringup')
    parameter_file = LaunchConfiguration('params_file')
    node_id = 'os_left'
    
    params_declare = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(
            share_dir, 'config', 'ouster_left_config.yaml'
        ),
        description='FPath to the ROS2 parameters file to use.'
    )


    # launch os
    os_include = GroupAction(
        actions=[
            SetRemap(src='/points',dst=node_id + '/points'),

            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(share_dir + '/launch/sensory/ouster_driver.launch.py'),
                launch_arguments = {   
                    'parameters' : [parameter_file]
                }.items(),
            )
        ]
    )

    return LaunchDescription([
        GroupAction(
            actions=[
                PushRosNamespace('os_left'),

                params_declare,
                os_include,
            ]
        )
    ])