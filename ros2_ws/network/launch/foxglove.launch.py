from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    # Launch Foxglove Studio to monitor data
    return LaunchDescription(
        ExecuteProcess(
            cmd=["ros2", "launch", "foxglove_bridge", "foxglove_bridge_launch.xml"]
        )
    )
