import wx

class Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        # create the status bar
        self.CreateStatusBar()
        # setting up the menu
        filemenu = wx.Menu()

        # Create the options - about and exit -
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this little program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Close this beautiful program")
        # Create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")

        # Put the menu bar in the frame
        self.SetMenuBar(menuBar)

        # Program the methods that will order the buttons
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self, e):
         # This method show a dialog window
         dlg = wx.MessageDialog(self, "A little project, elaborated for me and very good friends...and a thing", "About Motoboy 1.0", wx.OK)
         dlg.ShowModal()  # Show it
         dlg.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.


