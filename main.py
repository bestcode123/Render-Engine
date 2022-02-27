class RenderImage:
    def __init__(self, mesh_res, rendray_res):
        self.mesh_res = mesh_res
        self.render_res, self.ray_res = rendray_res
    def prereq_test(self):
        return [self.mesh_res, self.render_res, self.ray_res]
    def __version__(self):
        return '0.0.1a'
    
print(RenderImage(1, (6, 6)))