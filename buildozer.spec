[app]
# (str) Title of your application
title = UDFViewer
# (str) Package name
package.name = udfviewer
# (str) Package domain (needed for android/ios packaging)
package.domain = org.example
# (str) Source code where the main.py lives
source.dir = .
# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas
# (list) Source files to exclude (leave empty to not exclude anything)
#source.exclude_exts = spec
# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png
# (list) List of directory to exclude (leave empty to not exclude anything)
#source.exclude_dirs = tests, bin
# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg
# (str) Application versioning (method 1)
version = 0.1
# (str) Application versioning (method 2)
# version.regex = __version__ = '\"['\"]
# version.filename = %(source.dir)s/main.py
# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy
# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy
# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png
# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png
# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait
# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# OSX Specific
# 
# author = © Copyright Info
# 
# Kivy version to use
osx.kivy_version = 1.9.1

# Android specific
# 
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0
# (string) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF
# (list) Permissions
#android.permissions = INTERNET

# iOS specific
# 
# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# (str) Kivy version to use
#ios.kivy_version = 1.9.1
