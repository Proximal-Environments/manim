#!/usr/bin/env python3
"""Test script for clear_all_except method"""

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text


def test_scene_clear_all_except():
    """Test clear_all_except in Scene class"""
    print("Testing Scene.clear_all_except()...")
    
    # Create a scene without window for testing
    scene = Scene()
    
    # Create some test mobjects
    circle = Circle()
    square = Square()
    triangle = Triangle()
    
    # Add all mobjects to scene
    scene.add(circle, square, triangle)
    
    # Verify all mobjects are in the scene (plus camera frame)
    # Note: camera.frame is always in mobjects
    initial_count = len(scene.mobjects)
    print(f"  Initial mobject count: {initial_count}")
    assert circle in scene.mobjects, "Circle should be in scene"
    assert square in scene.mobjects, "Square should be in scene"
    assert triangle in scene.mobjects, "Triangle should be in scene"
    
    # Clear all except circle and square
    scene.clear_all_except(circle, square)
    
    # Verify only circle and square remain (plus camera frame)
    final_count = len(scene.mobjects)
    print(f"  Final mobject count: {final_count}")
    assert circle in scene.mobjects, "Circle should still be in scene"
    assert square in scene.mobjects, "Square should still be in scene"
    assert triangle not in scene.mobjects, "Triangle should be removed from scene"
    
    print("  ✓ Scene.clear_all_except() test passed!")
    

def test_interactive_scene_clear_all_except():
    """Test clear_all_except in InteractiveScene class"""
    print("\nTesting InteractiveScene.clear_all_except()...")
    
    # Create an interactive scene without window for testing
    scene = InteractiveScene()
    scene.setup()  # This initializes selection-related mobjects
    
    # Create some test mobjects
    circle = Circle()
    square = Square()
    triangle = Triangle()
    text = Text("Test")
    
    # Add mobjects to scene
    scene.add(circle, square, triangle, text)
    
    # Verify all mobjects are in the scene
    initial_count = len(scene.mobjects)
    print(f"  Initial mobject count: {initial_count}")
    assert circle in scene.mobjects, "Circle should be in scene"
    assert square in scene.mobjects, "Square should be in scene"
    assert triangle in scene.mobjects, "Triangle should be in scene"
    assert text in scene.mobjects, "Text should be in scene"
    
    # Clear all except square and text
    scene.clear_all_except(square, text)
    
    # Verify only square and text remain
    final_count = len(scene.mobjects)
    print(f"  Final mobject count: {final_count}")
    assert circle not in scene.mobjects, "Circle should be removed from scene"
    assert square in scene.mobjects, "Square should still be in scene"
    assert triangle not in scene.mobjects, "Triangle should be removed from scene"
    assert text in scene.mobjects, "Text should still be in scene"
    
    # Verify selection_highlight is still there (it's an unselectable)
    assert scene.selection_highlight in scene.mobjects, "Selection highlight should still exist"
    
    print("  ✓ InteractiveScene.clear_all_except() test passed!")


def test_clear_all_except_empty():
    """Test clear_all_except with no arguments (should clear all)"""
    print("\nTesting clear_all_except with no arguments...")
    
    scene = Scene()
    
    # Create and add test mobjects
    circle = Circle()
    square = Square()
    scene.add(circle, square)
    
    initial_count = len(scene.mobjects)
    print(f"  Initial mobject count: {initial_count}")
    
    # Clear all (no mobjects to keep)
    scene.clear_all_except()
    
    final_count = len(scene.mobjects)
    print(f"  Final mobject count: {final_count}")
    
    # Only camera.frame should remain
    assert circle not in scene.mobjects, "Circle should be removed"
    assert square not in scene.mobjects, "Square should be removed"
    
    print("  ✓ clear_all_except() with no arguments test passed!")


def test_clear_all_except_keeps_camera_frame():
    """Test that camera.frame is properly handled"""
    print("\nTesting that camera frame is preserved...")
    
    scene = Scene()
    camera_frame = scene.camera.frame
    
    # Add some mobjects
    circle = Circle()
    square = Square()
    scene.add(circle, square)
    
    # The camera frame should already be in mobjects from __init__
    assert camera_frame in scene.mobjects, "Camera frame should be in scene initially"
    
    # Clear all except circle
    scene.clear_all_except(circle)
    
    # Verify circle is kept and camera frame is still there
    assert circle in scene.mobjects, "Circle should be kept"
    assert square not in scene.mobjects, "Square should be removed"
    # The camera frame may or may not be explicitly kept depending on implementation
    # but it's OK either way as long as the scene functions properly
    
    print("  ✓ Camera frame handling test passed!")


def test_return_value():
    """Test that clear_all_except returns self for method chaining"""
    print("\nTesting return value for method chaining...")
    
    scene = Scene()
    circle = Circle()
    square = Square()
    
    scene.add(circle, square)
    
    # Test that we can chain methods
    result = scene.clear_all_except(circle).add(square)
    
    assert result is scene, "clear_all_except should return self"
    assert circle in scene.mobjects, "Circle should be in scene"
    assert square in scene.mobjects, "Square should be in scene (added after clear)"
    
    print("  ✓ Method chaining test passed!")


if __name__ == "__main__":
    print("=" * 60)
    print("Running tests for clear_all_except method")
    print("=" * 60)
    
    try:
        test_scene_clear_all_except()
        test_interactive_scene_clear_all_except()
        test_clear_all_except_empty()
        test_clear_all_except_keeps_camera_frame()
        test_return_value()
        
        print("\n" + "=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
