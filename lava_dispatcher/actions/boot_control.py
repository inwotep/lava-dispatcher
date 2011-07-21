#!/usr/bin/python

# Copyright (C) 2011 Linaro Limited
#
# Author: Paul Larson <paul.larson@linaro.org>
#
# This file is part of LAVA Dispatcher.
#
# LAVA Dispatcher is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# LAVA Dispatcher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along
# with this program; if not, see <http://www.gnu.org/licenses>.

from lava_dispatcher.actions import BaseAction, BaseAndroidAction

class cmd_boot_linaro_android_image(BaseAndroidAction):
    """ Call client code to boot to the master image
    """
    def run(self):
        #Workaround for commands coming too quickly at this point
        client = self.client
        client.proc.sendline("")
        client.boot_linaro_android_image()

class cmd_boot_linaro_image(BaseAction):
    """ Call client code to boot to the master image
    """
    def run(self):
        client = self.client
        #Workaround for commands coming too quickly at this point
        client.proc.sendline("")
        status = 'pass'
        try:
            client.boot_linaro_image()
        except:
            status = 'fail'
            raise
        finally:
            self.context.test_data.add_result("boot_image", status)

class cmd_boot_master_image(BaseAction):
    """ Call client code to boot to the master image
    """
    def run(self):
        client = self.client
        client.boot_master_image()