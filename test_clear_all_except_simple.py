#!/usr/bin/env python3
"""
Simple test script for the clear_all_except method (no window required)
"""

# Need to set headless mode before importing manimlib
import os
os.environ['MANIMGL_HEADLESS'] = '1'

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import UP, DOWN, LEFT, RIGHT


def test_scene_clear_all_except():
    """Test the clear_all_except method in Scene"""
    print("=" * 60)
    print("Testing clear_all_except in Scene")
    print("=" * 60)
    
    # Create a scene without window
    scene = Scene(skip_animations=True)
    
    # Create some objects
    circle = Circle().shift(UP)
    square = Square().shift(DOWN)
    triangle = Triangle().shift(LEFT)
    text = Text("Keep Me").shift(RIGHT)
    
    # Add all objects to the scene
    scene.add(circle, square, triangle, text)
    
    # Verify all objects are in the scene
    # Note: Scene always has camera.frame as mobject[0]
    assert len(scene.mobjects) == 5, f"Expected 5 mobjects (4 + camera frame), got {len(scene.mobjects)}"
    print(f"✓ Initially added 4 mobjects to scene (total: {len(scene.mobjects)} including camera frame)")
    
    # Clear all except circle and text
    scene.clear_all_except(circle, text)
    
    # Verify only circle and text remain (plus camera frame)
    assert len(scene.mobjects) == 3, f"Expected 3 mobjects (2 + camera frame), got {len(scene.mobjects)}"
    assert circle in scene.mobjects, "Circle should be in mobjects"
    assert text in scene.mobjects, "Text should be in mobjects"
    assert square not in scene.mobjects, "Square should not be in mobjects"
    assert triangle not in scene.mobjects, "Triangle should not be in mobjects"
    
    print(f"✓ After clear_all_except, kept 2 mobjects (total: {len(scene.mobjects)} including camera frame)")
    print("✓ Verified that only circle and text remain")
    
    # Test clearing all with empty keep list
    scene.clear_all_except()
    assert len(scene.mobjects) == 1, f"Expected 1 mobject (camera frame), got {len(scene.mobjects)}"
    print(f"✓ After clear_all_except() with no arguments, scene is empty (only camera frame remains)")
    
    # Test method chaining
    circle2 = Circle()
    result = scene.clear_all_except(circle2)
    assert result is scene, "clear_all_except should return self for chaining"
    print("✓ Method returns self for chaining")
    
    print("\n✅ All Scene tests passed!\n")


def test_interactive_scene_clear_all_except():
    """Test the clear_all_except method in InteractiveScene"""
    print("=" * 60)
    print("Testing clear_all_except in InteractiveScene")
    print("=" * 60)
    
    # Create an interactive scene without window
    scene = InteractiveScene(skip_animations=True)
    scene.setup()  # Need to call setup to initialize interactive scene elements
    
    # Create some objects
    circle = Circle().shift(UP)
    square = Square().shift(DOWN)
    triangle = Triangle().shift(LEFT)
    text = Text("Interactive").shift(RIGHT)
    
    # Add all objects to the scene
    scene.add(circle, square, triangle, text)
    
    # Count non-unselectable mobjects
    selectable_count = len([m for m in scene.mobjects if m not in scene.unselectables])
    assert selectable_count == 4, f"Expected 4 selectable mobjects, got {selectable_count}"
    print(f"✓ Initially added 4 mobjects to interactive scene")
    
    # Verify selection_search_set is populated
    initial_search_set_size = len(scene.selection_search_set)
    print(f"  Selection search set size: {initial_search_set_size}")
    
    # Clear all except circle and text
    scene.clear_all_except(circle, text)
    
    # Verify only circle and text remain (excluding unselectables)
    selectable_count = len([m for m in scene.mobjects if m not in scene.unselectables])
    assert selectable_count == 2, f"Expected 2 selectable mobjects, got {selectable_count}"
    assert circle in scene.mobjects, "Circle should be in mobjects"
    assert text in scene.mobjects, "Text should be in mobjects"
    assert square not in scene.mobjects, "Square should not be in mobjects"
    assert triangle not in scene.mobjects, "Triangle should not be in mobjects"
    
    # Verify selection_search_set was regenerated
    after_search_set_size = len(scene.selection_search_set)
    print(f"✓ After clear_all_except, kept 2 mobjects")
    print(f"  Selection search set size: {after_search_set_size}")
    assert after_search_set_size == 2, f"Expected selection_search_set to have 2 items, got {after_search_set_size}"
    
    # Test clearing all with empty keep list
    scene.clear_all_except()
    selectable_count = len([m for m in scene.mobjects if m not in scene.unselectables])
    assert selectable_count == 0, f"Expected 0 selectable mobjects, got {selectable_count}"
    assert len(scene.selection_search_set) == 0, "Selection search set should be empty"
    print(f"✓ After clear_all_except() with no arguments, all mobjects cleared")
    print(f"  Selection search set size: {len(scene.selection_search_set)}")
    
    # Test method chaining
    circle2 = Circle()
    result = scene.clear_all_except(circle2)
    assert result is scene, "clear_all_except should return self for chaining"
    print("✓ Method returns self for chaining")
    
    print("\n✅ All InteractiveScene tests passed!\n")


if __name__ == "__main__":
    import sys
    
    try:
        test_scene_clear_all_except()
        test_interactive_scene_clear_all_except()
        
        print("=" * 60)
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
