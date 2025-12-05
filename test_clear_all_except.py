#!/usr/bin/env python
"""Test script for clear_all_except method"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import RED, BLUE, GREEN, YELLOW, PURPLE


class TestClearAllExceptScene(Scene):
    """Test clear_all_except in basic Scene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(2 * LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(2 * RIGHT)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(0.5)
        
        # Verify all objects are present
        assert len(self.mobjects) >= 3, f"Expected at least 3 mobjects, got {len(self.mobjects)}"
        print(f"✓ Initial state: {len(self.mobjects)} mobjects in scene")
        
        # Clear all except the square
        self.clear_all_except(square)
        self.wait(0.5)
        
        # Verify only the square remains (plus camera frame)
        # Note: self.mobjects may include camera.frame
        assert square in self.mobjects, "Square should still be in scene"
        assert circle not in self.mobjects, "Circle should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        print(f"✓ After clear_all_except(square): {len(self.mobjects)} mobjects in scene")
        
        # Add new objects
        new_circle = Circle(color=YELLOW).shift(LEFT)
        new_triangle = Triangle(color=PURPLE).shift(RIGHT)
        self.add(new_circle, new_triangle)
        self.wait(0.5)
        
        print(f"✓ After adding new objects: {len(self.mobjects)} mobjects in scene")
        
        # Clear all except multiple objects
        self.clear_all_except(square, new_circle)
        self.wait(0.5)
        
        # Verify only square and new_circle remain
        assert square in self.mobjects, "Square should still be in scene"
        assert new_circle in self.mobjects, "New circle should still be in scene"
        assert new_triangle not in self.mobjects, "New triangle should be removed"
        print(f"✓ After clear_all_except(square, new_circle): {len(self.mobjects)} mobjects in scene")
        
        # Clear everything
        self.clear_all_except()
        self.wait(0.5)
        
        # Verify scene is essentially empty (may have camera frame)
        assert square not in self.mobjects, "Square should be removed"
        assert new_circle not in self.mobjects, "New circle should be removed"
        print(f"✓ After clear_all_except(): {len(self.mobjects)} mobjects in scene")
        
        print("\n✅ All tests passed for Scene.clear_all_except!")


class TestClearAllExceptInteractiveScene(InteractiveScene):
    """Test clear_all_except in InteractiveScene"""
    
    def construct(self):
        # Create multiple objects
        circle = Circle(color=RED).shift(2 * LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(2 * RIGHT)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(0.5)
        
        # Verify all objects are present
        print(f"✓ Initial state: {len(self.mobjects)} mobjects in scene")
        
        # Add to selection
        self.add_to_selection(circle, triangle)
        assert len(self.selection) == 2, "Should have 2 items in selection"
        print(f"✓ Selection has {len(self.selection)} items")
        
        # Clear all except the square
        self.clear_all_except(square)
        self.wait(0.5)
        
        # Verify selection is cleared
        assert len(self.selection) == 0, "Selection should be cleared"
        print(f"✓ Selection cleared after clear_all_except")
        
        # Verify only the square remains
        assert square in self.mobjects, "Square should still be in scene"
        assert circle not in self.mobjects, "Circle should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        print(f"✓ After clear_all_except(square): {len(self.mobjects)} mobjects in scene")
        
        # Add new objects
        new_circle = Circle(color=YELLOW).shift(LEFT)
        new_triangle = Triangle(color=PURPLE).shift(RIGHT)
        self.add(new_circle, new_triangle)
        self.wait(0.5)
        
        print(f"✓ After adding new objects: {len(self.mobjects)} mobjects in scene")
        
        # Clear all except multiple objects
        self.clear_all_except(square, new_circle)
        self.wait(0.5)
        
        # Verify only square and new_circle remain
        assert square in self.mobjects, "Square should still be in scene"
        assert new_circle in self.mobjects, "New circle should still be in scene"
        assert new_triangle not in self.mobjects, "New triangle should be removed"
        print(f"✓ After clear_all_except(square, new_circle): {len(self.mobjects)} mobjects in scene")
        
        print("\n✅ All tests passed for InteractiveScene.clear_all_except!")


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Testing Scene.clear_all_except")
    print("=" * 60)
    
    # Test basic Scene
    scene1 = TestClearAllExceptScene(
        skip_animations=True,
        show_animation_progress=False
    )
    try:
        scene1.run()
    except Exception as e:
        print(f"❌ Error in Scene test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except")
    print("=" * 60)
    
    # Test InteractiveScene
    scene2 = TestClearAllExceptInteractiveScene(
        skip_animations=True,
        show_animation_progress=False
    )
    try:
        scene2.run()
    except Exception as e:
        print(f"❌ Error in InteractiveScene test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed successfully!")
    print("=" * 60)
