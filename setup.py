from setuptools import setup

package_name = 'ai_robot_navigator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shreyas',
    maintainer_email='user@todo.com',
    description='AI Robot Navigator',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'navigator = ai_robot_navigator.navigator:main',
        ],
    },
)