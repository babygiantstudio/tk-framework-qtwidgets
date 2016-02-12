# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Widget that represents the value of a url_template field in Shotgun
"""
from .label_base_widget import LabelBaseWidget
from .widget_metaclass import ShotgunFieldMeta


class UrlTemplateWidget(LabelBaseWidget):
    """
    Inherited from a :class:`~LabelBaseWidget`, this class is able to
    display a url_template field value as returned by the Shotgun API.
    """
    __metaclass__ = ShotgunFieldMeta
    _FIELD_TYPE = "url_template"

    def _string_value(self, value):
        """
        Convert the Shotgun value for this field into a string

        :param value: The value to convert into a string
        :type value: A URL String
        """
        return "<a href='%s'>%s</a>" % (value, value)
