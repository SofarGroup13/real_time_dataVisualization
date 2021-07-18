# DatasetVisualization
This architecture will allow the user to visualize the content of the Dataset created by our team members.
Here, we are using GUI to visualize the data. Gui has three subgraphs to visualize the imu, mocap, and point cloud data using CSV files.
But, for instance, we have worked on IMU sensor data to visualize.

# Authors 
* Polaka Surendra : s4846909@studenti.unige.it
* Chetan Chand Chilakapati   : s4850111@studenti.unige.it

# Architecture of the System

Data visualization GUI is the overall graphical part of the visualization system where users can examine i-e The already built dataset of three sensors (Kinect, SmartWatch, Motion Capture Sensor MOCAP) with their respective datatypes (PointCloud2, IMU, Float32). The GUI enables the user to manage the configuration of CSV files, lets the user keep the track of time through a timer and the executed percentage of the CSV files via Progressbar. The progress bar contains scatter, Browse Button which enables the User to connect GUI with the loaded files.  GUI consists of three browsing options for the respective sensors, which allows the user to navigates through the system to a folder that contains the required bag files. Upon selecting, the path address will be displayed for an added certainty. To make the process simpler, we added two extra buttons, one for browsing and the other for running. So, in this case, the user need not access each file. He can simply click on the "Add" icon and opens the file and then by clicking the "play" button the data visualize. Also, Below each of the display windows, there is a STOP button, and an exit button to end the GUI.


![image](https://user-images.githubusercontent.com/62186578/125333672-ceb53800-e34a-11eb-9af9-1827498895db.png)

# Documentation

This directory contains the Doxygen documentation in "HTML" and "latex" format. For a clear and better idea of the project script and its detailed explanation, go to
```
documentation/html/index.html

```
# GUI pictures
This folder contains images of our old and modified GUI. Also, the images of the timeline and visualizing in the GUI.

A video visulaizing the IMU data is named as visualizing _video.

# GUI_Old
This is the code developed by my one of our batchmate. This folder contains a python script for the initialization of the MainwWindow. It also contains a file by the name of "gui.ui" which is GUI created in Qt Designer. But, only GUI has been designed in this. For the execution of the python script, both the python script and Qt designer file should be in the same directory. 

# GUI_updated
This is the updated version of the previous folder. This folder contains a python script for the initialization of the MainwWindow. It also contains a file by the name of "updated_gui.ui" which is a GUI created in Qt Designer. But, in this only GUI has been designed. For the execution of the python script, both the python script and Qt designer file should be in the same directory. The python script updated_gui.py has been modified to visualize the CSV files using gui.py(previous folder). The files like, imu.csv are the CSV data, and some other images which is part of the code.

# Installation


The first thing to do, after having cloned the repository :

Execute the following commands for Python libraries

```
sudo apt-update
sudo apt install python3-pip
sudo apt-get install python3-yaml	
pip3 install --user pyqt5
sudo apt-get install python3-pyqt5
```

To run the system:

```
python3 updated_gui.py
```
This individual python script can also be run from and python Integrated Development Environment (IDE) but make sure to have the project environment built accordingly with the required libraries installed i-e python and PyQt5 libraries

# Video Tutorial

A video showing how our GUI visualizes the data can be found at the following link.

[video](https://github.com/SofarGroup13/real_time_dataVisualization/blob/master/GUI%20pictures/visualization_video.mp4)



# Report

A detailed description of the module can be found in the following report.

[Report](https://github.com/SofarGroup13/real_time_dataVisualization/blob/master/Project_13.pdf)
