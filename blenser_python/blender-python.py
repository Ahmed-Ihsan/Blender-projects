import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ahmed Ihsan"
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="blender_python", icon= "CUBE")
        
        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)

if __name__=="__main__":
    register()