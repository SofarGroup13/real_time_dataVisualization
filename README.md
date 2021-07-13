# DatasetVisualization
This architecture will allow user to visualize the content of Dataset created by our team members.
Here, we are using GUI to visulaize the data. Gui has three sub graphs to visualize the imu,mocap and point cloud data using CSV files.
But, for instance, we have worked on IMU sensor data to visualize.

# Authors 
* Polaka Surendra : s4846909@studenti.unige.it
* Chetan Chand Chilakapati   : s4850111@studenti.unige.it

# Architecture of the System

Datavisualization GUI is the overall graphical part of the visualization system where user can examine Ros bags i-e The already built dataset of three sensors (Kinect, SmartWatch, Motion Capture Sensor MOCAP) with their respective datatypes (PointCloud2, IMU, Float32). The GUI enable the user regarding the managing the configuration of csv files, let the user to keep the track of time through a timer and the executed percentage of the csv files via Progressbar. The progress bar contains scatter,Browse Button  which enables the User to connect GUI with the loaded  files.  GUI consist of three borwising options for the respective sensors, which allows the user to navigates through the system to a folder that contains the required bag files. Upon selecting, the path address will be displayed for an added certainty. Also, to make the process simpler, we also added two extra buttons, one for brwosing and other for running. So, in this case, user need not access to each file. He can simply to click on "Add" icon and opens the file and then by clicking "play" button the data visualizes. Alos, Below each of the display window there is STOP button, and an exit button to end the GUI.


![image](https://user-images.githubusercontent.com/62186578/125333672-ceb53800-e34a-11eb-9af9-1827498895db.png)

# Contents of the repository
In this section we will explain the repository's content

# Documentation

This directory contains the doxygen documentation in "html" and "latex" format. For a clear and better idea of the project script and its detailed explanation, go to
```
Documentation/html/index.html

```

# Src
This folder contains a python script for the initialization of the MainwWindow. It also contains a file by the name of "gui.ui" which is GUI created in Qt designer. For execution of the python script, both the python script and Qt designer file should be in the same directory.


# Installation

The first thing to do, after having cloned the repository in the Ros workspace, is to build the package and install in order to make the files executable, using the following commands in the workspace:

```
catkin_make
catkin_make install
```

Execute the following commands for Ros related Python libraries

```
sudo apt-update
sudo apt install python3-pip
sudo apt-get install python3-yaml	
sudo pip3 install rospkg catkin-pkg 
pip3 install --user pyqt5
sudo apt-get install python3-pyqt5
```

To run the system:

```
python3 gui.py
```
This individual python script can also be run from and python Integrated Development Enviroment (IDE) but make sure to have project enviroment built accordingly with the required libraries installed i-e python and PyQt5 libraries

# Video Tutorial

A video showing how our gui works can be found at the following link.
[video](https://github.com/SofarGroup13/dataset_visualization/blob/master/video.mp4)



# Report

Detailed decription of the module can be found in the following report shared on a Google Drive.
[Report](https://github.com/SofarGroup13/dataset_visualization/blob/master/video.mp4)
