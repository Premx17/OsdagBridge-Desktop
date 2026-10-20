
def test_desktop_imports():
    """Verify that the desktop module can be imported cleanly."""
    import osdagbridge_desktop
    from osdagbridge_desktop.ui.template_page import CustomWindow
    from osdagbridge_desktop.ui.widgets.section_viewer import DB_PATH
    from osdagbridge_desktop.ui.widgets.native_map import _DATA_DIR

    assert DB_PATH.exists()
    assert _DATA_DIR.exists()
