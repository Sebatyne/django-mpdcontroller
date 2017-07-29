import subprocess

from django.conf import settings

class MpdController():
    def __init__(self):
        self.base_command = ["mpc", "--host", settings.MPD_HOST_URL]

    def _is_valid_mpd_command(self, command):
        return command in [
            'next',
            'pause',
            'play',
            'prev',
            'stop',
            'toggle',
        ]

    def _is_special_command(self, command):
        return command in [
            'status',
        ]

    def status(self):
        process = subprocess.run(self.base_command, stdout=subprocess.PIPE)
        output = process.stdout.decode('utf-8').split('\n')[0]
        artist, song = output.split(' - ')
        return {'artist': artist, 'song': song} 

    def run(self, command, **kw):
        if self._is_valid_mpd_command(command):
            process = subprocess.run(self.base_command + [command], stdout=subprocess.PIPE)
            result_dict = {'result': process.returncode}
        elif self._is_special_command(command):
            result_dict = getattr(self, command)()
        return result_dict
