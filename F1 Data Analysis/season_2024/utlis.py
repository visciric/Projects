import os
import fastf1 as ff1

def setup_cache(path):
    cache_folder = 'cache'
    cache_folder_path = os.path.join(path, cache_folder)

    if not os.path.exists(cache_folder_path):
        os.makedirs(cache_folder_path)

    ff1.Cache.enable_cache(cache_folder_path)
