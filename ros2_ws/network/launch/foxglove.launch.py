from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    # Launch Foxglove Studio to visualize URDF data
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PathJoinSubstitution(
                    [
                        FindPackageShare("foxglove_bridge"),
                        "launch",
                        "foxglove_bridge_launch.xml",
                    ]
                )
            ),
        ]
    )
