from bs4 import BeautifulSoup
from click.utils import get_app_dir
import shutil
import subprocess
import os
import requests


class File:
    def __init__(self, link, title):
        self.link = link
        self.title = title

    def __repr__(self) -> str:
        return str({"link": self.link, 'title': self.title})


def get_app_directory():
    folder = get_app_dir('dep-dl')
    if not os.path.isdir(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            print(e)
    return folder


def os_arch():
    os_arch = '32-bit'
    if os.name == 'nt':
        output = subprocess.check_output(
            ['wmic', 'os', 'get', 'OSArchitecture'])
        os_arch = 64 if '64' in output.split()[1].decode("utf-8") else 32
    else:
        output = subprocess.check_output(['uname', '-m']).decode("utf-8")
        if 'x86_64' in output:
            os_arch = 64
        else:
            os_arch = 32
    return os_arch


def check_in_path(app):
    """
    Checks to see if the given app exists on the path
    :param app: app name to look for
    :return: true if the app exists, false otherwise
    """
    return shutil.which(app) is not None


def get(link):
    return requests.get(link).text


def soup(html):
    return BeautifulSoup(html, 'html.parser')


def get_files_from_folder(folder):
    """
         input > :folder: A SourceForge dict for a folder in a project.
        output > [:File:]

        example return: [
            File,
            File
            File
        ]
    """
    tmp_soup = soup(get(folder['link']))
    results = tmp_soup.select('tbody > tr.file')
    return [
        File(
            x.find('a')['href'].replace("sourceforge.net/projects/",
                                        "master.dl.sourceforge.net/project/").replace("/files/", "/").replace('/download', ""),
            x['title']
        )
        for x in results
    ]


def toFloat(value, fallback=0.0):
    try:
        return float(value)
    except ValueError:
        return fallback
