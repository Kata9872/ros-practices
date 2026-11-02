
from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'course_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kata',
    maintainer_email='kata@example.com',
    description='PR05 launch and QoS demonstration',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'pose_relay = course_bringup.pose_relay:main',
            'sensor_subscriber = course_bringup.sensor_subscriber:main',
        ],
    },
)
