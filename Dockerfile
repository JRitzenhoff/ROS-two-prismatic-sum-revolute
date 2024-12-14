FROM ros:humble

RUN apt update && apt install -y \
    ros-humble-rviz2 \
    sudo

# Create the user
ARG USERNAME=vscode
ARG USER_UID=1001
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER ${USERNAME}:${USERNAME}

WORKDIR /workspaces/visualizer

CMD ["./ros_entrypoint.sh"]