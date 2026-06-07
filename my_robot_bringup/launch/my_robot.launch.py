from launch import LaunchDescription
from launch_ros.actions import Node
import xacro
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    my_robot_controller_path = os.path.join(get_package_share_directory('my_robot_bringup'),
                                'config', 'my_robot_controllers.yaml')
    
    robot_description_path = os.path.join(get_package_share_directory('my_robot_description'), 
                                'mjcf', 'my_robot.urdf.xacro')
    
    robot_description = {'robot_description': xacro.process_file(robot_description_path).toxml()}

    mujoco_simulator_node = Node(
        package='mujoco_ros2_control',
        executable='ros2_control_node',
        output='screen',
        parameters=[
            robot_description,
            my_robot_controller_path
        ]   
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    joint_state_broadcaster_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments=['joint_state_broadcaster']
    )

    bicycle_steering_controller_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments=['bicycle_steering_controller']
    )

    return LaunchDescription([
        mujoco_simulator_node,
        robot_state_publisher_node,
        joint_state_broadcaster_node,
        bicycle_steering_controller_node
    ])