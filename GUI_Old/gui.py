#!/usr/bin/env python

import sys
import rospy
from std_msgs import msg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Datavisualization(QMainWindow):
    """
    Documentation for a class.
 
    More details.
    """

    def __init__(self):
        """ 
        The loadui command will load the .UI file created by QT designer.
        This file is supposed to be in the same folder as the script

        Input: 
        A .UI file from QT designer

        WHAT THIS INITIALIZATION FUNCTION DO

        setting Progress bar value with 0.
        And the maximum limit will be 100

        Declaring the variables

        creating flag for buttons

        Adding actions to buttons.
        Every respective button will call a respective function that is link to the required task
        Buttons: 1) File'x' buttons are the ones for browsing the bag file
                 2) PlayAll and StopAll are for initiating and stopinng the timers and the progress bar
                 3) Exit is for exiting out of the Data visualization GUI
                 4) 'x'stop buttons are for stopping the respective timers

        Creating a timer object
        Adding actions to timer
        """

        super(Datavisualization, self).__init__()
        loadUi('final.ui', self)

       
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        
        self.count = 0
        self.count1 = 0
        self.count2 = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.sec1 = 0
        self.min1 = 0
        self.hour1 = 0
        self.sec2 = 0
        self.min2 = 0
        self.hour2 = 0
        self.lock = 1
        self.display = ''

        
        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.stopflag = False

       

        self.FileK.clicked.connect(self.kinectbag)
        self.FileS.clicked.connect(self.smartbag)
        self.FileM.clicked.connect(self.mocapbag)
        self.PlayAll.clicked.connect(self.playall)
        self.StopAll.clicked.connect(self.stopall)
        self.exit.clicked.connect(self.exitfile)
        self.kinectstop.clicked.connect(self.stoptimer)
        self.smartstop.pressed.connect(self.stoptimer1)
        self.mocapstop.pressed.connect(self.stoptimer2)



        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.timeout.connect(self.showTime1)
        timer.timeout.connect(self.showTime2)
        timer.timeout.connect(self.Increase_Step)


        timer.start(1000)


   

    def Increase_Step(self):
        """
        function will be initiated when the PlayAll button is pressed

        Returns: 
            Increase the value of a progress bar with 1%
        """

        if self.flag3:
            self.progressBar.setValue(self.progressBar.value() + 1)



    def Stop_step(self):
        """
        function will be called when the StopAll button is pressed
        
        Returns: 
            Will set the value of progressbar to zero
        """
        
        self.progressBar.setValue(0)


    def QTimer(self):
        """
        Function adds action to timer
        """

        self.timeout.connect(self.showTime)
        self.timeout.connect(self.showTime1)
        self.timeout.connect(self.showTime2)
        self.timeout.connect(self.Increase_Step)


        self.start(1000)


    def showTime(self):
        """
        function will show value of kinect timer
        will check if flag is true and will increment the counter

        Returns:
            Display the value of the timer in HH/MM/SS
        """
       
        if self.flag:
           
            self.count += 1

        if self.count >= 60:
            self.count = 0
            self.min += 1

        else:
            self.sec = self.count

        if self.min > 59:
            self.min = 0
            self.hour += 1

        if self.hour > 23:
            self.hour = 0

        
        self.display1 = '%s  : %s : %s' % (self.hour, self.min, self.sec)
        self.display2.setText(' %s\n\n%s' % (self.display1, self.display))

  
    def showTime1(self):      
        """
        function will show value of SmartWatch timer
        will check if flag is true and will increment the counter

        Returns:
            Display the value of the timer in HH/MM/SS
        """
       
        if self.flag1:
          
            self.count1 += 1

        if self.count1 >= 60:
            self.count1 = 0
            self.min1 += 1
        else:
            self.sec1 = self.count1

        if self.min1 > 59:
            self.min1 = 0
            self.hour1 += 1

        if self.hour1 > 23:
            self.hour1 = 0

       
        self.display5 = '%s  : %s : %s' % (self.hour1, self.min1, self.sec1)
        self.display3.setText(' %s\n\n%s' % (self.display5, self.display))


    def showTime2(self):
        """
        function will show value of mocap timer
        will check if flag is true and will increment the counter

        Returns:
            Display the value of the timer in HH/MM/SS
        """

        if self.flag2:

            self.count2 += 1

        if self.count2 >= 60:
            self.count2 = 0
            self.min2 += 1
        else:
            self.sec2 = self.count2

        if self.min2 > 59:
            self.min2 = 0
            self.hour2 += 1

        if self.hour2 > 23:
            self.hour2 = 0

        self.display6 = '%s  : %s : %s' % (self.hour2, self.min2, self.sec2)
        self.display4.setText(' %s\n\n%s' % (self.display6, self.display))


    def playall(self):
        """
        function will call the sub-function when PlayAll button is pressed
        
        Returns:
            initiate the timer and progress bar and will set the flags to TRUE
        """
        
        self.flag = True
        self.flag1 = True
        self.flag2 = True
        self.flag3 = True

        self.showTime()
        self.showTime1()
        self.showTime2()
        self.Increase_Step()

    def stopall(self):
        """
        fucntion will call the sub-functions when StopAll button is pressed
        
        Returns:
            This will put everything to stop i-e Timers and progressbar
        """

        self.stoptimer()
        self.stoptimer1()
        self.stoptimer2()
        self.Stop_step()

   

    def kinectbag(self):
        """
        This function is linked to 'FileK' button which will browse the bag file
        The browsing window will open into the home directory of the system

        Returns:
            Browse,play and dispay the path of bag file 
         """

        print("Browsing")
        filename = QFileDialog.getOpenFileName(self, 'OPEN BAG FILE ', r"home\\", "BAG FILES(*.bag)")
        path = filename[0]
        self.BrowserK.setText(path)


    def smartbag(self):
        """
        This function is linked to 'Files' button which will browse the bag file
        The browsing window will open into the home directory of the system

        Returns:
            Browse,play and dispay the path of bag file
         """

        print("Browsing")
        filename = QFileDialog.getOpenFileName(self, 'OPEN BAG FILE ', r"home\\", "BAG FILES(*.bag)")
        path = filename[0]
        self.BrowserS.setText(path)


    def mocapbag(self):
        """
        This function is linked to 'FileM' button which will browse the bag file
        The browsing window will open into the home directory of the system

        Returns:
            Browse,play and dispay the path of bag file         
         """

        print("Browsing")
        filename = QFileDialog.getOpenFileName(self, 'OPEN BAG FILE ', r"home\\zaid", "BAG FILES(*.bag)")
        path = filename[0]
        self.BrowserM.setText(path)

  
    def stoptimer(self):
        """
        Thisfunction will stop the Kinect timer in an individual capacity

        Returns:
            Stop the time
        """

        self.flag = False
        self.count = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.display1 = '%s  : %s : %s' % (self.hour, self.min, self.sec)
        self.display2.setText(' %s\n\n%s' % (self.display1, self.display))

    def stoptimer1(self):
        """
        Thisfunction will stop the SmartWatch timer in an individual capacity

        Returns:
            Stop the time
        """

        self.flag1 = False
        self.count1 = 0
        self.sec1 = 0
        self.min1 = 0
        self.hour1 = 0
        self.display5 = '%s  : %s : %s' % (self.hour1, self.min1, self.sec1)
        self.display3.setText(' %s\n\n%s' % (self.display5, self.display))


    def stoptimer2(self):
        """
        Thisfunction will stop the Kinect timer in an individual capacity

        Returns:
            Stop the timer
        """

        self.flag2 = False
        self.count2 = 0
        self.sec2 = 0
        self.min2 = 0
        self.hour2 = 0
        self.display6 = '%s  : %s : %s' % (self.hour2, self.min2, self.sec2)
        self.display4.setText(' %s\n\n%s' % (self.display6, self.display))


    def exitfile(self):
        """
        function exits the UI

        Returns:
            Process terminates
        """

        sys.exit()


if __name__ == "__main__":
    rospy.init_node('data_gui', disable_signals= True)

    app = QApplication([])
    window = Datavisualization()
    window.show()
    sys.exit(app.exec())



