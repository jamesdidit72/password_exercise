# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['password_exercise/password_functions.py'],
             pathex=['/home/kali/cyberspace/password_exercise/dist/password_functions'],
             binaries=[],
             datas=[('password_exercise/passtext.txt', '.'), ('password_exercise/password.txt', '.')],
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
          [],
          exclude_binaries=True,
          name='password_functions',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='password_functions')
