# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/quentin/Documents/Insta DM bot/main.py'],
             pathex=['/Users/quentin/Documents/Insta DM bot'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='/Users/quentin/Documents/Insta DM bot/insticon.icns')
app = BUNDLE(exe,
             name='InstaBotDm.app',
             icon='/Users/quentin/Documents/Insta DM bot/insticon.icns',
             bundle_identifier=None)
