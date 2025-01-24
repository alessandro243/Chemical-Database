# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Thalita\\Desktop\\Alessandro\\ProjetoSGM\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('SGM.sqlite3', '.')],
    hiddenimports=['sqlite3', 'PySide6'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='Chemical Database',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Thalita\\Desktop\\Alessandro\\ProjetoSGM\\imagem.ico'],
)
