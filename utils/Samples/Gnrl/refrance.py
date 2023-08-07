#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Tue Aug  4 18:55:10 2020
#
import os
import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pyshark
import wx.dataview as dv

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('WXAgg')
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

wildcardCsvFile = ".csv source (*.csv)|*.csv|" \
				  "All files (*.*)|*.*"

wildcardPcapFile = ".csv source (*.pcap)|*.pcap|" \
				  "All files (*.*)|*.*"


class CanvasPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.figure = Figure()
		self.axes = self.figure.add_subplot()
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		#self.sizer.Add(self.canvas, 1)
		self.sizer.Add(self.canvas, -1, wx.EXPAND)
		self.SetSizer(self.sizer)
		self.Fit()

	def draw(self,t,s):

		self.axes.plot(t, s)

class DataAnalysisLabFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		wx.Locale = "en"

		# begin wxGlade: DataAnalysisLabFrame.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((1250, 800))
		# Menu Bar
		self.mainFrame_menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Close"), "")
		self.Bind(wx.EVT_MENU, self.CloseHandler, id=item.GetId())
		self.mainFrame_menubar.Append(wxglade_tmp_menu, _("File"))
		wxglade_tmp_menu = wx.Menu()
		item = wxglade_tmp_menu.Append(wx.ID_ANY, _("About"), "")
		self.Bind(wx.EVT_MENU, self.AboutHandler, id=item.GetId())
		self.mainFrame_menubar.Append(wxglade_tmp_menu, _("Help"))
		self.SetMenuBar(self.mainFrame_menubar)
		# Menu Bar end
		self.controlPanel = wx.Panel(self, wx.ID_ANY)
		self.LoadData1 = wx.Button(self.controlPanel, wx.ID_ANY, _("Load Data-1"))
		self.LoadData2 = wx.Button(self.controlPanel, wx.ID_ANY, _("Load Data-2"))
		self.AnalyzeData1 = wx.Button(self.controlPanel, wx.ID_ANY, _("Analyze Data-1"))
		self.AnalyzeData2 = wx.Button(self.controlPanel, wx.ID_ANY, _("Analyze Data-2"))
		self.CompareData = wx.Button(self.controlPanel, wx.ID_ANY, _("Compare"))
		self.SniffDataFile = wx.Button(self.controlPanel, wx.ID_ANY, _("Sniff Data File"))
		self.SniffDataLive = wx.Button(self.controlPanel, wx.ID_ANY, _("Sniff Data Live"))
		self.interface_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.timeout_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.filter_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.dataPanel = wx.Panel(self, wx.ID_ANY)
		self.dataNB = wx.Notebook(self.dataPanel, wx.ID_ANY)
		self.CompareTab = wx.Panel(self.dataNB, wx.ID_ANY)
		#self.graphPanel = wx.Panel(self.CompareTab, wx.ID_ANY, style=wx.BORDER_RAISED | wx.TAB_TRAVERSAL)
		self.graphPanel = CanvasPanel(self.CompareTab)

		self.Data1 = wx.ScrolledWindow(self.dataNB, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
		self.list_data_1 = wx.ListCtrl(self.Data1, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

		self.Data2 = wx.ScrolledWindow(self.dataNB, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
		self.list_data_2 = wx.ListCtrl(self.Data2, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

		self.configPanel = wx.Panel(self, wx.ID_ANY)
		self.ClearLog = wx.Button(self.configPanel, wx.ID_ANY, _("Clear Log"))
		self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

		self.Bind(wx.EVT_BUTTON, self.LoadData1BtnHandler, self.LoadData1)
		self.Bind(wx.EVT_BUTTON, self.LoadData2BtnHandler, self.LoadData2)
		self.Bind(wx.EVT_BUTTON, self.AnalyzeData1BtnHandler, self.AnalyzeData1)
		self.Bind(wx.EVT_BUTTON, self.AnalyzeData2BtnHandler, self.AnalyzeData2)
		self.Bind(wx.EVT_BUTTON, self.CompareBtnHandler, self.CompareData)
		self.Bind(wx.EVT_BUTTON, self.SniffDataFileBtnHandler, self.SniffDataFile)
		self.Bind(wx.EVT_BUTTON, self.SniffDataLiveBtnHandler, self.SniffDataLive)
		self.interface_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.timeout_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.filter_text_ctrl = wx.TextCtrl(self.controlPanel, wx.ID_ANY, "")
		self.Bind(wx.EVT_NAVIGATION_KEY, self.graphPanelSelect)
		self.Bind(wx.EVT_NAVIGATION_KEY, self.graphTabSelect)
		self.Bind(wx.EVT_NAVIGATION_KEY, self.data1TabSelect)
		self.Bind(wx.EVT_NAVIGATION_KEY, self.data2TabSelect)
		self.Bind(wx.EVT_BUTTON, self.ClearLogBtnHandler, self.ClearLog)

		# end wxGlade
		# Create a dataview control
		#self.dvcDataEth = dv.DataViewCtrl(self,
		#						   style=wx.BORDER_THEME
		#								 | dv.DV_ROW_LINES  # nice alternating bg colors
		#								 | dv.DV_VERT_RULES
		#						   )
		#c0 = self.dvcDataEth.AppendTextColumn("C0", 0, width=250, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c2 = self.dvcDataEth.AppendTextColumn("C1", 2, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c3 = self.dvcDataEth.AppendTextColumn("C2", 3, width=150, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c5 = self.dvcDataEth.AppendTextColumn("C3", 5, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c6 = self.dvcDataEth.AppendTextColumn('C4', 6, width=150, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c7 = self.dvcDataEth.AppendTextColumn('C5', 7, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#c8 = self.dvcDataEth.AppendToggleColumn('C6', 8, width=100, mode=dv.DATAVIEW_CELL_ACTIVATABLE)
		# Set some additional attributes for all the columns
		#for c in self.dvcDataEth.Columns:
		#	c.Sortable = True
		#	c.Reorderable = True



		#self.dvcDataUsb = dv.DataViewCtrl(self,
		#								style=wx.BORDER_THEME
		#									  | dv.DV_ROW_LINES  # nice alternating bg colors
		#									  | dv.DV_VERT_RULES
		#								)

		#cc0 = self.dvcDataUsb.AppendTextColumn("C0", 0, width=250, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc2 = self.dvcDataUsb.AppendTextColumn("C1", 2, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc3 = self.dvcDataUsb.AppendTextColumn("C2", 3, width=150, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc5 = self.dvcDataUsb.AppendTextColumn("C3", 5, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc6 = self.dvcDataUsb.AppendTextColumn('C4', 6, width=150, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc7 = self.dvcDataUsb.AppendTextColumn('C5', 7, width=200, mode=dv.DATAVIEW_CELL_EDITABLE)
		#cc8 = self.dvcDataUsb.AppendToggleColumn('C6', 8, width=100, mode=dv.DATAVIEW_CELL_ACTIVATABLE)
		# Set some additional attributes for all the columns
		#for c in self.dvcDataUsb.Columns:
		#	c.Sortable = True
		#	c.Reorderable = True

		self.__set_properties()
		self.__do_layout()
		self.__do_usr_init()

	def __set_properties(self):
		# begin wxGlade: DataAnalysisLabFrame.__set_properties
		self.SetTitle(_("DataAnalysisLab"))
		self.LoadData1.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.LoadData2.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.AnalyzeData1.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.AnalyzeData2.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.CompareData.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.SniffDataFile.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.SniffDataLive.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.controlPanel.SetBackgroundColour(wx.Colour(50, 153, 204))
		self.Data1.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.Data2.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.dataPanel.SetMinSize((1100, 650))
		self.dataPanel.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.ClearLog.SetBackgroundColour(wx.Colour(255, 255, 255))
		self.configPanel.SetBackgroundColour(wx.Colour(136, 183, 204))
		self.list_ctrl_1.SetMinSize((900, -1))



		self.list_ctrl_1.AppendColumn(_("A"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_ctrl_1.AppendColumn(_("B"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_ctrl_1.AppendColumn(_("C"), format=wx.LIST_FORMAT_LEFT, width=-1)

		self.list_data_1.SetMinSize((900, -1))
		self.list_data_1.AppendColumn(_("Time"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_data_1.AppendColumn(_("Type"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_data_1.AppendColumn(_("Data"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_data_2.SetMinSize((900, -1))
		self.list_data_2.AppendColumn(_("Time"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_data_2.AppendColumn(_("Type"), format=wx.LIST_FORMAT_LEFT, width=-1)
		self.list_data_2.AppendColumn(_("Data"), format=wx.LIST_FORMAT_LEFT, width=-1)

		# end wxGlade


	def __do_layout(self):
		# begin wxGlade: DataAnalysisLabFrame.__do_layout
		frameSizer = wx.BoxSizer(wx.VERTICAL)
		bottomSizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer_8 = wx.StaticBoxSizer(wx.StaticBox(self.configPanel, wx.ID_ANY, _("Config")), wx.HORIZONTAL)
		topSizer = wx.BoxSizer(wx.HORIZONTAL)
		dataPanelSizer = wx.BoxSizer(wx.HORIZONTAL)
		data2Grid = wx.BoxSizer(wx.HORIZONTAL)
		data1Grid = wx.BoxSizer(wx.HORIZONTAL)
		CompareTabSizer = wx.BoxSizer(wx.HORIZONTAL)
		controlSizer = wx.BoxSizer(wx.VERTICAL)
		SnifferSizer = wx.StaticBoxSizer(wx.StaticBox(self.controlPanel, wx.ID_ANY, _("Sniffer")), wx.VERTICAL)
		DataAnalysisSizer = wx.StaticBoxSizer(wx.StaticBox(self.controlPanel, wx.ID_ANY, _("Data Analysis")),wx.VERTICAL)
		DataLoadingSizer = wx.StaticBoxSizer(wx.StaticBox(self.controlPanel, wx.ID_ANY, _("Data Loading")), wx.VERTICAL)
		DataLoadingSizer.Add(self.LoadData1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		DataLoadingSizer.Add(self.LoadData2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		controlSizer.Add(DataLoadingSizer, 1, wx.ALL | wx.EXPAND, 0)
		DataAnalysisSizer.Add(self.AnalyzeData1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		DataAnalysisSizer.Add(self.AnalyzeData2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		DataAnalysisSizer.Add(self.CompareData, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		controlSizer.Add(DataAnalysisSizer, 1, wx.EXPAND, 0)
		SnifferSizer.Add(self.SniffDataFile, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		SnifferSizer.Add(self.SniffDataLive, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
		CaptureInterface = wx.StaticText(self.controlPanel, wx.ID_ANY, _("Capture Interface:"), style=wx.ALIGN_LEFT)
		SnifferSizer.Add(CaptureInterface, 0, 0, 0)
		SnifferSizer.Add(self.interface_text_ctrl, 0, 0, 0)
		CaptureTimeout = wx.StaticText(self.controlPanel, wx.ID_ANY, _("Capture Timeout:"), style=wx.ALIGN_LEFT)
		SnifferSizer.Add(CaptureTimeout, 0, 0, 0)
		SnifferSizer.Add(self.timeout_text_ctrl, 0, 0, 0)
		CaptureFilter = wx.StaticText(self.controlPanel, wx.ID_ANY, _("Capture Filter:"), style=wx.ALIGN_LEFT)
		SnifferSizer.Add(CaptureFilter, 0, 0, 0)
		SnifferSizer.Add(self.filter_text_ctrl, 0, 0, 0)
		controlSizer.Add(SnifferSizer, 1, wx.EXPAND, 0)
		self.controlPanel.SetSizer(controlSizer)
		topSizer.Add(self.controlPanel, 1, wx.ALL | wx.EXPAND, 1)

		CompareTabSizer.Add(self.graphPanel, 1, wx.EXPAND, 0)
		self.CompareTab.SetSizer(CompareTabSizer)

		#data1Grid.Add(self.dvcDataEth, 1, wx.ALL , 0)#was grid 1
		data1Grid.Add(self.list_data_1, 1, wx.EXPAND, 0)
		self.Data1.SetSizer(data1Grid)

		#data2Grid.Add(self.dvcDataUsb, 1, wx.ALL , 0)#was grid 2
		data2Grid.Add(self.list_data_2, 1, wx.EXPAND, 0)
		self.Data2.SetSizer(data2Grid)

		self.dataNB.AddPage(self.CompareTab, _("Compare"))
		self.dataNB.AddPage(self.Data1,_("Data 1"))
		self.dataNB.AddPage(self.Data2, _("Data 2"))
		dataPanelSizer.Add(self.dataNB, 1, wx.EXPAND, 0)
		self.dataPanel.SetSizer(dataPanelSizer)
		topSizer.Add(self.dataPanel, 1, wx.ALL | wx.EXPAND, 1)
		frameSizer.Add(topSizer, 1, wx.EXPAND, 0)
		sizer_8.Add(self.ClearLog, 0, wx.ALL, 0)
		self.configPanel.SetSizer(sizer_8)
		bottomSizer.Add(self.configPanel, 1, wx.EXPAND, 0)
		bottomSizer.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND, 0)
		frameSizer.Add(bottomSizer, 1, wx.EXPAND, 0)
		self.SetSizer(frameSizer)
		self.Layout()
		# end wxGlade

		self.Center()
		self.SetLayoutDirection(wx.Layout_LeftToRight)

	def __do_usr_init(self):
		self.packets_array = []
		self.selectedInterface = ""
		self.selectedFilter = ""


	##***********************************************************************
	## Handlers
	##***********************************************************************
	def CloseHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.Close()

	def AboutHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'AboutHandler' not implemented!")
		event.Skip()

	def LoadData1BtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.LoadSrcFileHandler(event)

	def LoadData2BtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.LoadDstFileHandler(event)

	def AnalyzeData1BtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'AnalyzeData1BtnHandler' not implemented!")
		event.Skip()

	def AnalyzeData2BtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'AnalyzeData2BtnHandler' not implemented!")
		event.Skip()

	def ClearLogBtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'ClearLogBtnHandler' not implemented!")
		event.Skip()

	def CompareBtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		plt.plot(self.seriesSrcFileFinal['Delta'], 'go', self.seriesDstFileFinal['Delta'], 'r^')
		plt.show()

	def SniffDataFileBtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'SniffDataFileBtnHandler' not implemented!")
		event.Skip()

	def SniffDataLiveBtnHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'SniffDataLiveBtnHandler' not implemented!")
		event.Skip()

	def InterfaceTextCtrlHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.selectedInterface = event.GetString()

	def TimeoutTextCtrlHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.selectedTimeout = event.GetString()

	def FilterTextCtrlHandler(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		self.selectedFilter = event.GetString()

	def graphPanelSelect(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'graphPanelSelect' not implemented!")
		event.Skip()

	def graphTabSelect(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'graphTabSelect' not implemented!")
		event.Skip()

	def data1TabSelect(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'data1TabSelect' not implemented!")
		event.Skip()

	def data2TabSelect(self, event):  # wxGlade: DataAnalysisLabFrame.<event_handler>
		print("Event handler 'data2TabSelect' not implemented!")
		event.Skip()

	##***********************************************************************
	## User Functions
	##***********************************************************************


	def SniffDataLiveBtnHandler(self, event):
		start = time.time()
		capture = pyshark.LiveCapture(interface=self.selectedInterface)
		#capture.sniff(timeout=10)

		for item in capture.sniff_continuously():
			if self.selectedTimeout and time.time() - start > self.selectedTimeout:
				break
			yield item


	def SniffDataFileBtnHandler(self, event):

		dlg = wx.FileDialog(
			self, message="Choose a file",
			defaultDir=os.getcwd(),
			defaultFile="",
			# wildcard=wildcardDstFile,
			wildcard=wildcardPcapFile,
			style=wx.FD_OPEN | wx.FD_MULTIPLE |
				  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
				  wx.FD_PREVIEW
		)

		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			pass

		self.wiresharkFile = paths[0]

		dlg.Destroy()
		numOfPackets = self.AnalyzeWiresharkFile()
		print("Packets number:" + str(numOfPackets))

	def counter(self,*args):
		self.packets_array.append(args[0])

	def AnalyzeWiresharkFile(self):
		cap = pyshark.FileCapture(self.wiresharkFile, keep_packets=False)
		cap.apply_on_packets(self.counter, timeout=10000)
		return len(self.packets_array)

	def LoadSrcFileHandler(self, event):  # wxGlade: MyFrame.<event_handler>
		# self.log.WriteText("CWD: %s\n" % os.getcwd())

		# Create the dialog. In this case the current directory is forced as the starting
		# directory for the dialog, and no default file name is forced. This can easilly
		# be changed in your program. This is an 'open' dialog, and allows multitple
		# file selections as well.
		#
		# Finally, if the directory is changed in the process of getting files, this
		# dialog is set up to change the current working directory to the path chosen.
		dlg = wx.FileDialog(
			self, message="Choose a file",
			defaultDir=os.getcwd(),
			defaultFile="",
			# wildcard=wildcardSrcFile,
			wildcard=wildcardCsvFile,
			style=wx.FD_OPEN | wx.FD_MULTIPLE |
				  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
				  wx.FD_PREVIEW
		)

		# Show the dialog and retrieve the user response. If it is the OK response,
		# process the data.
		if dlg.ShowModal() == wx.ID_OK:
			# This returns a Python list of files that were selected.
			paths = dlg.GetPaths()

			pass
		# self.log.WriteText('You selected %d files:' % len(paths))

		# for path in paths:
		#    self.log.WriteText('           %s\n' % path)

		# Compare this with the debug above; did we change working dirs?
		# self.log.WriteText("CWD: %s\n" % os.getcwd())

		# Destroy the dialog. Don't do this until you are done with it!
		# BAD things can happen otherwise!
		self.convertSrcFile = paths[0]

		dlg.Destroy()

		self.CreateSrcFileSeries()

	def CreateSrcFileSeries(self):  # wxGlade: MyFrame.<event_handler>

		self.seriesSrcFile = pd.read_csv(self.convertSrcFile)
		print(self.seriesSrcFile.head(3))
		# print(self.seriesSrcFile['Timetag'][1])
		# print(self.seriesSrcFile['Timetag'].dtypes)
		temp = self.seriesSrcFile['Timetag'].diff()
		# print(temp)
		self.seriesSrcFileFinal = self.seriesSrcFile.copy(deep=False)
		self.seriesSrcFileFinal['Delta'] = temp.fillna(0)
		print(self.seriesSrcFileFinal['Delta'].head(3))

		# plt.grid(True)
		# plt.title("Delta-Diagram")
		# plt.xlabel("Sample")
		# plt.ylabel("Delta")
		# plt.savefig('delta.png')


		self.seriesSrcFileFinal['Delta'].plot()

	def LoadDstFileHandler(self, event):  # wxGlade: MyFrame.<event_handler>
		# self.log.WriteText("CWD: %s\n" % os.getcwd())

		# Create the dialog. In this case the current directory is forced as the starting
		# directory for the dialog, and no default file name is forced. This can easilly
		# be changed in your program. This is an 'open' dialog, and allows multitple
		# file selections as well.
		#
		# Finally, if the directory is changed in the process of getting files, this
		# dialog is set up to change the current working directory to the path chosen.
		dlg = wx.FileDialog(
			self, message="Choose a file",
			defaultDir=os.getcwd(),
			defaultFile="",
			# wildcard=wildcardDstFile,
			wildcard=wildcardCsvFile,
			style=wx.FD_OPEN | wx.FD_MULTIPLE |
				  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
				  wx.FD_PREVIEW
		)

		# Show the dialog and retrieve the user response. If it is the OK response,
		# process the data.
		if dlg.ShowModal() == wx.ID_OK:
			# This returns a Python list of files that were selected.
			paths = dlg.GetPaths()

			pass
		# self.log.WriteText('You selected %d files:' % len(paths))

		# for path in paths:
		#    self.log.WriteText('           %s\n' % path)

		# Compare this with the debug above; did we change working dirs?
		# self.log.WriteText("CWD: %s\n" % os.getcwd())

		# Destroy the dialog. Don't do this until you are done with it!
		# BAD things can happen otherwise!
		self.convertDstFile = paths[0]

		dlg.Destroy()
		self.CreateDstFileSeries()

	def CreateDstFileSeries(self):  # wxGlade: MyFrame.<event_handler>
		self.seriesDstFile = pd.read_csv(self.convertDstFile)
		print(self.seriesDstFile.head(3))
		# print(self.seriesDstFile['Timetag'][1])
		# print(self.seriesDstFile['Timetag'].dtypes)
		temp = self.seriesDstFile['Timetag'].diff()
		# print(temp)
		self.seriesDstFileFinal = self.seriesDstFile.copy(deep=False)
		self.seriesDstFileFinal['Delta'] = temp.fillna(0)
		print(self.seriesDstFileFinal['Delta'].head(3))


# end of class DataAnalysisLabFrame

class DataAnalysisLabApp(wx.App):
	def OnInit(self):
		self.Lab = DataAnalysisLabFrame(None, wx.ID_ANY, "")
		self.SetTopWindow(self.Lab)
		self.Lab.Show()
		return True


# end of class DataAnalysisLabApp

if __name__ == "__main__":
	gettext.install("DataAnalysisLab")  # replace with the appropriate catalog name

	DataAnalysisLab = DataAnalysisLabApp(0)
	DataAnalysisLab.MainLoop()
