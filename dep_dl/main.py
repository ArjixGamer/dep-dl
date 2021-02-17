from dep_dl.deps.mpv import MPV
from dep_dl.utils import get_app_directory


get_app_directory()
'''
    Ensures the app has a directory it can save files into.
'''


'''
    Here will be the tests,
    For now they are basically prints of the latest versions found.
'''


"""  MPV  """

mpv = MPV()
print(mpv.windows)
print(mpv.macos)

"""  MPV  """

# ================
