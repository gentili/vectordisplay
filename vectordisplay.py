#!/usr/bin/env python

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL.GL.shaders import *

import numpy as np


# A 1-D array of 3 4-D vertices (X,Y,Z,W)
# Note that this must be a numpy array, since as of 
# 170111 support for lists has not been implemented.
vertexPositions = np.array(
    [0.25, 0.25, 0.0, 1.0,
    0.25, -0.25, 0.0, 1.0, 
    -0.25, -0.25, 0.0, 1.0],
    dtype='float32'
)

vertexDim = 4
nVertices = 3

# String containing vertex shader program written in GLSL
strVertexShader = """
#version 300 es

in vec4 position;
void main()
{
   gl_Position = position;
}
"""

# String containing fragment shader program written in GLSL
strFragmentShader = """
#version 300 es
precision mediump float;

out vec4 outputColor;
void main()
{
   outputColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}
"""

def keyboard(key, x, y):
    glutLeaveMainLoop()

def display():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shaderProgram)

    glBindBuffer(GL_ARRAY_BUFFER, positionBufferObject)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, vertexDim, GL_FLOAT, GL_FALSE, 0, None)

    glDrawArrays(GL_TRIANGLES, 0, nVertices)

    glDisableVertexAttribArray(0)
    glUseProgram(0)

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)

def main():
    glutInit()
    displayMode = GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH
    glutInitDisplayMode(displayMode)
    window = glutCreateWindow("Blammo!")
    glutFullScreen()

    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)

    glutSetCursor(GLUT_CURSOR_NONE)


    # Set up shaders
    global shaderProgram
    shaderProgram = compileProgram(
        compileShader( strVertexShader, GL_VERTEX_SHADER),
        compileShader( strFragmentShader, GL_FRAGMENT_SHADER),
    )

    # Set up buffers
    global positionBufferObject
    positionBufferObject = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, positionBufferObject)
    glBufferData(
        GL_ARRAY_BUFFER,
        vertexPositions,
        GL_STATIC_DRAW
    )
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    glBindVertexArray(glGenVertexArrays(1))

    print("Entering main loop")

    glutMainLoop()


if __name__ == '__main__':
    main()
