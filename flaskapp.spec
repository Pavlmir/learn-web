# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['flaskapp.py'],
             pathex=['C:\\Users\\pavlm\\PycharmProjects\\learn_web'],
             binaries=[],
              datas=[('.\\webapp\\*', '.'),
             ('.\\webapp\\static\\', 'static'),
             ('.\\webapp\\templates\\', 'templates'),
             ('mainwindow.ui', '.')],
             hiddenimports=['PySide2.QtXml'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='flaskapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
