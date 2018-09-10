#!/usr/bin/env python

from sdl2 import *
import sdl2.video
from OpenGL import GL

SDL_Init(SDL_INIT_VIDEO)
rect = SDL_Rect()
SDL_GetDisplayBounds(0,rect)
window = SDL_CreateWindow(None,
                          SDL_WINDOWPOS_UNDEFINED,
                          SDL_WINDOWPOS_UNDEFINED,
                          rect.w,
                          rect.h,
                          SDL_WINDOW_OPENGL | SDL_WINDOW_FULLSCREEN_DESKTOP)
SDL_ShowCursor(SDL_DISABLE)
print(sdl2.video.SDL_GL_SetAttribute(
    sdl2.video.SDL_GL_CONTEXT_MAJOR_VERSION,
    3))
print(sdl2.video.SDL_GL_SetAttribute(
    sdl2.video.SDL_GL_CONTEXT_MINOR_VERSION,
    3))
print(sdl2.video.SDL_GL_SetAttribute(
    sdl2.video.SDL_GL_CONTEXT_PROFILE_MASK,
    sdl2.video.SDL_GL_CONTEXT_PROFILE_CORE))
context = sdl2.SDL_GL_CreateContext(window)
GL.glClearColor(0.3,0.3,0.3,1)
GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
sdl2.SDL_GL_SwapWindow(window)

input ("running")
