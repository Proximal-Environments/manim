#!/usr/bin/env python3
"""Quick integration test for clear_all_except method"""

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square

print("=" * 60)
print("Quick Integration Test")
print("=" * 60)

# Test 1: Scene class
print("\n1. Testing Scene.clear_all_except()...")
scene = Scene()
circle = Circle()
square = Square()
scene.add(circle, square)
assert circle in scene.mobjects and square in scene.mobjects
scene.clear_all_except(circle)
assert circle in scene.mobjects and square not in scene.mobjects
print("   ✓ Scene test passed")

# Test 2: InteractiveScene class
print("\n2. Testing InteractiveScene.clear_all_except()...")
interactive = InteractiveScene()
interactive.setup()
circle2 = Circle()
square2 = Square()
interactive.add(circle2, square2)
assert circle2 in interactive.mobjects and square2 in interactive.mobjects
initial_highlight_present = interactive.selection_highlight in interactive.mobjects
interactive.clear_all_except(circle2)
assert circle2 in interactive.mobjects and square2 not in interactive.mobjects
final_highlight_present = interactive.selection_highlight in interactive.mobjects
assert initial_highlight_present == final_highlight_present, "selection_highlight preservation failed"
print("   ✓ InteractiveScene test passed")

# Test 3: Method chaining
print("\n3. Testing method chaining...")
scene2 = Scene()
obj1 = Circle()
obj2 = Square()
result = scene2.add(obj1, obj2).clear_all_except(obj1).add(obj2)
assert result is scene2, "Method chaining failed"
assert obj1 in scene2.mobjects and obj2 in scene2.mobjects
print("   ✓ Method chaining test passed")

# Test 4: Empty arguments
print("\n4. Testing clear_all_except() with no arguments...")
scene3 = Scene()
obj = Circle()
scene3.add(obj)
scene3.clear_all_except()
assert obj not in scene3.mobjects
print("   ✓ Empty arguments test passed")

print("\n" + "=" * 60)
print("All Quick Tests Passed! ✓")
print("=" * 60)
print("\nThe clear_all_except method is working correctly!")
print("Ready for use in your animations.")
