# SPDX-License-Identifier: GPL-3.0-or-later
from af2lfs.domain import F2LFSDomain
from af2lfs.highlighting import F2LFSShellSessionLexer
from af2lfs.builder import setup as setup_builder

def setup(app):
    app.add_domain(F2LFSDomain)
    app.add_lexer('f2lfs-shell-session', F2LFSShellSessionLexer)
    setup_builder(app)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_save': True
    }
