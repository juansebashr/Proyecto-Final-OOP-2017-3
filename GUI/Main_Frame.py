import wx
import os
from PIL import Image
from Frame_Style import Window

program_intructions =("This program will take an image and process it with machine vision and neural networks \n"
                      "Press change parameters if you want to change the parameters of the AI\n"
                       "Press Upload a photo to upload the picture to process\n"
                       "Press START!!! to begin")

#Its create the Main window

class MainWindow(Window):
    def __init__(self,parent,title):
        Window.__init__(self, parent,title)

        #create the panel
        panel=wx.Panel(self)

        second_color = wx.Colour(red=128, green=128, blue=128)
        # Write some of the text
        program_title = wx.StaticText(panel, label="MOTOBOY 1.0", pos=(495, 50))
        menu = wx.StaticText(panel, label= "Menu", pos=(495, 100))
        font = program_title.GetFont()
        font.PointSize += 20
        font = font.Bold()
        program_title.SetFont(font)
        menu.SetFont(font)

        menu.SetForegroundColour(second_color)

        #change the background color
        background = wx.Colour(red=17,green=0,blue=129)
        self.SetBackgroundColour(background)
        #import the image
        motomanImg = wx.Image("Motoman.jpg",wx.BITMAP_TYPE_ANY)
        motomanImg2 = motomanImg.Rescale(300,400)

        #Put the image as a bit map
        motomanImg3 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(motomanImg2), pos=(50, 50))

        #Create the buttons

        instructions =wx.Button(panel,label="Instructions", pos=(495, 200), size=(150,30))
        #change_para =wx.Button(panel,label="Change Parameters", pos=(495, 260), size=(150,30))
        upl_photo = wx.Button(panel,label="Upload a photo", pos=(495, 320), size=(150,30))
        start_program = wx.Button(panel,label="START!!!", pos=(495, 400), size=(150,60))
        start_program.SetBackgroundColour(second_color)

        #program the actions in the buttons
        self.Bind(wx.EVT_BUTTON, self.showInst, instructions)
        #self.Bind(wx.EVT_BUTTON, self.changePara, change_para)
        self.Bind(wx.EVT_BUTTON, self.upload, upl_photo)
        self.Bind(wx.EVT_BUTTON, self.programExit, start_program)



    # Program the methods that will control the buttons
    def programExit(self,e):
        self.Close(True)

    def showInst(self,e):
        dlg = wx.MessageDialog(self,program_intructions,"Instructions" ,wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    # This method will allow the program to take the image
    def upload(self, e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose an image", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            #Open as a image on the path given and then saving it on the project path
            Image1 = Image.open(os.path.join(self.dirname, self.filename))
            Image1.save('C:\\Users\\Liliana Reyes\\PycharmProjects\\OOP_Final_Project\\Images\\Img1.jpg','JPEG')
        dlg.Destroy()

    def changePara(self,e):
        # Create frame
        little_frame = wx.Frame(None, -1, 'Parameters')
        little_frame.SetSize(0, 0, 200, 50)

        # Create text input
        dlg = wx.TextEntryDialog(little_frame, 'Enter some text','Text Entry')
        dlg.SetValue("Default")
        if dlg.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % dlg.GetValue())
        dlg.Destroy()