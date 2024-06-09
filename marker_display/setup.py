import os
from glob import glob
from setuptools import setup

package_name = 'marker_display'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append((os.path.join('share', package_name, 'config'), glob('config/*.xml')))


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bhavesh',
    maintainer_email='bhaveshvagadiya1990@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = marker_display.pathpoint_publisher:main',
            'sub = marker_display.pathpoint_subscriber:main',            
        ],
    },
)
