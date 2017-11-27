import wx
import cv2
from Frame_Style import Window
from Neural_Network.NN_Plots import NN_plots

class ResultWindow(Window):
    def __init__(self,parent,title,History):
        Window.__init__(self, parent, title=title)
        panel=wx.Panel(self)

        background = wx.Colour(red=0, green=0, blue=0)
        self.SetBackgroundColour(background)

        Results = wx.StaticText(panel, label="RESULTS", pos=(100, 50))
        font = Results.GetFont()
        font.PointSize += 40
        font = font.Bold()
        Results.SetFont(font)
        Results.SetForegroundColour('white')

        #create the buttons

        selections =wx.Button(panel,label="See figures selection", pos=(250, 200), size=(200,30))
        accuracy_graphic =wx.Button(panel,label="See network data accuracy graphics", pos=(250, 250), size=(200,30))
        loss_graphic =wx.Button(panel,label="See network data loss graphics", pos=(250, 300), size=(200,30))
        archive =wx.Button(panel,label="See position archives", pos=(250, 350), size=(200,30))

        def showDataAcc(event):
            Plot1 = NN_plots(History)
            Plot1.Accuracy(History)

        def showDataLost(event):
            Plot1 = NN_plots(History)
            Plot1.Loss(History)

        # program the actions in the buttons
        self.History = History

        self.Bind(wx.EVT_BUTTON, self.showArchives, archive)
        self.Bind(wx.EVT_BUTTON, showDataAcc,accuracy_graphic)
        self.Bind(wx.EVT_BUTTON, showDataLost, loss_graphic)
        self.Bind(wx.EVT_BUTTON, self.showFigures, selections)

    def showFigures(self,event):
        newImg = cv2.imread('newImg.jpg')
        cv2.imshow("newImg",newImg)

    def showArchives(self,event):
        file = open('C:\\Users\\Liliana Reyes\\PycharmProjects\\OOP_Final_Project\\Machine_vision\\Result', 'r')
        Result = file.readlines()
        ResultString=''.join(Result)
        print(ResultString)
        dlg = wx.MessageDialog(self, ResultString,"Result", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

