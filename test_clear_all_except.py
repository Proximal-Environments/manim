#!/usr/bin/env python
"""
Test script for the clear_all_except method in both Scene and InteractiveScene
"""

import sys
import os

# Simple unit test without window/rendering
def test_scene_clear_all_except():
    """Test clear_all_except in regular Scene"""
    print("=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    
    from manimlib.scene.scene import Scene
    from manimlib.mobject.geometry import Circle, Square, Triangle
    from manimlib.constants import RED, BLUE, GREEN, YELLOW, UP, DOWN, LEFT, RIGHT
    
    # Create scene without window
    scene = Scene(skip_animations=True)
    
    # Create multiple objects
    circle = Circle(color=RED).shift(LEFT * 2)
    square = Square(color=BLUE)
    triangle = Triangle(color=GREEN).shift(RIGHT * 2)
    
    # Add all objects to the scene
    scene.add(circle, square, triangle)
    
    # Verify all 3 objects are in the scene (plus the frame)
    print(f"Number of mobjects before clear_all_except: {len(scene.mobjects)}")
    assert len(scene.mobjects) == 4, f"Expected 4 mobjects (3 + frame), got {len(scene.mobjects)}"
    assert scene.frame in scene.mobjects, "Frame should be in scene initially"
    
    # Clear all except circle and square (frame should be preserved automatically)
    scene.clear_all_except(circle, square)
    
    # Verify only 2 objects remain (plus the frame which is auto-preserved)
    print(f"Number of mobjects after clear_all_except: {len(scene.mobjects)}")
    assert len(scene.mobjects) == 3, f"Expected 3 mobjects (2 + frame), got {len(scene.mobjects)}"
    assert scene.frame in scene.mobjects, "Frame should still be in scene (auto-preserved)"
    assert circle in scene.mobjects, "Circle should still be in scene"
    assert square in scene.mobjects, "Square should still be in scene"
    assert triangle not in scene.mobjects, "Triangle should not be in scene"
    
    # Add new objects
    new_square = Square(color=YELLOW).shift(DOWN * 2)
    scene.add(new_square)
    
    # Verify 3 objects now (plus frame)
    print(f"Number of mobjects after adding new_square: {len(scene.mobjects)}")
    assert len(scene.mobjects) == 4, f"Expected 4 mobjects (3 + frame), got {len(scene.mobjects)}"
    
    # Clear all except the new square
    scene.clear_all_except(new_square)
    
    # Verify only new square remains (plus the frame which is auto-preserved)
    print(f"Number of mobjects after second clear_all_except: {len(scene.mobjects)}")
    assert len(scene.mobjects) == 2, f"Expected 2 mobjects (1 + frame), got {len(scene.mobjects)}"
    assert new_square in scene.mobjects, "New square should be in scene"
    assert circle not in scene.mobjects, "Circle should not be in scene"
    assert square not in scene.mobjects, "Square should not be in scene"
    assert scene.frame in scene.mobjects, "Frame should still be in scene (auto-preserved)"
    
    print("✓ All Scene tests passed!")
    return True


def test_interactive_scene_clear_all_except():
    """Test clear_all_except in InteractiveScene"""
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except()")
    print("=" * 60)
    
    from manimlib.scene.interactive_scene import InteractiveScene
    from manimlib.mobject.geometry import Circle, Square, Triangle
    from manimlib.constants import RED, BLUE, GREEN, YELLOW, UP, DOWN, LEFT, RIGHT
    
    # Create scene without window
    scene = InteractiveScene(skip_animations=True)
    scene.setup()  # Initialize interactive scene components
    
    # Create multiple objects
    circle = Circle(color=RED).shift(LEFT * 2)
    square = Square(color=BLUE)
    triangle = Triangle(color=GREEN).shift(RIGHT * 2)
    
    # Add all objects to the scene
    scene.add(circle, square, triangle)
    
    # Count user-added objects (excluding internal InteractiveScene objects)
    user_objects_before = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"Number of user objects before clear_all_except: {len(user_objects_before)}")
    assert len(user_objects_before) == 3, f"Expected 3 user objects, got {len(user_objects_before)}"
    
    # Clear all except circle and square
    scene.clear_all_except(circle, square)
    
    # Verify only 2 user objects remain
    user_objects_after = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"Number of user objects after clear_all_except: {len(user_objects_after)}")
    assert len(user_objects_after) == 2, f"Expected 2 user objects, got {len(user_objects_after)}"
    assert circle in scene.mobjects, "Circle should still be in scene"
    assert square in scene.mobjects, "Square should still be in scene"
    assert triangle not in scene.mobjects, "Triangle should not be in scene"
    
    # Verify selection_highlight is still there (it's in unselectables)
    assert scene.selection_highlight in scene.mobjects, "selection_highlight should still be in scene"
    
    # Add new objects
    new_circle = Circle(color=YELLOW).shift(DOWN * 2)
    scene.add(new_circle)
    
    # Verify 3 user objects now
    user_objects_middle = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"Number of user objects after adding new_circle: {len(user_objects_middle)}")
    assert len(user_objects_middle) == 3, f"Expected 3 user objects, got {len(user_objects_middle)}"
    
    # Clear all except the new circle
    scene.clear_all_except(new_circle)
    
    # Verify only new circle remains
    user_objects_final = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"Number of user objects after second clear_all_except: {len(user_objects_final)}")
    assert len(user_objects_final) == 1, f"Expected 1 user object, got {len(user_objects_final)}"
    assert new_circle in scene.mobjects, "New circle should be in scene"
    assert circle not in scene.mobjects, "Circle should not be in scene"
    assert square not in scene.mobjects, "Square should not be in scene"
    
    print("✓ All InteractiveScene tests passed!")
    return True


if __name__ == "__main__":
    try:
        # Test regular Scene
        test_scene_clear_all_except()
        
        # Test InteractiveScene
        test_interactive_scene_clear_all_except()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED!")
        print("=" * 60)
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
