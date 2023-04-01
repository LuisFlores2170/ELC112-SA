import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos
#-------------------------------------------------------------------------------
# verifica que glfw no pudo ser inicializada
if not glfw.init():
    raise Exception("GLFW CAN NOT BE INITIALIZED")

#-------------------------------------------------------------------------------
# Crea la ventana y sus dimenciones
wd = glfw.create_window(500, 400, "WINDOW 01", None, None)

#-------------------------------------------------------------------------------
# verifica si la ventana no pudo ser creada
if not wd:
    glfw.terminate()
    raise Exception("WD CAN NOT BE CREATED")

#-------------------------------------------------------------------------------
# Posiciona la ventana en una posicion del monitor
glfw.set_window_pos(wd, 100, 100)
glfw.make_context_current(wd)

#-------------------------------------------------------------------------------
#posiciones xyz1, xyz2, xyz3
vertices = [
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0, 0.5, 0.0,
]

#-------------------------------------------------------------------------------

vertices = np.array(vertices, dtype=np.float32)
#-------------------------------------------------------------------------------

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)


#-------------------------------------------------------------------------------
# Ejecuta la ventana (MAINLOOP)
while not glfw.window_should_close(wd):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)

    #------------------------------------------------------

    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(wd)

#-------------------------------------------------------------------------------
# Destruye la ventana
glfw.terminate()