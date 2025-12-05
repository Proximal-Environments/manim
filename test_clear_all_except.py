#!/usr/bin/env python
"""
Test script for clear_all_except method
"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import UP, DOWN, LEFT, RIGHT, RED, BLUE, GREEN, YELLOW


class TestClearAllExceptScene(Scene):
    """Test clear_all_except method in basic Scene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Text("Test", color=YELLOW).shift(UP * 2)
        
        # Add all objects
        self.add(circle, square, triangle, text)
        self.wait(1)
        
        # Test: Keep only circle and square, remove triangle and text
        print(f"Before clear_all_except: {len(self.get_mobjects())} mobjects")
        self.clear_all_except(circle, square)
        print(f"After clear_all_except: {len(self.get_mobjects())} mobjects")
        
        # Verify that only circle and square remain
        remaining_mobs = [m for m in self.get_mobjects() if m not in [self.camera.frame]]
        print(f"Remaining mobjects (excluding frame): {remaining_mobs}")
        
        assert circle in self.get_mobjects(), "Circle should still be in scene"
        assert square in self.get_mobjects(), "Square should still be in scene"
        assert triangle not in self.get_mobjects(), "Triangle should be removed"
        assert text not in self.get_mobjects(), "Text should be removed"
        
        self.wait(1)
        
        # Add new object to verify scene still works
        new_triangle = Triangle(color=YELLOW).shift(DOWN * 2)
        self.add(new_triangle)
        self.wait(1)
        
        # Test: Clear everything (no arguments)
        self.clear_all_except()
        print(f"After clear_all_except() with no args: {len([m for m in self.get_mobjects() if m != self.camera.frame])} mobjects (excluding frame)")
        
        self.wait(1)
        
        print("✓ TestClearAllExceptScene passed!")


class TestClearAllExceptInteractiveScene(InteractiveScene):
    """Test clear_all_except method in InteractiveScene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Test: Keep only circle
        print(f"Before clear_all_except: {len(self.get_mobjects())} mobjects")
        self.clear_all_except(circle)
        print(f"After clear_all_except: {len(self.get_mobjects())} mobjects")
        
        # Verify
        assert circle in self.get_mobjects(), "Circle should still be in scene"
        assert square not in self.get_mobjects(), "Square should be removed"
        assert triangle not in self.get_mobjects(), "Triangle should be removed"
        
        # Verify selection search set was regenerated
        print(f"Selection search set length: {len(self.selection_search_set)}")
        
        self.wait(1)
        
        # Add objects back and test again
        self.add(square, triangle)
        self.wait(1)
        
        # Keep multiple objects
        self.clear_all_except(circle, square)
        
        assert circle in self.get_mobjects(), "Circle should still be in scene"
        assert square in self.get_mobjects(), "Square should still be in scene"
        assert triangle not in self.get_mobjects(), "Triangle should be removed"
        
        self.wait(1)
        
        print("✓ TestClearAllExceptInteractiveScene passed!")


if __name__ == "__main__":
    import sys
    
    # Test basic Scene
    print("=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    
    from manimlib.config import manim_config
    # Configure for headless testing
    manim_config.window_config["size"] = "default"
    manim_config.window_monitor = 0
    
    try:
        # Create and run the test scene without window
        test_scene = TestClearAllExceptScene(
            skip_animations=True,
            show_animation_progress=False
        )
        test_scene.run()
        print()
        
        # Test InteractiveScene
        print("=" * 60)
        print("Testing InteractiveScene.clear_all_except()")
        print("=" * 60)
        
        test_interactive = TestClearAllExceptInteractiveScene(
            skip_animations=True,
            show_animation_progress=False
        )
        test_interactive.run()
        print()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
