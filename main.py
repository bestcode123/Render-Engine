class RenderImage:
    def __init__(self, mesh_res, rendray_res):
        self.mesh_res = mesh_res
        self.render_res, self.ray_res = rendray_res
    def prereq_test(self):
        return [self.mesh_res, self.render_res, self.ray_res]
    def __version__(self):
        return '0.0.1a'
    def mesh_point_calc(self, indata, closest_num):
        self.indata = indata
        in2 = indata
        out = []

        for j in range(closest_num):
            min = in2[0][2]
            min2 = in2[0]
            for i in range(len(in2)):
                if(in2[i][1] < min):
                    min = in2[i][2]
                    min2 = in2[i]
            in2.remove(min2)
            out.append(min2)
        return out

co = [[1, 5, 0], [4, 5, 0], [3, 2, 1], [3, 3, 1], [1, 1, 0], [4, 1, 0]]
root = RenderImage(1, (len(co), len(co)))
print(root.mesh_point_calc(co, 4))
