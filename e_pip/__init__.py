# from __future__ import print_function # Python 2.x
import subprocess
# import argparse


def execute(cmd):
    popen = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, universal_newlines=True)
    stdout_lines = iter(popen.stdout.readline, "")
    for stdout_line in stdout_lines:
        print(stdout_line)

    popen.stdout.close()
    return_code = popen.wait()
    if return_code != 0:
        raise subprocess.CalledProcessError(return_code, cmd)
    return return_code


import os
import sys
import posixpath

import click


class Project(object):

    def __init__(self, **kwargs):
        self.virtual_env = self.in_a_virtual_environment()
        if 'virtual_environment' in kwargs:
            self.virtual_env = kwargs['virtual_environment']

    def get_python_version(self, major_version=False):
        """Returns the major python version"""
        version = sys.version_info
        if major_version:
            return version.major
        return "%s.%s" % (version.major, version.minor)

    def in_a_virtual_environment(self):
        if hasattr(sys, 'real_prefix'):
            return True
        return False

    def get_virtual_env_name(self):
        if self.in_a_virtual_environment():
            return sys.prefix.split('/')[-1]
        return None

    def has_virtualenv_folder(self):
        cwd = os.getcwd()
        venv = os.path.join(cwd, 'venv')
        return os.path.exists(venv)

    def is_windows(self):
        return os.name != 'posix'

    def has_virtualenv(self):
        try:
            import virtualenv
            return True
        except ImportError:
            return False

    def create_virtual_environment(self):
        if not self.has_virtualenv_folder():
            python_version = self.get_python_version(major_version=True)
            if python_version == 3:
                your_command = ['python', '-m', 'venv', 'venv']
                output = subprocess.call(your_command)
            else:
                if not self.has_virtualenv():
                    your_command = ['python', '-m',
                                    'pip', 'install', 'virtualenv']
                    output = execute(your_command)
                output = execute(['virtualenv', 'venv'])
        return output

    def activate_virtual_environment(self):
        if self.has_virtualenv_folder():
            if self.is_windows():
                cwd = os.path.join(os.getcwd(),'venv','Script','activate.bat')
            else:
                cwd = os.path.join(os.getcwd(),'venv','bin','activate')
                output = subprocess.call(['chmod', '+x', cwd])
            # os.system('/bin/bash  --rcfile %s' % cwd)
            output = subprocess.call(['%s' % cwd], shell=True)
        return output


class Repo(object):

    def __init__(self, home):
        self.home = home
        self.config = {}
        self.verbose = False

    def set_config(self, key, value):
        self.config[key] = value
        if self.verbose:
            click.echo('  config[%s] = %s' % (key, value), file=sys.stderr)

    def __repr__(self):
        return '<Repo %r>' % self.home


pass_repo = click.make_pass_decorator(Repo)


# @click.group()
# @click.option('--repo-home', envvar='REPO_HOME', default='.repo',
#               metavar='PATH', help='Changes the repository folder location.')
# @click.option('--config', nargs=2, multiple=True,
#               metavar='KEY VALUE', help='Overrides a config key/value pair.')
# @click.option('--verbose', '-v', is_flag=True,
#               help='Enables verbose mode.')
# @click.version_option('1.0')
# @click.pass_context
# def cli(ctx, repo_home, config, verbose):
#     """Repo is a command line tool that showcases how to build complex
#     command line interfaces with Click.
#     This tool is supposed to look like a distributed version control
#     system to show how something like this can be structured.
#     """
#     # Create a repo object and remember it as as the context object.  From
#     # this point onwards other commands can refer to it by using the
#     # @pass_repo decorator.
#     ctx.obj = Repo(os.path.abspath(repo_home))
#     ctx.obj.verbose = verbose
#     for key, value in config:
#         ctx.obj.set_config(key, value)

@click.group()
def cli():
    pass

@cli.command()
def activate():
    pass

@cli.command()
def init():
    pass


@cli.command()
def install():
    pass


@cli.command()
def uninstall():
    pass


@cli.command()
def generate():
    pass

# @cli.command()
# @click.argument('src')
# @click.argument('dest', required=False)
# @click.option('--shallow/--deep', default=False,
#               help='Makes a checkout shallow or deep.  Deep by default.')
# @click.option('--rev', '-r', default='HEAD',
#               help='Clone a specific revision instead of HEAD.')
# @pass_repo
# def clone(repo, src, dest, shallow, rev):
#     """Clones a repository.
#     This will clone the repository at SRC into the folder DEST.  If DEST
#     is not provided this will automatically use the last path component
#     of SRC and create that folder.
#     """
#     if dest is None:
#         dest = posixpath.split(src)[-1] or '.'
#     click.echo('Cloning repo %s to %s' % (src, os.path.abspath(dest)))
#     repo.home = dest
#     if shallow:
#         click.echo('Making shallow checkout')
#     click.echo('Checking out revision %s' % rev)


# @cli.command()
# @click.confirmation_option()
# @pass_repo
# def delete(repo):
#     """Deletes a repository.
#     This will throw away the current repository.
#     """
#     click.echo('Destroying repo %s' % repo.home)
#     click.echo('Deleted!')


# @cli.command()
# @click.option('--username', prompt=True,
#               help='The developer\'s shown username.')
# @click.option('--email', prompt='E-Mail',
#               help='The developer\'s email address')
# @click.password_option(help='The login password.')
# @pass_repo
# def setuser(repo, username, email, password):
#     """Sets the user credentials.
#     This will override the current user config.
#     """
#     repo.set_config('username', username)
#     repo.set_config('email', email)
#     repo.set_config('password', '*' * len(password))
#     click.echo('Changed credentials.')


# @cli.command()
# @click.option('--message', '-m', multiple=True,
#               help='The commit message.  If provided multiple times each '
#               'argument gets converted into a new line.')
# @click.argument('files', nargs=-1, type=click.Path())
# @pass_repo
# def commit(repo, files, message):
#     """Commits outstanding changes.
#     Commit changes to the given files into the repository.  You will need to
#     "repo push" to push up your changes to other repositories.
#     If a list of files is omitted, all changes reported by "repo status"
#     will be committed.
#     """
#     if not message:
#         marker = '# Files to be committed:'
#         hint = ['', '', marker, '#']
#         for file in files:
#             hint.append('#   U %s' % file)
#         message = click.edit('\n'.join(hint))
#         if message is None:
#             click.echo('Aborted!')
#             return
#         msg = message.split(marker)[0].rstrip()
#         if not msg:
#             click.echo('Aborted! Empty commit message')
#             return
#     else:
#         msg = '\n'.join(message)
#     click.echo('Files to be committed: %s' % (files,))
#     click.echo('Commit message:\n' + msg)


# @cli.command(short_help='Copies files.')
# @click.option('--force', is_flag=True,
#               help='forcibly copy over an existing managed file')
# @click.argument('src', nargs=-1, type=click.Path())
# @click.argument('dst', type=click.Path())
# @pass_repo
# def copy(repo, src, dst, force):
#     """Copies one or multiple files to a new location.  This copies all
#     files from SRC to DST.
#     """
#     for fn in src:
#         click.echo('Copy from %s -> %s' % (fn, dst))
