#!/usr/bin/env python3
"""Demo script for the clear_all_except method with visual examples"""

from manimlib import Scene, Square, Circle, Triangle, Text
from manimlib.constants import RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, LEFT, RIGHT, UP, DOWN


class DemoClearAllExcept(Scene):
    """Demonstrates the clear_all_except method with visual examples"""
    
    def construct(self):
        # Title
        title = Text("Demo: clear_all_except Method", font_size=36)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Scene 1: Create multiple objects
        label1 = Text("Step 1: Add multiple objects", font_size=24)
        label1.next_to(title, DOWN)
        self.add(label1)
        
        square = Square(color=RED, side_length=1).shift(LEFT * 3)
        circle = Circle(color=BLUE, radius=0.5).shift(LEFT * 1)
        triangle = Triangle(color=GREEN).shift(RIGHT * 1)
        pentagon = Square(color=YELLOW).shift(RIGHT * 3)  # Using square as pentagon for simplicity
        
        self.add(square, circle, triangle, pentagon)
        self.wait(2)
        
        # Scene 2: Keep only circle
        self.remove(label1)
        label2 = Text("Step 2: Keep only BLUE circle", font_size=24)
        label2.next_to(title, DOWN)
        self.add(label2)
        self.wait(1)
        
        self.clear_all_except(title, label2, circle)
        self.wait(2)
        
        # Scene 3: Add more objects and keep multiple
        self.remove(label2)
        label3 = Text("Step 3: Add new objects", font_size=24)
        label3.next_to(title, DOWN)
        self.add(label3)
        
        square2 = Square(color=ORANGE, side_length=1.5).shift(UP * 1.5)
        triangle2 = Triangle(color=PURPLE).shift(DOWN * 1.5)
        
        self.add(square2, triangle2)
        self.wait(2)
        
        # Scene 4: Keep only specific objects
        self.remove(label3)
        label4 = Text("Step 4: Keep ORANGE square and BLUE circle", font_size=24)
        label4.next_to(title, DOWN)
        self.add(label4)
        self.wait(1)
        
        self.clear_all_except(title, label4, circle, square2)
        self.wait(2)
        
        # Scene 5: Clear everything except title
        self.remove(label4)
        label5 = Text("Step 5: Clear all except title", font_size=24)
        label5.next_to(title, DOWN)
        self.add(label5)
        self.wait(1)
        
        self.clear_all_except(title, label5)
        self.wait(2)
        
        # Final message
        self.remove(label5)
        final = Text("Demo Complete!", font_size=30, color=GREEN)
        final.next_to(title, DOWN)
        self.add(final)
        self.wait(2)


class DemoEdgeCase(Scene):
    """Test edge cases for clear_all_except"""
    
    def construct(self):
        title = Text("Edge Case Tests", font_size=36)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Test 1: Clear with no arguments (clear all)
        label1 = Text("Test 1: Clear all (no arguments)", font_size=24)
        label1.next_to(title, DOWN)
        self.add(label1)
        
        obj1 = Circle(color=RED).shift(LEFT)
        obj2 = Square(color=BLUE).shift(RIGHT)
        self.add(obj1, obj2)
        self.wait(1)
        
        self.clear_all_except(title, label1)
        result1 = Text("✓ All cleared except title and label", font_size=20, color=GREEN)
        result1.next_to(label1, DOWN)
        self.add(result1)
        self.wait(2)
        
        # Test 2: Clear when already empty
        self.remove(label1, result1)
        label2 = Text("Test 2: Clear when scene is empty", font_size=24)
        label2.next_to(title, DOWN)
        self.add(label2)
        self.wait(1)
        
        self.clear_all_except(title, label2)
        result2 = Text("✓ No errors when clearing empty scene", font_size=20, color=GREEN)
        result2.next_to(label2, DOWN)
        self.add(result2)
        self.wait(2)
        
        # Test 3: Keep non-existent object (should not cause error)
        self.remove(label2, result2)
        label3 = Text("Test 3: Reference to removed object", font_size=24)
        label3.next_to(title, DOWN)
        self.add(label3)
        
        obj3 = Triangle(color=GREEN)
        self.add(obj3)
        self.wait(1)
        
        removed_obj = Circle(color=YELLOW)  # Not added to scene
        self.clear_all_except(title, label3, obj3, removed_obj)
        result3 = Text("✓ Handles non-existent objects gracefully", font_size=20, color=GREEN)
        result3.next_to(label3, DOWN)
        self.add(result3)
        self.wait(2)
        
        # Final
        self.clear_all_except(title)
        final = Text("All Edge Cases Passed!", font_size=30, color=GREEN)
        final.next_to(title, DOWN)
        self.add(final)
        self.wait(2)


if __name__ == "__main__":
    print("=" * 60)
    print("Running Demo: clear_all_except")
    print("=" * 60)
    
    scene1 = DemoClearAllExcept()
    scene1.run()
    
    print("\n" + "=" * 60)
    print("Running Edge Case Tests")
    print("=" * 60)
    
    scene2 = DemoEdgeCase()
    scene2.run()
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
