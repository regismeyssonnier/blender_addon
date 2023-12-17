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
    
class MyOpSetOrigGeo(bpy.types.Operator):
    bl_idname='myops.set_orig_to_geo'
    bl_label = 'Set Origin to Geometry'
    
    
    def execute(self, context):
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

        return{'FINISHED'}
    
class MyOpDuplicateSel(bpy.types.Operator):
    bl_idname='myops.duplicate_sel'
    bl_label = 'Duplicate Selection'
    
    
    def execute(self, context):
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
        bpy.ops.mesh.separate(type='SELECTED')

        return{'FINISHED'}
    
class MyOpDuplicateObject(bpy.types.Operator):
    bl_idname='myops.duplicate_obj'
    bl_label = 'Duplicate Object'
    
    
    def execute(self, context):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
        
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
            
        layout.row().operator("myops.add_point", icon='VERTEXSEL', text="Add Point")
      
        layout.row().operator("myops.set_orig_to_geo", icon='WORLD', text="Set origin to geometry")
      
        layout.row().operator("mesh.fill_grid", icon="GRID", text="Grid Fill")
        
        if 'EDIT' in bpy.context.mode:
            layout.row().operator("myops.duplicate_sel", icon="DUPLICATE", text="Duplicate Selection")
        
        layout.row().operator("myops.duplicate_obj", icon="DUPLICATE", text="Duplicate Object")
                
        
def register():
    bpy.utils.register_class(PanelRM)
    bpy.utils.register_class(PanelRMModifier)
    bpy.utils.register_class(PanelRMAction)
    
    bpy.utils.register_class(MyOpSubdSol)
    bpy.utils.register_class(MyOpAddPoint)
    bpy.utils.register_class(MyOpSetOrigGeo)
    bpy.utils.register_class(MyOpDuplicateSel) 
    bpy.utils.register_class(MyOpDuplicateObject) 
    
def unregister():
    bpy.utils.unregister_class(PanelRM)
    bpy.utils.unregister_class(PanelRMModifier)
    bpy.utils.unregister_class(PanelRMAction)
    
    bpy.utils.unregister_class(MyOpSubdSol)
    bpy.utils.unregister_class(MyOpAddPoint)
    bpy.utils.unregister_class(MyOpSetOrigGeo)
    bpy.utils.unregister_class(MyOpDuplicateSel) 
    bpy.utils.unregister_class(MyOpDuplicateObject) 
    

if __name__ == "__main__":
    register()
    