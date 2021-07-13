import csv
import sys
import rospy
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os
from os.path import dirname, realpath,join
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QAction,QFileDialog
from PyQt5.uic import  loadUiType
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from std_msgs import msg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

scriptDir=dirname(realpath(__file__))
From_Main,_= loadUiType(join(dirname(__file__),"updated_gui.ui"))

#data = pd.read_csv("/root/Downloads/Final/1.csv")

class Sheet(QMainWindow,From_Main):
    
    def __init__(self):
        super(Sheet, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ToolBar()
        self.sc =myCanvas()
        self.l=QVBoxLayout(self.frame)
        self.l.addWidget(self.sc)
        
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

	#self.FileK.clicked.connect(self.kinectbag)
        self.FileS.clicked.connect(self.smartbag)
        #self.FileM.clicked.connect(self.mocapbag)
        self.PlayAll.clicked.connect(self.playall)
        self.StopAll.clicked.connect(self.stopall)
        self.exit.clicked.connect(self.exitfile)
        self.kinectstop.clicked.connect(self.stoptimer)
        self.smartstop.pressed.connect(self.stoptimer1)
        self.mocapstop.pressed.connect(self.stoptimer2)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.timeout.connect(self.showTime1)
        self.timer.timeout.connect(self.showTime2)
        self.timer.timeout.connect(self.Increase_Step)


        self.timer.start(1000)
        
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
        
    def ToolBar(self):
        AddFile = QAction(QIcon('image.png'),'Add File',self)
        AddFile.triggered.connect(self.smartbag)
        self.toolBar= self.addToolBar('Add data File')
        self.toolBar.addAction(AddFile)
        AddPlot = QAction(QIcon('scatter.png'),'Scatter',self)
        AddPlot.triggered.connect(self.Plot)
        self.toolBar.addAction(AddPlot)
        
    def smartbag(self):
        """
        This function is linked to 'Files' button which will browse the bag file
        The browsing window will open into the home directory of the system

        Returns:
            Browse,play and dispay the path of bag file
         """
        print("Browsing")
        path = QFileDialog.getOpenFileName(self, 'OPEN CSV FILE ', r"/root/Desktop/real_time_dataVisualization/GUI_updated/", "CSV FILES(*.csv)")
        #path = filename[0]
        if path[0]!='':
           self.FileN=path[0]
    
    def Plot(self):
        f=self.FileN
        index = int(self.lineEdit.text())
        x= []
        y=[]
        with open(f, newline = '') as csv_file:
            my_file = csv.reader(csv_file, delimiter = ',',quotechar = '|')
            for row in my_file:
                x.append(str(row[0]))
                y.append(str(row[index]))
        self.sc.plot(x, y)
	    
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
        
class myCanvas(FigureCanvas):
    def __init__(self):
        self.fig=Figure()
        FigureCanvas.__init__(self,self.fig)
        

        
    def plot(self,xarray,yarray):
        self.fig.clear()
        self.ax1= self.fig.add_subplot(611)
        self.ax2= self.fig.add_subplot(612)
        self.ax3= self.fig.add_subplot(613)
        self.ax4= self.fig.add_subplot(614)
        self.ax5= self.fig.add_subplot(615)
        self.ax6= self.fig.add_subplot(616)

        self.ax1.plot(xarray[1:],yarray[1:])
        self.ax2.plot(xarray[10:],yarray[10:])
        self.ax3.plot(xarray[15:],yarray[15:])
        self.ax4.plot(xarray[20:],yarray[20:])
        self.ax5.plot(xarray[30:],yarray[30:])
        self.ax6.plot(xarray[50:],yarray[50:])
	
        self.draw()

app = QApplication(sys.argv)
sheet= Sheet()
sheet.show()
sys.exit(app.exec_())
