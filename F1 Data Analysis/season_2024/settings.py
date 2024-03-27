# CACHE_FOLDER_PATH = r'C:\Users\ricca\OneDrive - ZHAW\Dokumente\f1_cache'


import platform

# Check the system platform
if platform.system() == 'Windows':
    CACHE_FOLDER_PATH = r'C:\Users\ricca\OneDrive - ZHAW\Dokumente\f1_cache'
elif platform.system() == 'Darwin':  # 'Darwin' is the platform name for macOS
    CACHE_FOLDER_PATH = '/Users/riccardoviscio1/Desktop/Projects/F1 Data Analysis/season_2024/f1_cache'
else:
    # You may add handling for other platforms if needed
    raise NotImplementedError("Platform not supported")

print("CACHE_FOLDER_PATH:", CACHE_FOLDER_PATH)
