__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# fuctions here
from os.path import abspath, exists, isdir, isfile
from os import mkdir
from shutil import rmtree
from zipfile import ZipFile
from glob import glob
from fileinput import input


def clean_cache():

    CACHE = abspath('./cache')

    if exists(CACHE) and isdir(CACHE):
        try:
            rmtree(CACHE)  # a compact way of clearing the cache
        except OSError:
            print(f'Unable to delete directory: {CACHE}')

    try:
        mkdir(CACHE)
        if exists(CACHE) and isdir(CACHE):
            return CACHE  # cache path string
        return ''  # empty (tring
    except OSError:
        print(f'Unable to make directory: {CACHE}')


def cache_zip(zip_path, cache_path):
    if exists(zip_path) and isfile(zip_path):
        clean_cache()  # extract into a clean cache folder
        if exists(cache_path) and isdir(cache_path):
            with ZipFile(zip_path, 'r') as obj:
                obj.extractall(cache_path)
            return True
    return False


def cached_files():

    CACHE = abspath('./cache')

    if exists(CACHE) and isdir(CACHE):
        files = glob(CACHE + '/*.txt', recursive=False)  # a sea of text files
        files = [f for f in files if isfile(f)]  # files only
        return files  # a list of files
    return []  # an empty list when there are no files


def find_password(cached_files):

    needle = 'password: '

    with input(cached_files) as f:
        for line in f:
            position = line.find(needle)
            if(position >= 0):
                return line[position + len(needle):-1]  # without newline
    return ''  # an empty string when not found


if __name__ == '__main__':

    # calls here
    cache = clean_cache()
    zipfile = abspath('./data.zip')

    cache_zip(zipfile, cache)
    files = cached_files()

    password = find_password(files)
    print(password)

    cache = clean_cache()
