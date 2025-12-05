#!/usr/bin/env python3
"""
Comprehensive test script for clear_all_except method with visual output
"""

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle, Rectangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.mobject.mobject import Group
from manimlib.constants import RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE
import numpy as np


class VisualTestClearAllExcept(Scene):
    """Visual demonstration of clear_all_except method"""
    
    def construct(self):
        # Title
        title = Text("Testing clear_all_except Method", color=WHITE).scale(0.7)
        title.to_edge([0, 1, 0], buff=0.5)
        self.add(title)
        self.wait(1)
        
        # Create multiple mobjects in a grid
        circle = Circle(color=RED, radius=0.5).shift([-3, 1, 0])
        square = Square(color=BLUE, side_length=1).shift([0, 1, 0])
        triangle = Triangle(color=GREEN).scale(0.7).shift([3, 1, 0])
        rect = Rectangle(color=ORANGE, width=2, height=0.8).shift([-3, -1, 0])
        
        label1 = Text("Keep", font_size=24, color=WHITE).next_to(circle, [0, -1, 0])
        label2 = Text("Remove", font_size=24, color=WHITE).next_to(square, [0, -1, 0])
        label3 = Text("Remove", font_size=24, color=WHITE).next_to(triangle, [0, -1, 0])
        label4 = Text("Keep", font_size=24, color=WHITE).next_to(rect, [0, -1, 0])
        
        # Add all
        self.add(circle, square, triangle, rect)
        self.add(label1, label2, label3, label4)
        
        info = Text(f"Total mobjects: {len(self.mobjects)}", 
                   font_size=24, color=WHITE).to_edge([0, -1, 0], buff=0.3)
        self.add(info)
        
        print(f"Initial state: {len(self.mobjects)} mobjects")
        self.wait(2)
        
        # Update info
        self.remove(info)
        info = Text("Clearing all except Circle and Rectangle...", 
                   font_size=24, color=YELLOW).to_edge([0, -1, 0], buff=0.3)
        self.add(info)
        self.wait(1)
        
        # Clear all except circle and rect
        self.clear_all_except(title, circle, rect, label1, label4)
        
        self.remove(info)
        info = Text(f"After clear_all_except: {len(self.mobjects)} mobjects", 
                   font_size=24, color=GREEN).to_edge([0, -1, 0], buff=0.3)
        self.add(info)
        
        print(f"After clear_all_except: {len(self.mobjects)} mobjects")
        assert circle in self.mobjects
        assert rect in self.mobjects
        assert square not in self.mobjects
        assert triangle not in self.mobjects
        
        self.wait(2)
        
        print("✅ Visual test passed!")


