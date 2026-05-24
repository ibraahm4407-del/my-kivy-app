[app]

title = My Kivy App

package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Android settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# IMPORTANT FIX
android.sdk_path = /usr/local/lib/android/sdk

android.accept_sdk_license = True
android.skip_update = True

[buildozer]

log_level = 2
warn_on_root = 1
