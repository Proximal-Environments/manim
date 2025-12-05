#!/usr/bin/env python
"""Test script for clear_all_except method"""

from manimlib import *

class TestClearAllExceptScene(Scene):
    """Test the clear_all_except method for Scene"""
    
    def construct(self):
        # Create several mobjects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Text("Keep Me!", font_size=24).to_edge(UP)
        
        # Add all mobjects
        self.add(circle, square, triangle, text)
        self.wait(1)
        
        # Clear all except the text and square
        self.clear_all_except(text, square)
        self.wait(1)
        
        # Verify that only text and square remain
        assert text in self.mobjects, "Text should still be in scene"
        assert square in self.mobjects, "Square should still be in scene"
        assert circle not in self.mobjects, "Circle should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        print("✓ Test 1 passed: Basic clear_all_except works")
        
        # Test 2: Clear all (keep nothing)
        self.clear_all_except()
        self.wait(0.5)
        
        # Only the camera frame should remain
        non_frame_mobs = [m for m in self.mobjects if m != self.camera.frame]
        assert len(non_frame_mobs) == 0, "All mobjects should be removed"
        
        print("✓ Test 2 passed: clear_all_except() with no args clears everything")
        
        # Test 3: Add new mobjects and test again
        new_circle = Circle(color=YELLOW).scale(0.5)
        new_square = Square(color=PURPLE).scale(0.5).shift(RIGHT)
        new_text = Text("Test", font_size=20).to_edge(DOWN)
        
        self.add(new_circle, new_square, new_text)
        self.wait(1)
        
        # Keep only the circle
        self.clear_all_except(new_circle)
        self.wait(1)
        
        assert new_circle in self.mobjects, "New circle should remain"
        assert new_square not in self.mobjects, "New square should be removed"
        assert new_text not in self.mobjects, "New text should be removed"
        
        print("✓ Test 3 passed: Selective keeping works correctly")
        
        # Add final message
        success_text = Text("All tests passed!", color=GREEN)
        self.add(success_text)
        self.wait(1)
        
        print("✓ All Scene tests passed!")


class TestClearAllExceptInteractive(InteractiveScene):
    """Test the clear_all_except method for InteractiveScene"""
    
    def construct(self):
        # Create several mobjects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Text("Interactive Test", font_size=24).to_edge(UP)
        
        # Add all mobjects
        self.add(circle, square, triangle, text)
        self.wait(1)
        
        # Clear all except the text and square
        self.clear_all_except(text, square)
        self.wait(1)
        
        # Verify that only text and square remain (excluding interactive elements)
        regular_mobs = [m for m in self.mobjects 
                       if m not in [self.camera.frame, self.selection_highlight]]
        
        assert text in regular_mobs, "Text should still be in scene"
        assert square in regular_mobs, "Square should still be in scene"
        assert circle not in self.mobjects, "Circle should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        print("✓ Interactive Test 1 passed: Basic clear_all_except works")
        
        # Test 2: Verify selection search set is regenerated
        initial_search_set_size = len(self.selection_search_set)
        assert initial_search_set_size > 0, "Selection search set should not be empty"
        
        print(f"✓ Interactive Test 2 passed: Selection search set regenerated (size: {initial_search_set_size})")
        
        # Test 3: Clear all
        self.clear_all_except()
        self.wait(0.5)
        
        regular_mobs = [m for m in self.mobjects 
                       if m not in [self.camera.frame, self.selection_highlight]]
        assert len(regular_mobs) == 0, "All regular mobjects should be removed"
        
        print("✓ Interactive Test 3 passed: clear_all_except() with no args works")
        
        # Add final message
        success_text = Text("Interactive tests passed!", color=GREEN, font_size=30)
        self.add(success_text)
        self.wait(1)
        
        print("✓ All InteractiveScene tests passed!")


if __name__ == "__main__":
    # Run tests
    import sys
    
    print("=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    
    try:
        # Test Scene
        scene1 = TestClearAllExceptScene()
        scene1.run()
        print("\n✓✓✓ Scene tests completed successfully!\n")
    except Exception as e:
        print(f"\n✗✗✗ Scene test failed: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("=" * 60)
    print("Testing InteractiveScene.clear_all_except()")
    print("=" * 60)
    
    try:
        # Test InteractiveScene
        scene2 = TestClearAllExceptInteractive()
        scene2.run()
        print("\n✓✓✓ InteractiveScene tests completed successfully!\n")
    except Exception as e:
        print(f"\n✗✗✗ InteractiveScene test failed: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
