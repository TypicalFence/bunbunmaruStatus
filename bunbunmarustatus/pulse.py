import pulsectl
from .module import Module


class PulseAudio(Module):
    def __init__(self):
        super().__init__()
        self.pulse = pulsectl.Pulse()
        self.sink_name = self.pulse.server_info().default_sink_name

    def _locate_default_sink(self):
        sinks = self.pulse.sink_list()
        results = filter(lambda x: x.name == self.sink_name, sinks)
        # filter objects in python are annoying
        results = list(results)

        if len(results) != 0:
            return results[0]

        return None

    def get_block(self):
        sink = self._locate_default_sink()

        if sink is None:
            return {"full_text": "no audio"}

        volume = sink.volume.value_flat * 100
        if sink.mute == 0:
            text = str(volume).split(".")[0] + "%"
        else:
            text = "muted"

        return {"full_text": text}

    @staticmethod
    def get_name():
        return "pulse"
