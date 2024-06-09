### Run below command in terminal to create ROS2 WORKSPACE
./create_ros2_workpace.sh 

### Run below command in terminal to create new rclpy pkg
./create_rclpy_pkg.sh

### Build ROS2 pkg and Run below 3 conmmands in different terminal
- ros2 run marker_display pub
- ros2 run marker_display sub
- ros2 run rviz2 rviz2 (make sure to select topic from topic window in rviz)

### About marker_display pkg
1. Config folder inside marker_display contain path.xml --> Path/Edges data
2. Inside marker_display there are two files
    - pathpoint_publisher.py for data extraction forn path.xml file and send data over /data_topic.
    - pathpoint_subscriber.py for receive data from /data_topic and publish to over /marker_topic as marker msg so that rviz2 read that topic and display in rviz2.







