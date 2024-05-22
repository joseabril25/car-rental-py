# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('database/*', 'database'),
        ('ui/*', 'ui'),
        ('constants/*', 'constants'),
        ('models/*', 'models'),
        ('managers/*', 'managers'),
        ('factories/*', 'factories'),
        ('services/*', 'services'),
        ('utils/*', 'utils'),
        ('states/*', 'states'),
        ],
    hiddenimports=[
        'sqlalchemy',
        'prettytable',
        'sqlalchemy.ext.declarative',
        'sqlalchemy.orm',
        'bcrypt',
        'datetime',
        're'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='car_rental_system',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
