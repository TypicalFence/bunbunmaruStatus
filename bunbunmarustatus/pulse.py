import pulsectl
from .module import Module

class PulseAudio(Module):
    def __init__(self):
        super().__init__()
        self.pulse = pulsectl.Pulse()

    def get_block(self):
        sink = self.pulse.sink_list()[0]
        volume = sink.volume.value_flat * 100
        if sink.mute == 1:
            text = str(volume).split(".")[0] + "%"
        else: 
            text = "muted"

        return {"full_text": text}
    
    def get_name(self):
        return "pulse"