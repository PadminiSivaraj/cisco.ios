# -*- coding: utf-8 -*-
# Copyright 2023 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# ansible.content_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the documentation in the module file and re-run
# ansible.content_builder commenting out
# the path to external 'docstring' in build.yaml.
#
##############################################

"""
The arg spec for the ios_evpn_evi module
"""


class Evpn_eviArgs(object):  # pylint: disable=R0903
    """The arg spec for the ios_evpn_evi module"""

    argument_spec = {
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "evi": {"type": "int", "required": True},
                "default_gateway": {
                    "type": "dict",
                    "options": {
                        "advertise": {
                            "type": "dict",
                            "options": {
                                "enable": {"type": "bool"},
                                "disable": {"type": "bool"},
                            },
                        },
                    },
                },
                "ip": {
                    "type": "dict",
                    "options": {
                        "local_learning": {
                            "type": "dict",
                            "options": {
                                "enable": {"type": "bool"},
                                "disable": {"type": "bool"},
                            },
                        },
                    },
                },
                "encapsulation": {
                    "type": "str",
                    "choices": ["vxlan"],
                    "default": "vxlan",
                },
                "replication_type": {
                    "type": "str",
                    "choices": ["ingress", "static"],
                },
                "route_distinguisher": {"type": "str"},
            },
        },
        "state": {
            "type": "str",
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
        },
    }  # pylint: disable=C0301