# test.py
import moderngl
import moderngl_window as mglw
import numpy as np
from pyrr import Matrix44

class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (512, 512)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open("./shaders/vertex/rotating_triangle.glsl", "r") as shader:
            vertex_shader = shader.read()

        with open("./shaders/fragment/set_color.glsl", "r") as shader:
            fragment_shader = shader.read()

        self.program = self.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader
        )

        vertices = np.array([
            -0.57735, -0.57735,
            1.0, 0.0, 0.0,
            0.57735, -0.57735,
            0.0, 1.0, 0.0,
            0.0, 1.0,
            0.0, 0.0, 1.0,
        ], dtype='f4')

        vbo = self.ctx.buffer(vertices)
        self.vao = self.ctx.simple_vertex_array(self.program, vbo, 'in_vert', 'in_color')
        self.ctx.clear()

    def render(self, time, frametime):
        self.program['rotation_matrix'].write(Matrix44.from_eulers((0.0, 0, 0.0), dtype='f4'))
        self.vao.render(moderngl.TRIANGLES)


Test.run()