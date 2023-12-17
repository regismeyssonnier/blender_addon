bl_info = {
    "name": "Addon RM",
    "author": "Régis Meyssonnier",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > RM addon",
    "description": "Manage some shortcut",
    "warning": "",
    "doc_url": "",
    "category": "Managing",
}

import bpy

class MyOpSubdSol(bpy.types.Operator):
    bl_idname='myops.add_subdsolid'
    bl_label = 'Subdiv&Solid'
    
    
    def execute(self, context):
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        return{'FINISHED'}
    
class MyOpAddPoint(bpy.types.Operator):
    bl_idname='myops.add_point'
    bl_label = 'Add Point'
    
    
    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.merge(type='COLLAPSE')
        bpy.ops.object.editmode_toggle()


        return{'FINISHED'}
    
    
class PanelRM(bpy.types.Panel):
    bl_label = "RM addon"
    bl_idname = "RM_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RM addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Choose your action:", icon='QUESTION')
    
    
class PanelRMModifier(bpy.types.Panel):
    bl_label = "Modifier Action"
    bl_idname = "RM_Panel_Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RM addon'
    bl_parent_id = 'RM_Panel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
             
        row = layout.row()
        row.operator("object.modifier_add", icon='MODIFIER', text="Subdivision").type='SUBSURF'
        
        row = layout.row()
        row.operator("object.modifier_add", icon='MODIFIER', text="Solidify").type='SOLIDIFY'
        
        row = layout.row()
        row.operator("myops.add_subdsolid", icon='MODIFIER', text="Subd&Solid")
        
        row = layout.row()
        mirror = row.operator("object.modifier_add", icon='MODIFIER', text="Mirror")
        mirror.type = 'MIRROR'
        
class PanelRMAction(bpy.types.Panel):
    bl_label = "Action"
    bl_idname = "RM_Action"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RM addon'
    bl_parent_id = 'RM_Panel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
            
        row = layout.row()
        row.operator("myops.add_point", icon='VERTEXSEL', text="Add Point")
      
        
        
def register():
    bpy.utils.register_class(PanelRM)
    bpy.utils.register_class(PanelRMModifier)
    bpy.utils.register_class(PanelRMAction)
    bpy.utils.register_class(MyOpSubdSol)
    bpy.utils.register_class(MyOpAddPoint)
    
def unregister():
    bpy.utils.unregister_class(PanelRM)
    bpy.utils.unregister_class(PanelRMModifier)
    bpy.utils.unregister_class(PanelRMAction)
    bpy.utils.unregister_class(MyOpSubdSol)
    bpy.utils.unregister_class(MyOpAddPoint)
    

if __name__ == "__main__":
    register()
    