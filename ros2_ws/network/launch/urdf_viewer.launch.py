from pathlib import Path

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    workspace_path = Path("/workspaces") / "urdf-testing" / "ros2_ws"
    urdf_directory = workspace_path / "network" / "urdf"
    urdf_path = urdf_directory / "robot.urdf"

    with open(urdf_path) as urdf_file_handle:
        urdf_contents = urdf_file_handle.read()

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[{"robot_description": urdf_contents}],
                output="screen",
            ),
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
                parameters=[{"source_list": ["/faked_joints"]}],
                output="screen",
            ),
        ]
    )
