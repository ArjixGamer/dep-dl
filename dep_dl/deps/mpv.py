from dep_dl import utils
from dep_dl.deps import BaseDep
import sys


class MPV(BaseDep):
    def __init__(self):
        self.arch = utils.os_arch()
        self.folders = [
            {
                "title": x['title'],
                "link": "https://sourceforge.net" + x.find('a', href=True)['href']
            }
            for x in utils.soup(
                utils.get('https://sourceforge.net/projects/mpv-player-windows/files/')).select('tbody > tr')
        ]
        if sys.platform.startswith('darwin'):
            self.os = 'macos'
        elif sys.platform.startswith('win'):
            self.os = 'windows'
        else:
            self.os = 'linux'

    @property
    def is_on_path(self):
        return utils.check_in_path('mpv')

    @property
    def windows(self):
        if self.arch == 32:
            folder = list(
                filter(
                    lambda x: x,
                    [x if '32' in x['title'] else False for x in self.folders]
                ))[0]
        elif self.arch == 64:
            folder = list(
                filter(
                    lambda x: x,
                    [x if '64' in x['title'] else False for x in self.folders]
                ))[0]

        files = utils.get_files_from_folder(folder)
        latest_version = files[0]
        return latest_version

    @property
    def macos(self):
        link = 'https://laboratory.stolendata.net/~djinn/mpv_osx/'
        files = [
            utils.File(
                "https://laboratory.stolendata.net/~djinn/mpv_osx/" +
                x['href'],
                x['href']
            )
            for x in utils.soup(utils.get(link)).select('a[href*="tar.gz"]')
        ]
        # This is the latest version, only supported on Mac OS 10.12 (sierra) and later
        return files[0]
