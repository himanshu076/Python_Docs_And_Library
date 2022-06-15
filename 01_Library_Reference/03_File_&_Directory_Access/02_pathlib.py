
# *This is the library that is used to get the path.....
from pathlib import Path, PurePath, PureWindowsPath, PurePosixPath
import os
from traceback import print_tb


# Listing Subdirectories: - shown all directories present in this path.
# p = Path('.')
# s = [x for x in p.iterdir() if x.is_dir()]
# print(s)

# **************************************************************************************************

# Listing Python source files in this directory tree: - shown all fileas available in this directories...
# d = list(p.glob('**/*.py'))
# print(d)

# **************************************************************************************************
# Navigating inside a directory tree:
# p = Path('/01_Library_Reference')
# q = p / '01_Numeric and Mathematical Modules' / '01_random_Module.py'
# print(q)
# q.resolve()
# print(q)

# *************************************************************************************************
# q.exists()
# print(q)
# q.is_dir()
# print(q)

# *************************************************************************************************

# # Opening a file:
# with q.open() as f: f.readline()

# s = PurePath('main.py')
# print(s)

# **************************************************************************************************
# s = PurePath('foo', 'some/path', 'bar')
# print(s)
# d = PurePath(Path('foo'), Path('path'))
# print(d)

# **************************************************************************************************
# s = PurePath()
# print(s)

# **************************************************************************************************
# s = PurePath('/etc', '/usr', 'lib64')
# print(s)
# d = PureWindowsPath('c:/Windows', 'd:bar')
# print(d)

# **************************************************************************************************
# s = PureWindowsPath('c:/Windows', '/Program Files')
# print(s)

# **************************************************************************************************
# s = PurePath('foo//bar')
# print(s)
# a = PurePath('//foo/bar')
# print(a)
# d = PurePath('foo/./bar')
# print(d)
# e = PurePath('foo/../bar')
# print(e)

# **************************************************************************************************
# s = PurePosixPath('/etc')
# print(s)

# **************************************************************************************************
# s = PureWindowsPath('c:/Program Files/')
# print(s)

# **************************************************************************************************
# d = PureWindowsPath('//server/share/file')
# print(d)

# **************************************************************************************************
# r = PurePosixPath('foo') == PurePosixPath('FOO')
# print(r)
# q = PureWindowsPath('foo') == PureWindowsPath('FOO')
# print(q)
# y = PureWindowsPath('FOO') in { PureWindowsPath('foo') }
# print(y)
# t = PureWindowsPath('C:') < PureWindowsPath('d:')
# print(t)

# **************************************************************************************************
# d = PureWindowsPath('foo') == PurePosixPath('foo')
# print(d)
# s = PureWindowsPath('foo') < PurePosixPath('foo')
# print(s)

# **************************************************************************************************
# p = PurePath('/etc')
# print(p)
# t = os.fspath(p)
# print(t)

# **************************************************************************************************
# p = PurePath('/usr/bin/python3')
# print(p.parts)

# **************************************************************************************************
# p = PureWindowsPath('c:/Program Files/PSF')
# print(p.parts)eWindowsPath('c:/Program Files/').root
# print(s

# **************************************************************************************************
# s = PureWindowsPath('c:/Program Files/').drive
# print(s)

# **************************************************************************************************
# s = PureWindowsPath('/Program Files/').drive
# print(s)

# **************************************************************************************************
# f = PurePosixPath('/etc').drive
# print(f)

# **************************************************************************************************
# d = PureWindowsPath('//host/share/foo.txt').drive
# print(d)

# **************************************************************************************************
# s = PureWindowsPath('c:/Program Files/').root
# print(s)
# e = PureWindowsPath('c:Program Files/').root
# print(e)
# t = PurePosixPath('/etc').root
# print(t)

# **************************************************************************************************
# s = PureWindowsPath('//host/share').root
# print(s)

# **************************************************************************************************
# d = PureWindowsPath('c:/Program Files/').anchor
# print(d)
# e = PureWindowsPath('c:Program Files/').anchor
# print(e)
# s = PurePosixPath('/etc').anchor
# print(s)
# r = PureWindowsPath('//host/share').anchor
# print(r)

# **************************************************************************************************
# p = Path(__file__).resolve().parent.parent
# print(p)

# **************************************************************************************************
# **************************************************************************************************
# **************************************************************************************************
# **************************************************************************************************