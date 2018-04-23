import ui
import bpy

bl_info = {
    "name": "Material Painter",
    "author": "Antonio Aloisio",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "3D View > Tool Shelve > Mixamo Tab",
    "description": ("Experimental PBR Material painter"),
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/gnuton/MaterialPainter/wiki",
    "tracker_url": "https://github.com/enziop/MaterialPainter/issues",
    "category": "Texturing"
}

def trigger_reload(mod, l = locals()):
    from importlib import reload

    print("Reloading ", mod.__name__)
    if ui.__name__ not in l:
        return

    try:
        mod.unregister()
    except AttributeError as e:
        print("Unable to unregister error:", e)
    reload(mod)
    mod.reload()

if bpy.__name__ in locals():
    modules = [ui]
    [trigger_reload(module) for module in modules]

if __name__ == "__main__":

    print("Loading Material Painter.")
    ui.register()
