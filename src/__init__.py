# -*- coding: utf-8 -*-
#########################################################################
# Copyright (C) 2018-2021 by Simone Gaiarin <simgunz@gmail.com>         #
#                                                                       #
# This program is free software; you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation; either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program; if not, see <http://www.gnu.org/licenses/>.  #
#########################################################################
from anki.hooks import wrap
from aqt.editor import Editor


def setBrowserImageMaxDimensions(self):
    config = self.mw.addonManager.getConfig(__name__)
    styleTag = createStyleTag(config['height_or_width'], config['max-width'], config['max-height'])
    self.web.eval(f"""$('head').append('{styleTag}')""")


def createStyleTag(dimension, maxWidth, maxHeight):
    if dimension == "width":
        imgCss = f"max-width: {maxWidth};"
    if dimension == "height":
        imgCss = f"max-height: {maxHeight};"
    elif dimension == "both":
        imgCss = f"max-width: {maxWidth}; max-height: {maxHeight};"
    else:
        print(f"max-image-height: invalid value '{dimension}' for 'height_or_width'")
    return f'<style type="text/css">#fields img{{ {imgCss} }}</style>'


Editor.setupWeb = wrap(Editor.setupWeb, setBrowserImageMaxDimensions)
