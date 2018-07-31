import os
from wx import *

class PhotoCtrl(App):
    def __init__(self, redirect=False, filename=None):
        App.__init__(self, redirect, filename)
        self.frame = Frame(None, title='Picture Frame')

        self.panel = Panel(self.frame)

        self.PhotoMaxSize = 240

        self.createWidgets()
        self.frame.Show()

    def createWidgets(self):
        instructions = 'Browse for an image'
        img = EmptyImage(240,240)
        self.imageCtrl = StaticBitmap(self.panel, ID_ANY,
                                         BitmapFromImage(img))

        instructLbl = StaticText(self.panel, label=instructions)
        self.photoTxt = TextCtrl(self.panel, size=(200,-1))
        browseBtn = Button(self.panel, label='Browse')
        browseBtn.Bind(EVT_BUTTON, self.onBrowse)

        self.mainSizer = BoxSizer(VERTICAL)
        self.sizer = BoxSizer(HORIZONTAL)

        self.mainSizer.Add(StaticLine(self.panel, ID_ANY),
                           0, ALL|EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, ALL, 5)
        self.sizer.Add(self.photoTxt, 0, ALL, 5)
        self.sizer.Add(browseBtn, 0, ALL, 5)
        self.mainSizer.Add(self.sizer, 0, ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)

        self.panel.Layout()

    def onBrowse(self, event):
        """
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=FD_OPEN)
        if dialog.ShowModal() == ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

    def onView(self):
        filepath = self.photoTxt.GetValue()
        img = Image(filepath, BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(BitmapFromImage(img))
        self.panel.Refresh()

if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()
