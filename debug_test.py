#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root/proximal/workspace')

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle

scene = Scene(skip_animations=True)
print('Initial mobjects:', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)

circle = Circle()
scene.add(circle)
print('After adding circle:', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)

scene.clear()
print('After clear:', len(scene.mobjects))
print('Camera frame in mobjects:', scene.camera.frame in scene.mobjects)
print('Mobjects:', scene.mobjects)
