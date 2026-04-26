[app]

title = My Kivy App
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 0.1

requirements = python3,kivy

# Android settings (IMPORTANT)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Entry point
entrypoint = main.py

# (optional but safer)
presplash_color = #FFFFFF

[buildozer]

log_level = 2
warn_on_root = 1
