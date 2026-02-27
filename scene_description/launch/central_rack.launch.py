from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import FindExecutable


def generate_launch_description():
    # Launch args
    use_gui = LaunchConfiguration("use_gui")
    rviz_config = LaunchConfiguration("rviz_config")

    # Paths
    scene_xacro = PathJoinSubstitution([
        FindPackageShare("scene_description"),
        "urdf",
        "central_rack_tools.xacro"
    ])

    default_rviz_config = PathJoinSubstitution([
        FindPackageShare("scene_description"),
        "rviz",
        "config.rviz"
    ])

    # robot_description da xacro
    robot_description = Command([
        FindExecutable(name="xacro"),
        " ",
        scene_xacro,
    ])

    # Nodes
    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )

    # Uno SOLO tra GUI e non-GUI (mai entrambi)
    jsp_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen",
        condition=IfCondition(use_gui),
    )

    jsp = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        output="screen",
        condition=UnlessCondition(use_gui),
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
    )

    return LaunchDescription([
        DeclareLaunchArgument("use_gui", default_value="true"),
        DeclareLaunchArgument("rviz_config", default_value=default_rviz_config),

        rsp,
        jsp_gui,
        jsp,
        rviz,
    ])