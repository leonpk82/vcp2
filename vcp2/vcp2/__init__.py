#!/usr/bin/env python

"""Main entry point for vcp2.

This module contains the code necessary to be able to launch QControl
directly from the command line, without using qtpyvcp. It handles
parsing command line args and starting the main application.

Example:
    Assuming the dir this file is located in is on the PATH, you can
    launch vcp2 by saying::

        $ vcp2 --ini=/path/to/config.ini [options ...]

    Run with the --help option to print a full list of options.

"""

__version__ = '0.0.1'

import os
import qtpyvcp

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'config.yml')


def main(opts=None):

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(vcp_cmd='vcp2',
                          vcp_name='vcp2',
                          vcp_version=__version__)

    qtpyvcp.run_vcp(opts, VCP_CONFIG_FILE)


if __name__ == '__main__':
    main()
