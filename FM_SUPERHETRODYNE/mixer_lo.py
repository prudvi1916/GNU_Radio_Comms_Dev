"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, sample_rate=1.08e6,lof=1055e3):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='mixer_lo',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.lof= lof
        self.sample_rate = sample_rate
        self.ry =0.0

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        input_signal = input_items[0]
        time = np.arange(len(input_signal))
        lo_signal = np.cos(2*np.pi*self.lof*time/self.sample_rate)
        output_items[0][:] = input_signal * lo_signal
        return len(output_items[0])
