# -*- coding: utf8 -*-
import difflib
from sys import stdout

from sqlibrist.helpers import get_last_schema, get_current_schema, \
    compare_schemas


def diff(verbose):
    last_schema = get_last_schema()

    current_schema = get_current_schema()

    added, removed, changed = compare_schemas(last_schema, current_schema)

    if any((added, removed, changed)):
        if added:
            stdout.write(u'New items:\n')
            for item in added:
                stdout.write(u'  %s\n' % item)

        if removed:
            stdout.write(u'Removed items:\n')
            for item in removed:
                stdout.write(u'  %s\n' % item)

        if changed:
            stdout.write(u'Changed items:\n')
            for item in changed:
                stdout.write(u'  %s\n' % item)
                if verbose:
                    _diff = difflib.unified_diff(last_schema[item]['up'],
                                                 current_schema[item]['up'])
                    stdout.write('\n'.join(_diff))
                    stdout.write('\n')

    else:
        stdout.write(u'No changes\n')


def diff_command(args):
    return diff(verbose=args.verbose)
