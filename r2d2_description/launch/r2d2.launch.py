from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_name = 'r2d2_description'
    pkg_path = get_package_share_directory(pkg_name)

    # urdf_file = os.path.join(pkg_path, 'urdf', 'r2d2.urdf')
    xacro_file = os.path.join(pkg_path, 'urdf', 'r2d2.xacro')
    rviz_config = os.path.join(pkg_path, 'rviz', 'config.rviz')

    robot_description = ParameterValue(
        #Command(['cat ', urdf_file]),
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])