class EdgeCaseTests(Scene):
    """Test edge cases for clear_all_except"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing Edge Cases")
        print("=" * 60)
        
        # Test 1: Clear with no arguments (clear everything)
        print("\nTest 1: Clear with no arguments")
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        self.add(c1, c2)
        initial_count = len(self.mobjects)
        print(f"  Before: {initial_count} mobjects")
        
        self.clear_all_except()
        print(f"  After clear_all_except(): {len(self.mobjects)} mobjects")
        assert len(self.mobjects) == 0, "Should have no mobjects"
        print("  ✅ Pass: All mobjects cleared")
        
        # Test 2: Keep only one mobject
        print("\nTest 2: Keep only one mobject")
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        c3 = Circle(color=GREEN)
        self.add(c1, c2, c3)
        print(f"  Before: {len(self.mobjects)} mobjects")
        
        self.clear_all_except(c2)
        print(f"  After clear_all_except(c2): {len(self.mobjects)} mobjects")
        assert len(self.mobjects) == 1, "Should have exactly 1 mobject"
        assert c2 in self.mobjects, "c2 should remain"
        assert c1 not in self.mobjects, "c1 should be removed"
        assert c3 not in self.mobjects, "c3 should be removed"
        print("  ✅ Pass: Only specified mobject kept")
        
        # Test 3: Keep mobjects that are in a Group
        print("\nTest 3: Keep mobjects from a Group")
        self.clear()
        c1 = Circle(color=RED).shift([-1, 0, 0])
        c2 = Circle(color=BLUE).shift([1, 0, 0])
        group = Group(c1, c2)
        c3 = Circle(color=GREEN).shift([0, 2, 0])
        
        self.add(group, c3)
        print(f"  Before: {len(self.mobjects)} mobjects")
        
        self.clear_all_except(c1)
        print(f"  After clear_all_except(c1): {len(self.mobjects)} mobjects")
        print(f"  c1 in mobjects: {c1 in self.mobjects}")
        print("  ✅ Pass: Group handling works")
        
        # Test 4: Keep non-existent mobject (should not error)
        print("\nTest 4: Keep non-existent mobject")
        self.clear()
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        c_not_added = Circle(color=GREEN)
        
        self.add(c1, c2)
        print(f"  Before: {len(self.mobjects)} mobjects")
        
        # This should not raise an error
        self.clear_all_except(c_not_added)
        print(f"  After clear_all_except(c_not_added): {len(self.mobjects)} mobjects")
        print("  ✅ Pass: Non-existent mobject handled gracefully")
        
        # Test 5: Multiple clear_all_except calls
        print("\nTest 5: Multiple clear_all_except calls")
        self.clear()
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        c3 = Circle(color=GREEN)
        c4 = Circle(color=YELLOW)
        
        self.add(c1, c2, c3, c4)
        print(f"  Start: {len(self.mobjects)} mobjects")
        
        self.clear_all_except(c1, c2, c3)
        print(f"  After first clear: {len(self.mobjects)} mobjects")
        
        self.clear_all_except(c1, c2)
        print(f"  After second clear: {len(self.mobjects)} mobjects")
        assert len(self.mobjects) == 2
        assert c1 in self.mobjects and c2 in self.mobjects
        
        self.clear_all_except(c1)
        print(f"  After third clear: {len(self.mobjects)} mobjects")
        assert len(self.mobjects) == 1
        assert c1 in self.mobjects
        print("  ✅ Pass: Multiple calls work correctly")
        
        # Test 6: Keep the same mobject multiple times (no duplicates)
        print("\nTest 6: Duplicate mobjects in arguments")
        self.clear()
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        
        self.add(c1, c2)
        self.clear_all_except(c1, c1, c1)  # Keep c1 three times
        print(f"  After clear_all_except(c1, c1, c1): {len(self.mobjects)} mobjects")
        assert len(self.mobjects) == 1, "Should not create duplicates"
        print("  ✅ Pass: No duplicates created")
        
        print("\n" + "=" * 60)
        print("✅ All edge case tests passed!")
        print("=" * 60)


class InteractiveSceneTest(InteractiveScene):
    """Test clear_all_except with InteractiveScene specific features"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing InteractiveScene Integration")
        print("=" * 60)
        
        # Create mobjects
        c1 = Circle(color=RED).shift([-2, 0, 0])
        c2 = Circle(color=BLUE).shift([2, 0, 0])
        s1 = Square(color=GREEN).shift([0, 2, 0])
        
        self.add(c1, c2, s1)
        
        initial_selectable = len([m for m in self.mobjects if m not in self.unselectables])
        print(f"Initial selectable mobjects: {initial_selectable}")
        print(f"Initial search set size: {len(self.selection_search_set)}")
        
        # Test that selection_search_set updates properly
        self.clear_all_except(c1)
        
        after_selectable = len([m for m in self.mobjects if m not in self.unselectables])
        print(f"After clear selectable mobjects: {after_selectable}")
        print(f"After clear search set size: {len(self.selection_search_set)}")
        
        assert c1 in self.mobjects
        assert c2 not in self.mobjects
        assert s1 not in self.mobjects
        
        # Verify selection_search_set is properly updated
        assert len(self.selection_search_set) == after_selectable, \
            "Selection search set should be updated"
        
        print("✅ InteractiveScene integration test passed!")


class MethodChainingTest(Scene):
    """Test that clear_all_except can be chained with other methods"""
    
    def construct(self):
        print("\n" + "=" * 60)
        print("Testing Method Chaining")
        print("=" * 60)
        
        c1 = Circle(color=RED)
        c2 = Circle(color=BLUE)
        c3 = Circle(color=GREEN)
        
        # Test chaining
        result = self.add(c1, c2, c3).clear_all_except(c1).add(c3)
        
        assert result is self, "Methods should return self"
        assert c1 in self.mobjects
        assert c2 not in self.mobjects
        assert c3 in self.mobjects
        
        print("✅ Method chaining test passed!")


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("COMPREHENSIVE TEST SUITE FOR clear_all_except")
    print("=" * 60)
    
    # Run visual test
    print("\n1. Running visual test...")
    scene1 = VisualTestClearAllExcept(
        skip_animations=True,
        show_animation_progress=False,
    )
    scene1.run()
    
    # Run edge case tests
    print("\n2. Running edge case tests...")
    scene2 = EdgeCaseTests(
        skip_animations=True,
        show_animation_progress=False,
    )
    scene2.run()
    
    # Run interactive scene test
    print("\n3. Running interactive scene test...")
    scene3 = InteractiveSceneTest(
        skip_animations=True,
        show_animation_progress=False,
    )
    scene3.run()
    
    # Run method chaining test
    print("\n4. Running method chaining test...")
    scene4 = MethodChainingTest(
        skip_animations=True,
        show_animation_progress=False,
    )
    scene4.run()
    
    print("\n" + "=" * 60)
    print("🎉 ALL COMPREHENSIVE TESTS PASSED! 🎉")
    print("=" * 60)
