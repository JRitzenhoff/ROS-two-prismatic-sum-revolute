import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import LogInfo

def generate_launch_description():
    urdf_path = LaunchConfiguration('urdf_path', default='/workspaces/urdf-testing/ros2_ws/robot.urdf')

    return LaunchDescription([
        DeclareLaunchArgument('urdf_path', description='Path to the URDF file'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', urdf_path])}],
            output='screen',
        ),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        ),
    ])
