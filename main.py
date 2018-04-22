# -*- coding: utf-8 -*-

import os

from kivy.config import Config
# 0 being off 1 being on as in true/false
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'multisamples', '0')

import kivy

kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker


class PiPy(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "BlueGrey"
    theme_cls.accent_palette = "LightBlue"
    
    previous_date = ObjectProperty()
    title = "PiPy"
    
    def build(self):
        pass


def main():
    PiPy().run()


if __name__ == "__main__":
    main()