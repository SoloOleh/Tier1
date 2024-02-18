# import shutil

# archive_name = shutil.make_archive('backup', 'zip', '/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/')

# import shutil

# archive_name = shutil.make_archive('backup', 'zip', '/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')

import shutil

for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))


