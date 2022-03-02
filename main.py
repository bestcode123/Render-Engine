class RenderImage:
    def __init__(self, mesh_res, rendray_res):
        self.mesh_res = mesh_res
        self.render_res, self.ray_res = rendray_res
    def prereq_test(self):
        return [self.mesh_res, self.render_res, self.ray_res]
    def __version__(self):
        return '0.0.1a'
    def sqcalcfull(self, indata):
        # Step 1: 2D Mesh Point calculation
        face  = [
            [1, 1, 0], # c1
            [3, 1, 0], # c2
            [1, 3, 0], # c3
            [3, 3, 0] # c4 // (NON-REGARD)
        ]
        inface = []
        gridset = []
        grid_size = (4, 4, 0)
        ugrid_size = (grid_size[0]+1,grid_size[1]+1,grid_size[2]+1)
        for z in range(ugrid_size[2]):
            for y in range(ugrid_size[1]):
                for x in range(ugrid_size[0]):
                    gridset.append([x, y, z])
        for c in gridset:
            if(face[1-1][0] <= c[0] <= face[2-1][0] and face[1-1][1] <= c[1] <= face[3-1][1]):
                inface.append(c)
        # inface = output
        # Step 2: Point Conversion
        tdp2 = []
        for c in inface:
            tdp1 = []
            tdp1.append(c[0])
            tdp1.append(c[1])
            tdp2.append(tdp1)
        #print(tdp2)
        g2 = []
        for c in gridset:
            g1 = []
            g1.append(c[0])
            g1.append(c[1])
            g2.append(tdp1)
        #print(tdp2)
        # Step 3: Color calculation:
        white = [255, 255, 255]
        black = [0, 0, 0]
        out = []
        for y in range(ugrid_size[1]):
            xout = []
            for x in range(ugrid_size[0]):
                coord = [x, y]
                w = False
                for c in tdp2:
                    if(c == coord):
                        w = True
                if(w):
                    xout.append(white)
                else:
                    xout.append(black)
            out.append(xout)

        # Step 4: Rendering:
        from PIL import Image
        import numpy as np
        Image.fromarray(np.uint8(out)).convert('RGB').save('2drend.png')
        return 0

co = [[1, 5, 0], [4, 5, 0], [3, 2, 1], [3, 3, 1], [1, 1, 0], [4, 1, 0]]
root = RenderImage(1, (len(co), len(co)))
print(root.sqcalcfull(co))
