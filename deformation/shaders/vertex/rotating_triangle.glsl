#version 330
uniform mat4 rotation_matrix;
in vec2 in_vert;
in vec3 in_color;
out vec3 color;

void main() {
    gl_Position = rotation_matrix * vec4(in_vert, 0.0, 1.0);
    color = in_color;
}