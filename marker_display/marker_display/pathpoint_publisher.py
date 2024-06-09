import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from rclpy.qos import QoSProfile, DurabilityPolicy
import xml.etree.ElementTree as ET

import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

class DataPublisher(Node):
    def __init__(self):
        super().__init__('data_publisher')
        qos_profile = QoSProfile(
            depth=10,  # Maximum number of messages that can be queued if subscribers are not receiving them fast enough
            durability=DurabilityPolicy.TRANSIENT_LOCAL  # Messages are persisted locally until all subscribers have received them
        )
        self.publisher_ = self.create_publisher(Float32MultiArray, 'data_topic', qos_profile)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_data)
        package_name = 'marker_display'
        file_name = 'path.xml'
        # Get the absolute path to the 'data' directory within the package
        package_share_directory = get_package_share_directory(package_name)
         # Construct the absolute path to the XML file
        file_path = os.path.join(package_share_directory, 'config', file_name)
        self.data_file = file_path  # Change this to your XML file path

    def publish_data(self):
        data = self.extract_coordinates(self.data_file)
        msg = Float32MultiArray()
        for points in data:
            for x, y in points:
                msg.data.append(x)
                msg.data.append(y)
        self.publisher_.publish(msg)

    def extract_coordinates(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data = []

        for edge in root.findall('edge'):
            points = []
            for ep in edge.findall('./points/ep'):
                x = float(ep.find('x').text)
                y = float(ep.find('y').text)
                points.append((x, y))
            data.append(points)

        return data

def main(args=None):
    rclpy.init(args=args)
    data_publisher = DataPublisher()
    rclpy.spin(data_publisher)
    data_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
