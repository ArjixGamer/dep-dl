from dep_dl import utils


class BaseDep:
    def __init__(self):
        pass

    @property
    def is_on_path(self):
        return False

    @property
    def windows(self):
        return 'link-for-windows-exe or zip'

    @property
    def linux(self):
        return 'link-for-linux-executable-or-zip'

    @property
    def macos(self):
        return 'link-for-MacOS-executable-or-zip'
