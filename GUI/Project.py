import wx
from Main_Frame import MainWindow
from Results_Frame import ResultWindow
from Loading_Frame import LoadingWindow
from Neural_Network.NN_Plots import NN_plots
app = wx.App(False)
MainWindow(None,"Motoboy 1.0")
app.MainLoop()
L=LoadingWindow(None,"Motoboy 1.0")
app.MainLoop()
ResultWindow(None,"Motoboy 1.0",L.historyl)
app.MainLoop()
