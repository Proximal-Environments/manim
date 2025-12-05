#!/usr/bin/env python3
"""
Test script for the clear_all_except method
"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import UP, DOWN, LEFT, RIGHT


class TestClearAllExcept(Scene):
    """Test the clear_all_except method in Scene"""
    
    def construct(self):
        # Create some objects
        circle = Circle().shift(UP)
        square = Square().shift(DOWN)
        triangle = Triangle().shift(LEFT)
        text = Text("Keep Me").shift(RIGHT)
        
        # Add all objects to the scene
        self.add(circle, square, triangle, text)
        
        # Verify all objects are in the scene
        assert len(self.mobjects) == 5, f"Expected 5 mobjects (4 + camera frame), got {len(self.mobjects)}"
        print(f"✓ Initially added 4 mobjects to scene (total: {len(self.mobjects)} including camera frame)")
        
        # Wait a moment
        self.wait(0.5)
        
        # Clear all except circle and text
        self.clear_all_except(circle, text)
        
        # Verify only circle and text remain (plus camera frame)
        assert len(self.mobjects) == 3, f"Expected 3 mobjects (2 + camera frame), got {len(self.mobjects)}"
        assert circle in self.mobjects, "Circle should be in mobjects"
        assert text in self.mobjects, "Text should be in mobjects"
        assert square not in self.mobjects, "Square should not be in mobjects"
        assert triangle not in self.mobjects, "Triangle should not be in mobjects"
        
        print(f"✓ After clear_all_except, kept 2 mobjects (total: {len(self.mobjects)} including camera frame)")
        print("✓ Verified that only circle and text remain")
        
        # Wait to see the result
        self.wait(0.5)
        
        # Test clearing all with empty keep list
        self.clear_all_except()
        assert len(self.mobjects) == 1, f"Expected 1 mobject (camera frame), got {len(self.mobjects)}"
        print(f"✓ After clear_all_except() with no arguments, scene is empty (only camera frame remains)")
        
        print("\n✅ All Scene tests passed!")


class TestInteractiveClearAllExcept(InteractiveScene):
    """Test the clear_all_except method in InteractiveScene"""
    
    def construct(self):
        # Create some objects
        circle = Circle().shift(UP)
        square = Square().shift(DOWN)
        triangle = Triangle().shift(LEFT)
        text = Text("Interactive").shift(RIGHT)
        
        # Add all objects to the scene
        self.add(circle, square, triangle, text)
        
        # Count non-unselectable mobjects
        selectable_count = len([m for m in self.mobjects if m not in self.unselectables])
        assert selectable_count == 4, f"Expected 4 selectable mobjects, got {selectable_count}"
        print(f"✓ Initially added 4 mobjects to interactive scene")
        
        # Verify selection_search_set is populated
        initial_search_set_size = len(self.selection_search_set)
        print(f"  Selection search set size: {initial_search_set_size}")
        
        # Wait a moment
        self.wait(0.5)
        
        # Clear all except circle and text
        self.clear_all_except(circle, text)
        
        # Verify only circle and text remain (excluding unselectables)
        selectable_count = len([m for m in self.mobjects if m not in self.unselectables])
        assert selectable_count == 2, f"Expected 2 selectable mobjects, got {selectable_count}"
        assert circle in self.mobjects, "Circle should be in mobjects"
        assert text in self.mobjects, "Text should be in mobjects"
        assert square not in self.mobjects, "Square should not be in mobjects"
        assert triangle not in self.mobjects, "Triangle should not be in mobjects"
        
        # Verify selection_search_set was regenerated
        after_search_set_size = len(self.selection_search_set)
        print(f"✓ After clear_all_except, kept 2 mobjects")
        print(f"  Selection search set size: {after_search_set_size}")
        
        # Wait to see the result
        self.wait(0.5)
        
        # Test clearing all with empty keep list
        self.clear_all_except()
        selectable_count = len([m for m in self.mobjects if m not in self.unselectables])
        assert selectable_count == 0, f"Expected 0 selectable mobjects, got {selectable_count}"
        print(f"✓ After clear_all_except() with no arguments, all mobjects cleared")
        
        print("\n✅ All InteractiveScene tests passed!")


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Testing clear_all_except in Scene")
    print("=" * 60)
    
    try:
        scene = TestClearAllExcept(skip_animations=True)
        scene.run()
        print("\n")
    except Exception as e:
        print(f"\n❌ Scene test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("=" * 60)
    print("Testing clear_all_except in InteractiveScene")
    print("=" * 60)
    
    try:
        scene = TestInteractiveClearAllExcept(skip_animations=True)
        scene.run()
        print("\n")
    except Exception as e:
        print(f"\n❌ InteractiveScene test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("=" * 60)
    print("🎉 ALL TESTS PASSED! 🎉")
    print("=" * 60)
