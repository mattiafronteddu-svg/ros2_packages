import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument
from launch_ros.parameter_descriptions import ParameterValue
import xacro

def generate_launch_description():

    pkg_share = get_package_share_directory('dh_er_4ia')

    xacro_file = os.path.join(pkg_share, 'urdf', 'fanuc_er_4ia.urdf.xacro')
    
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    params = {'use_sim_time': True, 'robot_description':doc.toxml()}


    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    rviz_config = os.path.join(
        pkg_share,
        'rviz',
        'config.rviz'
    )

    rviz_node = Node(
        package='rviz2',
            executable='rviz2',
            name='rviz',
            arguments=['-d', rviz_config],
            output='screen'
    )

    jsp_node= Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        )

    return LaunchDescription([
        robot_state_publisher_node,
        jsp_node,
        rviz_node
    ])