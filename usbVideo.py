# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\usbVideo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
import numpy as np
import os.path

class Ui_contraWindow(object):
    def setupUi(self, contraWindow):
        contraWindow.setObjectName("contraWindow")
        contraWindow.resize(941, 481)
        self.centralwidget = QtWidgets.QWidget(contraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(160, 0, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(300, 360, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 941, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("vessel.tif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.portSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.portSpinBox.setGeometry(QtCore.QRect(140, 280, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.portSpinBox.setFont(font)
        self.portSpinBox.setMinimum(0)
        self.portSpinBox.setMaximum(10)
        self.portSpinBox.setProperty("value", 0)
        self.portSpinBox.setObjectName("portSpinBox")
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setGeometry(QtCore.QRect(20, 290, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.portLabel.setFont(font)
        self.portLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName("portLabel")
        self.displayFramesOpt = QtWidgets.QSlider(self.centralwidget)
        self.displayFramesOpt.setGeometry(QtCore.QRect(840, 280, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(820, 250, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(890, 250, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(650, 290, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.displayFramesLabel.setFont(font)
        self.displayFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.displayFramesLabel.setObjectName("displayFramesLabel")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(550, 380, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.numFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.numFramesLabel.setGeometry(QtCore.QRect(280, 290, 241, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.numFramesLabel.setFont(font)
        self.numFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.numFramesLabel.setObjectName("numFramesLabel")
        self.numFramesEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numFramesEntry.setGeometry(QtCore.QRect(520, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.numFramesEntry.setFont(font)
        self.numFramesEntry.setObjectName("numFramesEntry")
        self.runButton.raise_()
        self.label.raise_()
        self.titleLabel.raise_()
        self.portSpinBox.raise_()
        self.portLabel.raise_()
        self.displayFramesOpt.raise_()
        self.dispOptNot.raise_()
        self.dispOptYes.raise_()
        self.displayFramesLabel.raise_()
        self.stopButton.raise_()
        self.numFramesLabel.raise_()
        self.numFramesEntry.raise_()
        contraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(contraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        contraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(contraWindow)
        self.statusbar.setObjectName("statusbar")
        contraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(contraWindow)
        QtCore.QMetaObject.connectSlotsByName(contraWindow)

# Added ================       
 
        self.initiateWidgets()

# =====================

    def retranslateUi(self, contraWindow):
        _translate = QtCore.QCoreApplication.translate
        contraWindow.setWindowTitle(_translate("contraWindow", "MainWindow"))
        self.titleLabel.setText(_translate("contraWindow", "conduXer<sup>2</sup>: Live Video Acquisition"))
        self.runButton.setText(_translate("contraWindow", "RUN"))
        self.portLabel.setText(_translate("contraWindow", "Port Option:"))
        self.dispOptNot.setText(_translate("contraWindow", "No"))
        self.dispOptYes.setText(_translate("contraWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("contraWindow", "Display Frames?"))
        self.stopButton.setText(_translate("contraWindow", "STOP"))
        self.numFramesLabel.setText(_translate("contraWindow", "No. of Frames to Acquire:"))
        self.numFramesEntry.setText(_translate("contraWindow", "10"))

    def initiateWidgets(self):
        self.runButton.clicked.connect(self.videoAcquisition)
        self.stopButton.clicked.connect(self.stopAcquisition)
        
    def stopAcquisition(self):
        global stopFlag
        print "Acquisition Cancelled!"
        stopFlag = 1
        
    def videoAcquisition(self):
                
        portOption = int(self.portSpinBox.value())
        displayOption = self.displayFramesOpt.value()
        numFrames = int(self.numFramesEntry.text())
        
        directory = 'images'
        
        if not os.path.exists(directory):
            os.makedirs(directory)

                # initialize camera
        cap = cv2.VideoCapture(portOption)
#        cap.set(cv2.cv.CV_CAP_PROP_EXPOSURE, 50) 
#        cap.set(cv2.cv.CV_CAP_PROP_FPS, 20) 

        if cap is None:
            print 'Warning: unable to access camera'
        
#        if displayOption == 1:
#            videoFrames = "Displaying Video Frames"
#            cv2.namedWindow(videoFrames, cv2.CV_WINDOW_AUTOSIZE)
#            cv2.startWindowThread()
        
        # stopPin = 7 # listen for a change on this pin to stop
        
        # number of frames to acquire
        currFrame = 0
        stopFlag = 0
        
#        cv2.namedWindow("Live")
        
        # outfilebase = 'images/image' # append number + .tif
        
#        print 'starting capture of ' + str(numFrames) + ' frames.'
#        print 'press ctrl-c to stop ... eventually we will stop on a TTL'
#        while(cap.isOpened()):
        while(True):
            try:
                ret, frame = cap.read()
                cv2.imshow("Live",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
#                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
#                if currFrame == 0:
#                    print grayFrame
#                    print np.amax(grayFrame)
#                    print np.amin(grayFrame)
                if ret==True:
#                    if displayOption == 1:
#                        cv2.imshow(videoFrames,frame)
                    # flip frame
                    # frame = cv2.flip(frame,0)
        
                    # print frame.shape
        
                    # write the flipped frame
                    try:
#                        out.write(frame)
#                        cv2.SaveImage('file' + str(currFrame) + '.tif', frame)
#                        print 'Attempint to save frames'
                        print currFrame+1
                        if currFrame == 0:
                            t0 = time.time()
                        else:
                            tempTime = ((time.time()-t0)*1000)/(currFrame)
                            print tempTime
                            cv2.imwrite(directory+'/'+'image' + str(currFrame) + '.tif', frame)
                            print "time.time(): %f " %  time.time()
                    except:
                        print 'Error in out.write() OR user hit ctrl-c'
                        break
        
                    currFrame += 1
                    # if (currFrame > numFrames):
                    #    print 'finished ' + str(numFrames) + ' frames.'
                    #    break
            
                    if currFrame == numFrames:
                        break
                    
                    if stopFlag == 1:
                        break
#            
                else:
                    break
                
        
        
            except KeyboardInterrupt:
#            except self.stopButton.clicked():
                print 'user hit ctrl-c'
                print 'frames=' + str(currFrame)
                break
        
        # Release camera
        cap.release()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    contraWindow = QtWidgets.QMainWindow()
    ui = Ui_contraWindow()
    ui.setupUi(contraWindow)
    contraWindow.show()
    sys.exit(app.exec_())

