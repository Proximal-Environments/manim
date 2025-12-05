#!/usr/bin/env python3
"""Quick simple test to verify clear_all_except works"""

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import RED, BLUE, GREEN

# Test Scene
print("Testing Scene.clear_all_except()...")
scene = Scene(skip_animations=True)

circle = Circle(color=RED)
square = Square(color=BLUE)
triangle = Triangle(color=GREEN)

scene.add(circle, square, triangle)
print(f"Added 3 objects. Total: {len(scene.mobjects)}")
assert len(scene.mobjects) == 4  # 3 objects + camera frame

scene.clear_all_except(circle)
print(f"After clear_all_except(circle): {len(scene.mobjects)}")
assert circle in scene.mobjects
assert square not in scene.mobjects
assert triangle not in scene.mobjects
print("✅ Scene test passed!")

# Test InteractiveScene
print("\nTesting InteractiveScene.clear_all_except()...")
iscene = InteractiveScene(skip_animations=True)
iscene.setup()  # InteractiveScene needs setup to initialize unselectables

c1 = Circle(color=RED)
c2 = Square(color=BLUE)
c3 = Triangle(color=GREEN)

iscene.add(c1, c2, c3)
initial_search_set = len(iscene.selection_search_set)
print(f"Added 3 objects. Search set: {initial_search_set}")

iscene.clear_all_except(c1, c2)
after_search_set = len(iscene.selection_search_set)
print(f"After clear_all_except(c1, c2). Search set: {after_search_set}")
assert c1 in iscene.mobjects
assert c2 in iscene.mobjects
assert c3 not in iscene.mobjects
assert after_search_set == 2
print("✅ InteractiveScene test passed!")

print("\n🎉 All simple tests passed!")
