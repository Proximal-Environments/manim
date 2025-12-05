#!/usr/bin/env python
"""
Test script for the clear_all_except method in both Scene and InteractiveScene
"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.constants import RED, BLUE, GREEN, YELLOW, UP, DOWN, LEFT, RIGHT


class TestClearAllExceptScene(Scene):
    """Test clear_all_except in regular Scene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Tex("Test").shift(UP * 2)
        
        # Add all objects to the scene
        self.add(circle, square, triangle, text)
        self.wait(1)
        
        # Verify all 4 objects are in the scene (plus the frame)
        print(f"Number of mobjects before clear_all_except: {len(self.mobjects)}")
        assert len(self.mobjects) == 5, f"Expected 5 mobjects (4 + frame), got {len(self.mobjects)}"
        
        # Clear all except circle and square
        self.clear_all_except(circle, square)
        self.wait(1)
        
        # Verify only 2 objects remain (plus the frame)
        print(f"Number of mobjects after clear_all_except: {len(self.mobjects)}")
        assert len(self.mobjects) == 3, f"Expected 3 mobjects (2 + frame), got {len(self.mobjects)}"
        assert circle in self.mobjects, "Circle should still be in scene"
        assert square in self.mobjects, "Square should still be in scene"
        assert triangle not in self.mobjects, "Triangle should not be in scene"
        assert text not in self.mobjects, "Text should not be in scene"
        
        # Add new objects
        new_square = Square(color=YELLOW).shift(DOWN * 2)
        self.add(new_square)
        self.wait(1)
        
        # Clear all except the new square
        self.clear_all_except(new_square)
        self.wait(1)
        
        # Verify only new square remains (plus the frame)
        print(f"Number of mobjects after second clear_all_except: {len(self.mobjects)}")
        assert len(self.mobjects) == 2, f"Expected 2 mobjects (1 + frame), got {len(self.mobjects)}"
        assert new_square in self.mobjects, "New square should be in scene"
        assert circle not in self.mobjects, "Circle should not be in scene"
        assert square not in self.mobjects, "Square should not be in scene"
        
        print("✓ All Scene tests passed!")


class TestClearAllExceptInteractiveScene(InteractiveScene):
    """Test clear_all_except in InteractiveScene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Tex("Interactive").shift(UP * 2)
        
        # Add all objects to the scene
        self.add(circle, square, triangle, text)
        self.wait(1)
        
        # Count user-added objects (excluding internal InteractiveScene objects)
        user_objects_before = [m for m in self.mobjects if m not in self.unselectables]
        print(f"Number of user objects before clear_all_except: {len(user_objects_before)}")
        assert len(user_objects_before) == 4, f"Expected 4 user objects, got {len(user_objects_before)}"
        
        # Clear all except circle and square
        self.clear_all_except(circle, square)
        self.wait(1)
        
        # Verify only 2 user objects remain
        user_objects_after = [m for m in self.mobjects if m not in self.unselectables]
        print(f"Number of user objects after clear_all_except: {len(user_objects_after)}")
        assert len(user_objects_after) == 2, f"Expected 2 user objects, got {len(user_objects_after)}"
        assert circle in self.mobjects, "Circle should still be in scene"
        assert square in self.mobjects, "Square should still be in scene"
        assert triangle not in self.mobjects, "Triangle should not be in scene"
        assert text not in self.mobjects, "Text should not be in scene"
        
        # Verify selection_highlight is still there (it's in unselectables)
        assert self.selection_highlight in self.mobjects, "selection_highlight should still be in scene"
        
        # Add new objects
        new_circle = Circle(color=YELLOW).shift(DOWN * 2)
        self.add(new_circle)
        self.wait(1)
        
        # Clear all except the new circle
        self.clear_all_except(new_circle)
        self.wait(1)
        
        # Verify only new circle remains
        user_objects_final = [m for m in self.mobjects if m not in self.unselectables]
        print(f"Number of user objects after second clear_all_except: {len(user_objects_final)}")
        assert len(user_objects_final) == 1, f"Expected 1 user object, got {len(user_objects_final)}"
        assert new_circle in self.mobjects, "New circle should be in scene"
        assert circle not in self.mobjects, "Circle should not be in scene"
        assert square not in self.mobjects, "Square should not be in scene"
        
        print("✓ All InteractiveScene tests passed!")


if __name__ == "__main__":
    import sys
    
    # Test regular Scene
    print("=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    try:
        from manimlib import config
        config.digest_args([])
        scene1 = TestClearAllExceptScene()
        scene1.run()
    except Exception as e:
        print(f"✗ Scene test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Test InteractiveScene
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except()")
    print("=" * 60)
    try:
        config.digest_args([])
        scene2 = TestClearAllExceptInteractiveScene()
        scene2.run()
    except Exception as e:
        print(f"✗ InteractiveScene test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED!")
    print("=" * 60)
