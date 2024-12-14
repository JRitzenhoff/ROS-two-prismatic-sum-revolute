FROM ros:humble

RUN apt update && apt install -y \
    sudo \
    ros-humble-foxglove-bridge \
    ros-humble-robot-state-publisher \
    ros-humble-joint-state-publisher

# Create the user
ARG USERNAME=vscode
ARG USER_UID=1001
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER ${USERNAME}:${USERNAME}

SHELL ["/bin/bash", "-c"]

RUN touch ~/.bashrc \
    && echo ". /opt/ros/humble/setup.bash" >> ~/.bashrc

WORKDIR /workspaces/visualizer/ros2_ws