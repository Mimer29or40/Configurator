# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Configurator
###########################################################################


class Configurator(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="Configurator",
            pos=wx.DefaultPosition,
            size=wx.Size(883, 698),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.menubar = wx.MenuBar(0)
        self.menu_file = wx.Menu()
        self.menu_new = wx.MenuItem(
            self.menu_file,
            wx.ID_ANY,
            "New" + "\t" + "CTRL+N",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.menu_file.Append(self.menu_new)

        self.menu_open = wx.MenuItem(
            self.menu_file, wx.ID_ANY, "Open...", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.menu_file.Append(self.menu_open)

        self.menu_save = wx.MenuItem(
            self.menu_file,
            wx.ID_ANY,
            "Save" + "\t" + "CTRL+S",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.menu_file.Append(self.menu_save)

        self.menu_save_as = wx.MenuItem(
            self.menu_file,
            wx.ID_ANY,
            "Save as..." + "\t" + "CTRL+SHIFT+S",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.menu_file.Append(self.menu_save_as)

        self.menu_file.AppendSeparator()

        self.menu_settings = wx.MenuItem(
            self.menu_file, wx.ID_ANY, "Settings", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.menu_file.Append(self.menu_settings)

        self.menu_file.AppendSeparator()

        self.menu_close = wx.MenuItem(
            self.menu_file,
            wx.ID_ANY,
            "Close" + "\t" + "CTRL+W",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.menu_file.Append(self.menu_close)

        self.menubar.Append(self.menu_file, "File")

        self.SetMenuBar(self.menubar)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.project_name_label = wx.StaticText(
            self.m_panel1,
            wx.ID_ANY,
            "Project Name",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.project_name_label.Wrap(-1)

        gbSizer2.Add(
            self.project_name_label,
            wx.GBPosition(0, 0),
            wx.GBSpan(1, 1),
            wx.ALIGN_CENTER | wx.ALL,
            5,
        )

        self.project_name_text = wx.TextCtrl(
            self.m_panel1,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        gbSizer2.Add(
            self.project_name_text,
            wx.GBPosition(0, 1),
            wx.GBSpan(1, 1),
            wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND,
            5,
        )

        self.project_selection_label = wx.StaticText(
            self.m_panel1,
            wx.ID_ANY,
            "Project Choice",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.project_selection_label.Wrap(-1)

        gbSizer2.Add(
            self.project_selection_label,
            wx.GBPosition(1, 0),
            wx.GBSpan(1, 1),
            wx.ALIGN_CENTER | wx.ALL,
            5,
        )

        project_choiceChoices = []
        self.project_choice = wx.Choice(
            self.m_panel1,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            project_choiceChoices,
            0,
        )
        self.project_choice.SetSelection(0)
        gbSizer2.Add(
            self.project_choice,
            wx.GBPosition(1, 1),
            wx.GBSpan(1, 1),
            wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND,
            5,
        )

        project_radio_boxChoices = ["Red", "Green", "Blue"]
        self.project_radio_box = wx.RadioBox(
            self.m_panel1,
            wx.ID_ANY,
            "Project Radio Box",
            wx.DefaultPosition,
            wx.DefaultSize,
            project_radio_boxChoices,
            3,
            wx.RA_SPECIFY_COLS,
        )
        self.project_radio_box.SetSelection(0)
        gbSizer2.Add(
            self.project_radio_box,
            wx.GBPosition(2, 0),
            wx.GBSpan(1, 2),
            wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND,
            5,
        )

        self.project_toggle_button = wx.CheckBox(
            self.m_panel1,
            wx.ID_ANY,
            "Project Toggle",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        gbSizer2.Add(
            self.project_toggle_button,
            wx.GBPosition(3, 0),
            wx.GBSpan(1, 2),
            wx.ALL | wx.EXPAND,
            5,
        )

        self.project_slider_label = wx.StaticText(
            self.m_panel1,
            wx.ID_ANY,
            "Project Slider",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.project_slider_label.Wrap(-1)

        gbSizer2.Add(
            self.project_slider_label,
            wx.GBPosition(4, 0),
            wx.GBSpan(1, 1),
            wx.ALIGN_CENTER | wx.ALL,
            5,
        )

        self.project_slider = wx.Slider(
            self.m_panel1,
            wx.ID_ANY,
            50,
            0,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SL_HORIZONTAL | wx.SL_LABELS | wx.SL_SELRANGE,
        )
        gbSizer2.Add(
            self.project_slider,
            wx.GBPosition(4, 1),
            wx.GBSpan(1, 1),
            wx.ALL | wx.EXPAND,
            5,
        )

        gbSizer2.AddGrowableCol(1)

        self.m_panel1.SetSizer(gbSizer2)
        self.m_panel1.Layout()
        gbSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel2 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.project_name_text.Bind(wx.EVT_TEXT, self.project_config_changed)
        self.project_choice.Bind(wx.EVT_CHOICE, self.project_config_changed)
        self.project_radio_box.Bind(wx.EVT_RADIOBOX, self.project_config_changed)
        self.project_toggle_button.Bind(wx.EVT_CHECKBOX, self.project_config_changed)
        self.project_slider.Bind(wx.EVT_SLIDER, self.project_config_changed)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def project_config_changed(self, event):
        print(event)
