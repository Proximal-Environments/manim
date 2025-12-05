#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root/proximal/workspace')

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle, Square

scene = Scene(skip_animations=True)
print('Initial mobjects:', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)

circle = Circle()
square = Square()
scene.add(circle, square)
print('After adding circle and square:', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)

scene.clear_all_except(circle)
print('After clear_all_except(circle):', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)
print('Circle in mobjects:', circle in scene.mobjects)
print('Square in mobjects:', square in scene.mobjects)
print('Mobjects:', scene.mobjects)
