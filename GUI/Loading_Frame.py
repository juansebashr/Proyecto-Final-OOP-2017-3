import wx
from Machine_vision.Vision import vision
from Frame_Style import Window
from Neural_Network.NN_Parameters import NN_parameters
from Neural_Network.Neural_Network import Neural_Network
class LoadingWindow(Window):
    def __init__(self,parent,title):
        Window.__init__(self, parent, title=title)
        panel=wx.Panel(self)

        background = wx.Colour(red=0, green=0, blue=0)
        self.SetBackgroundColour(background)

        loading_title = wx.StaticText(panel, label="LOADING...", pos=(250, 200))
        font = loading_title.GetFont()
        font.PointSize += 40
        font = font.Bold()
        loading_title.SetFont(font)
        loading_title.SetForegroundColour('white')

        #run vision method
        vision()

        #run NN method
        Parameters=NN_parameters('relu','sigmoid',181,100)
        NN = Neural_Network('relu', 'sigmoid', 181, 100)
        History = NN.History
        self.historyl = History
        self.Close(True)
