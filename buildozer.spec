[app]

# (str) Title of your application
title = Mobile Security Toolkit

# (str) Package name
package.name = mobilesecuritytoolkit

# (str) Package domain (needed for android/ios packaging)
package.domain = org.securitytoolkit

# (str) Source files where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,charset-normalizer,certifi,idna

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# (int) Target Android API version
android.api = 30

# (int) Minimum Android API version
android.minapi = 21

# (str) Android NDK version
android.ndk = 23b

# (str) Android SDK version
android.sdk = 30

# (str) Android arch to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Python for android branch
p4a.branch = master

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Android additional libraries
android.android_libs =

# (bool) Android copy libs
android.copy_libs = 1

# (str) Android logcat filter
android.logcat_filters = *:S python:D

# (bool) Copy application libs to content folder
android.copy_app_libs_to_content = 1

# (str) The Android arch name (arm64-v8a, armeabi-v7a)
android.arch = arm64-v8a