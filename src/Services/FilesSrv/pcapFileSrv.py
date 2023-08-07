from typing import Text
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether

from qt_core import *
import pandas as pd
import re
from scapy.all import *
from scapy.utils import rdpcap
from gui.uis.windows.main_window.ui_main import *

file_name = None


def get_url_from_payload(payload):
    http_header_regex = r"(?P<name>.*?): (?P<value>.*?)\r\n"
    start = payload.index(b"GET ") + 4
    end = payload.index(b" HTTP/1.1")
    url_path = payload[start:end].decode("utf8")
    http_header_raw = payload[:payload.index(b"\r\n\r\n") + 2]
    http_header_parsed = dict(re.findall(http_header_regex, http_header_raw.decode("utf8")))
    url = http_header_parsed["Host"] + url_path + "\n"
    return url


def parse_pcap(pcap_path, urls_file):
    pcap_flow = rdpcap(pcap_path)
    sessions = pcap_flow.sessions()
    urls_output = open(urls_file, "wb")
    for session in sessions:
        for packet in sessions[session]:
            try:
                if packet[TCP].dport == 80:
                    payload = bytes(packet[TCP].payload)
                    url = get_url_from_payload(payload)
                    urls_output.write(url.encode())
            except Exception as e:
                pass
    urls_output.close()


def parse_raw_pcap(pcap_path):
    pkts = rdpcap(pcap_path)

    pktDB = pd.DataFrame(pkts)



    for pkt in pkts:
        #pkt[Ether].src = new_src_mac  # i.e new_src_mac="00:11:22:33:44:55"
        #pkt[Ether].dst = new_dst_mac
        #pkt[IP].src = new_src_ip  # i.e new_src_ip="255.255.255.255"
        #pkt[IP].dst = new_dst_ip
        sendp(pkt,iface="mirror")  # sending packet at layer 2

class pcapFilesSrv():
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui()

    def new(self):
        global file_name

        self.ui.load_pages.text_edit.setPlainText("")
        self.ui.title_bar.set_title("New file")
        file_name = None

    def load(self):
        global file_name

        dlg_file = QFileDialog.getOpenFileName(
            parent=self,
            caption=self.tr("Select a file"),
            filter=self.tr("Pcap files (*.pcap)")
        )

        if dlg_file:
            #file = open(dlg_file[0], encoding="utf 8")
            #text = file.read()
            #file.close()
            file_name = dlg_file[0]
            parse_raw_pcap(file_name)

            #self.ui.load_pages.text_edit.setPlainText(text)
            #file_name = dlg_file[0]
            self.ui.title_bar.set_title(file_name)



    def save(self):
        global file_name

        def write_text(self, file):
            print("saved in folder:" + file)
            file = open(file, "w")
            file.write(self.ui.load_pages.text_edit.toPlainText())

        if file_name:
            write_text(self, file_name)
            self.ui.title_bar.set_title(file_name)
        else:
            dlg_file = QFileDialog.getSaveFileName(
                parent=self,
                caption=self.tr("Select a file"),
                filter=self.tr("Pcap files (*.pcap)")
            )

            if dlg_file:
                write_text(self, dlg_file[0])

                file_name = dlg_file[0]
                self.ui.title_bar.set_title(file_name)

