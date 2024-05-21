#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import sssssss_epy_block_1 as epy_block_1  # embedded python block
import sssssss_epy_block_2 as epy_block_2  # embedded python block
import sssssss_epy_block_2_0 as epy_block_2_0  # embedded python block
import sssssss_epy_block_2_1 as epy_block_2_1  # embedded python block
import sssssss_epy_block_5 as epy_block_5  # embedded python block
import sssssss_epy_block_5_0 as epy_block_5_0  # embedded python block



class sssssss(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "sssssss")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1080000000
        self.mi = mi = 10
        self.fm = fm = 95000
        self.fc = fc = 109400000

        ##################################################
        # Blocks
        ##################################################

        self._mi_range = qtgui.Range((-2), 10, 1, 10, 200)
        self._mi_win = qtgui.RangeWidget(self._mi_range, self.set_mi, "'mi'", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._mi_win)
        self._fm_range = qtgui.Range(10000, 95000, 1500, 95000, 200)
        self._fm_win = qtgui.RangeWidget(self._fm_range, self.set_fm, "'fm'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._fc_range = qtgui.Range(100000000, 109400000, 1000000, 109400000, 200)
        self._fc_win = qtgui.RangeWidget(self._fc_range, self.set_fc, "'fc'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.epy_block_5_0 = epy_block_5_0.blk(gain=1.0)
        self.epy_block_5 = epy_block_5.blk(gain=1.0)
        self.epy_block_2_1 = epy_block_2_1.blk(gain=1.0)
        self.epy_block_2_0 = epy_block_2_0.blk(threshold=1.0)
        self.epy_block_2 = epy_block_2.blk(gain=1.0)
        self.epy_block_1 = epy_block_1.blk(sample_rate=1080000.0, lof=1055000.0)
        self.blocks_throttle2_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(mi)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fc, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fm, 0.5, 0, 0)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(1)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=384000,
        	audio_decim=4,
        	deviation=95000,
        	audio_pass=15000,
        	audio_stop=50000,
        	gain=1,
        	tau=(75e-6),
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.epy_block_5, 0))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.epy_block_2_1, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_throttle2_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_throttle2_1, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.epy_block_1, 0), (self.epy_block_2, 0))
        self.connect((self.epy_block_2, 0), (self.epy_block_2_0, 0))
        self.connect((self.epy_block_2_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.epy_block_2_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.epy_block_2_1, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_5, 0), (self.epy_block_5_0, 0))
        self.connect((self.epy_block_5_0, 0), (self.blocks_throttle2_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sssssss")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_mi(self):
        return self.mi

    def set_mi(self, mi):
        self.mi = mi
        self.blocks_multiply_const_vxx_1.set_k(self.mi)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_sig_source_x_1.set_frequency(self.fc)




def main(top_block_cls=sssssss, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
