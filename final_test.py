#!/usr/bin/env python
"""Final comprehensive test of clear_all_except functionality"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import LEFT, RIGHT, UP, RED, BLUE, GREEN, YELLOW

print("=" * 70)
print("FINAL COMPREHENSIVE TEST OF clear_all_except()")
print("=" * 70)

# Test 1: Basic Scene functionality
print("\n[1/5] Testing basic Scene.clear_all_except()...")
scene = Scene(skip_animations=True)
c1 = Circle(color=RED)
c2 = Square(color=BLUE)
c3 = Triangle(color=GREEN)

scene.add(c1, c2, c3)
assert len([m for m in scene.get_mobjects() if m != scene.camera.frame]) == 3

scene.clear_all_except(c1, c2)
remaining = [m for m in scene.get_mobjects() if m != scene.camera.frame]
assert len(remaining) == 2
assert c1 in remaining and c2 in remaining and c3 not in remaining
print("   ✓ Basic functionality works")

# Test 2: Empty clear
print("\n[2/5] Testing clear_all_except() with no arguments...")
scene.clear_all_except()
assert len([m for m in scene.get_mobjects() if m != scene.camera.frame]) == 0
print("   ✓ Empty clear works")

# Test 3: Deduplication
print("\n[3/5] Testing deduplication...")
circle = Circle(color=RED)
scene.add(circle)
scene.clear_all_except(circle, circle, circle)
remaining = [m for m in scene.get_mobjects() if m != scene.camera.frame]
assert remaining.count(circle) == 1
print("   ✓ Deduplication works")

# Test 4: Method chaining
print("\n[4/5] Testing method chaining...")
scene.clear()
t = Text("Title").to_edge(UP)
c = Circle()
result = scene.clear_all_except(t).add(c)
assert result is scene
assert t in scene.get_mobjects()
assert c in scene.get_mobjects()
print("   ✓ Method chaining works")

# Test 5: InteractiveScene
print("\n[5/5] Testing InteractiveScene.clear_all_except()...")
iscene = InteractiveScene(skip_animations=True)
iscene.setup()  # Initialize interactive components

c1 = Circle(color=RED).shift(LEFT)
c2 = Square(color=BLUE).shift(RIGHT)
iscene.add(c1, c2)

highlight_before = iscene.selection_highlight in iscene.get_mobjects()
iscene.clear_all_except(c1)
highlight_after = iscene.selection_highlight in iscene.get_mobjects()

assert c1 in iscene.get_mobjects()
assert c2 not in iscene.get_mobjects()
assert highlight_before and highlight_after  # Highlight preserved
print("   ✓ InteractiveScene functionality works")
print("   ✓ Selection highlight automatically preserved")

print("\n" + "=" * 70)
print("ALL TESTS PASSED! ✓✓✓")
print("=" * 70)
print("\nThe clear_all_except() method has been successfully implemented in:")
print("  • manimlib/scene/scene.py")
print("  • manimlib/scene/interactive_scene.py")
print("\nFeatures:")
print("  • Clears all objects except those specified")
print("  • Automatic deduplication")
print("  • Method chaining support")
print("  • InteractiveScene preserves selection_highlight")
print("  • Comprehensive test coverage")
print("\nRun 'xvfb-run -a python test_clear_all_except.py' for detailed tests")
