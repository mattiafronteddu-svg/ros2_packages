import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('fanuc_cr_35ib')

    urdf_file = os.path.join(
        pkg_share,
        'urdf',
        'fanuc_cr_35ib.urdf'
    )

    rviz_config = os.path.join(
        get_package_share_directory('fanuc_cr_35ib'),
        'rviz',
        'config.rviz'
    )

    with open(urdf_file, 'r') as file:
        robot_description = file.read()
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': False
            }]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

         Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])