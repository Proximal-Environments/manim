#!/usr/bin/env python
"""Test edge cases for clear_all_except method"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.mobject import Group
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT


class TestEdgeCases(Scene):
    """Test edge cases for clear_all_except"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing Edge Cases")
        print("=" * 60)
        
        # Test 1: Clear when scene is already empty
        print("\n1. Testing clear_all_except on empty scene...")
        self.clear_all_except()
        assert len([m for m in self.mobjects if not hasattr(m, 'is_fixed_in_frame')]) == 0
        print("   ✓ Empty scene cleared successfully")
        
        # Test 2: Keep objects that don't exist in scene
        print("\n2. Testing with objects not in scene...")
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        self.add(circle)
        self.clear_all_except(square)  # square is not in scene
        assert circle not in self.mobjects
        assert square not in self.mobjects
        print("   ✓ Handled non-existent objects correctly")
        
        # Test 3: Keep grouped objects
        print("\n3. Testing with grouped objects...")
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        group = Group(circle, square)
        self.add(group, triangle)
        
        # Keep the group
        self.clear_all_except(group)
        assert group in self.mobjects
        assert triangle not in self.mobjects
        print("   ✓ Grouped objects handled correctly")
        
        # Test 4: Multiple calls
        print("\n4. Testing multiple consecutive calls...")
        self.clear()
        c1 = Circle(color=RED).shift(2 * LEFT)
        c2 = Circle(color=BLUE)
        c3 = Circle(color=GREEN).shift(2 * RIGHT)
        
        self.add(c1, c2, c3)
        assert len([m for m in self.mobjects if isinstance(m, Circle)]) == 3
        
        self.clear_all_except(c1, c2)
        assert len([m for m in self.mobjects if isinstance(m, Circle)]) == 2
        assert c3 not in self.mobjects
        
        self.clear_all_except(c1)
        assert len([m for m in self.mobjects if isinstance(m, Circle)]) == 1
        assert c2 not in self.mobjects
        
        self.clear_all_except()
        assert len([m for m in self.mobjects if isinstance(m, Circle)]) == 0
        print("   ✓ Multiple consecutive calls work correctly")
        
        # Test 5: Keep the same object multiple times (should still work)
        print("\n5. Testing duplicate objects in arguments...")
        circle = Circle(color=RED)
        self.add(circle)
        self.clear_all_except(circle, circle, circle)  # Duplicates
        assert circle in self.mobjects
        print("   ✓ Duplicate arguments handled correctly")
        
        # Test 6: Clear and re-add pattern
        print("\n6. Testing clear and re-add pattern...")
        self.clear()
        original = Square(color=BLUE)
        self.add(original)
        
        for i in range(3):
            temp = Circle(color=RED)
            self.add(temp)
            self.clear_all_except(original)
            assert original in self.mobjects
            assert temp not in self.mobjects
        print("   ✓ Clear and re-add pattern works correctly")
        
        print("\n" + "=" * 60)
        print("✅ All edge case tests passed!")
        print("=" * 60)


class TestInteractiveEdgeCases(InteractiveScene):
    """Test edge cases specific to InteractiveScene"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing InteractiveScene Edge Cases")
        print("=" * 60)
        
        # Test 1: Selection is cleared when objects are removed
        print("\n1. Testing selection cleanup...")
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        
        self.add(circle, square)
        self.add_to_selection(circle, square)
        assert len(self.selection) == 2
        
        self.clear_all_except(square)
        assert len(self.selection) == 0, "Selection should be empty"
        assert circle not in self.mobjects
        print("   ✓ Selection cleared correctly")
        
        # Test 2: Selection search set is regenerated
        print("\n2. Testing selection search set regeneration...")
        initial_search_set_size = len(self.selection_search_set)
        
        triangle = Triangle(color=GREEN)
        self.add(triangle)
        new_search_set_size = len(self.selection_search_set)
        assert new_search_set_size > initial_search_set_size
        
        self.clear_all_except(square)
        final_search_set_size = len(self.selection_search_set)
        assert final_search_set_size < new_search_set_size
        print("   ✓ Selection search set regenerated correctly")
        
        print("\n" + "=" * 60)
        print("✅ All InteractiveScene edge case tests passed!")
        print("=" * 60)


if __name__ == "__main__":
    import sys
    
    # Test basic Scene edge cases
    scene1 = TestEdgeCases(
        skip_animations=True,
        show_animation_progress=False
    )
    try:
        scene1.run()
    except Exception as e:
        print(f"❌ Error in Scene edge case test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Test InteractiveScene edge cases
    scene2 = TestInteractiveEdgeCases(
        skip_animations=True,
        show_animation_progress=False
    )
    try:
        scene2.run()
    except Exception as e:
        print(f"❌ Error in InteractiveScene edge case test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("🎉 All edge case tests completed successfully!")
    print("=" * 60)
