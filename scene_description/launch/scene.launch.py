from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # UR args
    ur_type = LaunchConfiguration("ur_type")
    name = LaunchConfiguration("name")
    tf_prefix = LaunchConfiguration("tf_prefix")

    # Pose args
    robot_x = LaunchConfiguration("robot_x")
    robot_y = LaunchConfiguration("robot_y")
    robot_z = LaunchConfiguration("robot_z")
    robot_roll = LaunchConfiguration("robot_roll")
    robot_pitch = LaunchConfiguration("robot_pitch")
    robot_yaw = LaunchConfiguration("robot_yaw")

    table_x = LaunchConfiguration("table_x")
    table_y = LaunchConfiguration("table_y")
    table_z = LaunchConfiguration("table_z")
    table_roll = LaunchConfiguration("table_roll")
    table_pitch = LaunchConfiguration("table_pitch")
    table_yaw = LaunchConfiguration("table_yaw")

    use_gui = LaunchConfiguration("use_gui")

    # RViz config
    rviz_config = LaunchConfiguration("rviz_config")

    scene_xacro = PathJoinSubstitution([
        FindPackageShare("scene_description"),
        "urdf",
        "scene_desc.xacro"
    ])

    robot_description = Command([
        "xacro ",
        scene_xacro,

        " ur_type:=", ur_type,
        " name:=", name,
        " tf_prefix:=", tf_prefix,

        " robot_x:=", robot_x,
        " robot_y:=", robot_y,
        " robot_z:=", robot_z,
        " robot_roll:=", robot_roll,
        " robot_pitch:=", robot_pitch,
        " robot_yaw:=", robot_yaw,

        " table_x:=", table_x,
        " table_y:=", table_y,
        " table_z:=", table_z,
        " table_roll:=", table_roll,
        " table_pitch:=", table_pitch,
        " table_yaw:=", table_yaw,
    ])

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
        parameters=[{"robot_description": robot_description}],
    )

    jsp = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        output="screen",
        condition=UnlessCondition(use_gui),
        parameters=[{"robot_description": robot_description}],
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
    )

    default_rviz_config = PathJoinSubstitution([
        FindPackageShare("scene_description"),
        "rviz",
        "config.rviz"
    ])

    return LaunchDescription([
        # UR
        DeclareLaunchArgument("ur_type", default_value="ur10"),
        DeclareLaunchArgument("name", default_value="ur10"),
        DeclareLaunchArgument("tf_prefix", default_value=""),

        # Robot pose
        DeclareLaunchArgument("robot_x", default_value="0.0"),
        DeclareLaunchArgument("robot_y", default_value="0.0"),
        DeclareLaunchArgument("robot_z", default_value="0.775"),
        DeclareLaunchArgument("robot_roll", default_value="0.0"),
        DeclareLaunchArgument("robot_pitch", default_value="0.0"),
        DeclareLaunchArgument("robot_yaw", default_value="0.0"),

        # Table pose
        DeclareLaunchArgument("table_x", default_value="0.0"),
        DeclareLaunchArgument("table_y", default_value="0.0"),
        DeclareLaunchArgument("table_z", default_value="0.75"),
        DeclareLaunchArgument("table_roll", default_value="0.0"),
        DeclareLaunchArgument("table_pitch", default_value="0.0"),
        DeclareLaunchArgument("table_yaw", default_value="0.0"),

        # GUI + RViz config
        DeclareLaunchArgument("use_gui", default_value="true"),
        DeclareLaunchArgument("rviz_config", default_value=default_rviz_config),

        rsp,
        jsp_gui,
        jsp,
        rviz,
    ])