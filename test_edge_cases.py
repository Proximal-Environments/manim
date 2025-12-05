#!/usr/bin/env python
"""
Edge case tests for clear_all_except method
"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square
from manimlib.mobject.mobject import Group
from manimlib.constants import LEFT, RIGHT, RED, BLUE, GREEN


class TestEdgeCases(Scene):
    """Test edge cases for clear_all_except method"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing Edge Cases")
        print("=" * 60)
        
        # Test 1: Empty scene
        print("\nTest 1: clear_all_except on empty scene (except frame)")
        self.clear_all_except()
        non_frame_mobs = [m for m in self.get_mobjects() if m != self.camera.frame]
        assert len(non_frame_mobs) == 0, "Scene should be empty except for frame"
        print("✓ Empty scene test passed")
        
        # Test 2: Clear with no arguments (remove all)
        print("\nTest 2: Clear all objects with no arguments")
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        self.add(circle, square)
        assert circle in self.get_mobjects()
        assert square in self.get_mobjects()
        
        self.clear_all_except()
        non_frame_mobs = [m for m in self.get_mobjects() if m != self.camera.frame]
        assert len(non_frame_mobs) == 0, "All objects should be removed"
        print("✓ Clear all test passed")
        
        # Test 3: Keep object that wasn't in scene
        print("\nTest 3: Keep object that wasn't in scene originally")
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        extra_circle = Circle(color=GREEN)  # Not added to scene
        
        self.add(circle, square)
        self.clear_all_except(circle, extra_circle)  # extra_circle wasn't in scene
        
        assert circle in self.get_mobjects(), "Circle should be kept"
        assert extra_circle in self.get_mobjects(), "Extra circle should be added"
        assert square not in self.get_mobjects(), "Square should be removed"
        print("✓ Keep non-existent object test passed")
        
        # Test 4: Groups
        print("\nTest 4: Working with groups")
        self.clear()
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        group = Group(circle, square)
        self.add(group)
        
        # Keep the group
        self.clear_all_except(group)
        assert group in self.get_mobjects(), "Group should be kept"
        print("✓ Group test passed")
        
        # Test 5: Duplicate objects in arguments
        print("\nTest 5: Duplicate objects in arguments")
        self.clear()
        circle = Circle(color=RED)
        self.add(circle)
        
        # Pass the same object multiple times
        # clear_all_except should deduplicate automatically
        self.clear_all_except(circle, circle, circle)
        assert circle in self.get_mobjects(), "Circle should be kept"
        non_frame_mobs = [m for m in self.get_mobjects() if m != self.camera.frame]
        assert non_frame_mobs.count(circle) == 1, "Circle should appear only once (deduplicated)"
        print("✓ Duplicate arguments test passed")
        
        # Test 6: Method chaining
        print("\nTest 6: Method chaining")
        self.clear()
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        self.add(circle, square)
        
        # Chain methods
        result = self.clear_all_except(circle)
        assert result is self, "Should return self for chaining"
        assert circle in self.get_mobjects(), "Circle should be kept"
        assert square not in self.get_mobjects(), "Square should be removed"
        print("✓ Method chaining test passed")
        
        # Test 7: Camera frame preservation
        print("\nTest 7: Camera frame is always preserved")
        self.clear()
        circle = Circle(color=RED)
        self.add(circle)
        
        frame = self.camera.frame
        self.clear_all_except()  # Clear everything
        assert frame in self.get_mobjects(), "Camera frame should always be preserved"
        print("✓ Camera frame preservation test passed")
        
        print("\n" + "=" * 60)
        print("ALL EDGE CASE TESTS PASSED! ✓")
        print("=" * 60)


class TestInteractiveEdgeCases(InteractiveScene):
    """Test edge cases specific to InteractiveScene"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing InteractiveScene Edge Cases")
        print("=" * 60)
        
        # Test 1: Selection highlight is preserved
        print("\nTest 1: Selection highlight handling")
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        self.add(circle, square)
        
        # Selection highlight should be in mobjects
        assert self.selection_highlight in self.get_mobjects()
        
        self.clear_all_except(circle)
        
        # Selection highlight should still be there
        assert self.selection_highlight in self.get_mobjects(), \
            "Selection highlight should be preserved"
        assert circle in self.get_mobjects(), "Circle should be kept"
        assert square not in self.get_mobjects(), "Square should be removed"
        print("✓ Selection highlight test passed")
        
        # Test 2: Selection search set regeneration
        print("\nTest 2: Selection search set is regenerated")
        self.clear()
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        self.add(circle, square)
        
        initial_search_set_size = len(self.selection_search_set)
        
        self.clear_all_except(circle)
        
        final_search_set_size = len(self.selection_search_set)
        
        # Search set should be smaller now
        assert final_search_set_size < initial_search_set_size, \
            "Selection search set should be regenerated and smaller"
        print(f"  Initial search set size: {initial_search_set_size}")
        print(f"  Final search set size: {final_search_set_size}")
        print("✓ Selection search set regeneration test passed")
        
        print("\n" + "=" * 60)
        print("ALL INTERACTIVE EDGE CASE TESTS PASSED! ✓")
        print("=" * 60)


if __name__ == "__main__":
    import sys
    
    try:
        # Test basic Scene
        test_scene = TestEdgeCases(
            skip_animations=True,
            show_animation_progress=False
        )
        test_scene.run()
        
        # Test InteractiveScene
        test_interactive = TestInteractiveEdgeCases(
            skip_animations=True,
            show_animation_progress=False
        )
        test_interactive.run()
        
        print("\n" + "=" * 60)
        print("COMPLETE TEST SUITE PASSED! ✓✓✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
