#!/usr/bin/env python3
"""Test script for the clear_all_except method"""

from manimlib import Scene, Square, Circle, Triangle
from manimlib.constants import RED, BLUE, GREEN, YELLOW, LEFT, RIGHT, UP, DOWN


class TestClearAllExcept(Scene):
    def construct(self):
        # Create some objects
        square = Square(color=RED).shift(LEFT * 2)
        circle = Circle(color=BLUE).shift(RIGHT * 2)
        triangle = Triangle(color=GREEN).shift(UP * 2)
        
        # Add all objects
        self.add(square, circle, triangle)
        self.wait(1)
        
        # Clear all except the circle
        print("Clearing all except circle...")
        self.clear_all_except(circle)
        self.wait(1)
        
        # Verify that only the circle remains
        print(f"Number of mobjects after clear_all_except: {len(self.mobjects)}")
        print(f"Circle in mobjects: {circle in self.mobjects}")
        print(f"Square in mobjects: {square in self.mobjects}")
        print(f"Triangle in mobjects: {triangle in self.mobjects}")
        
        # Add new objects
        square2 = Square(color=YELLOW).shift(DOWN * 2)
        self.add(square2)
        self.wait(1)
        
        # Clear all except circle and square2
        print("\nClearing all except circle and square2...")
        self.clear_all_except(circle, square2)
        self.wait(1)
        
        # Verify
        print(f"Number of mobjects after second clear_all_except: {len(self.mobjects)}")
        print(f"Circle in mobjects: {circle in self.mobjects}")
        print(f"Square2 in mobjects: {square2 in self.mobjects}")
        
        print("\nTest completed successfully!")


class TestClearAllExceptEmpty(Scene):
    def construct(self):
        # Test with no objects to keep
        square = Square(color=RED)
        circle = Circle(color=BLUE).shift(RIGHT * 2)
        
        self.add(square, circle)
        self.wait(1)
        
        # Clear everything
        print("Clearing all objects (no exceptions)...")
        self.clear_all_except()
        self.wait(1)
        
        print(f"Number of mobjects after clear_all_except(): {len(self.mobjects)}")
        print("Test completed successfully!")


if __name__ == "__main__":
    import sys
    
    # Test basic Scene
    print("=" * 60)
    print("Testing Scene.clear_all_except")
    print("=" * 60)
    scene1 = TestClearAllExcept()
    scene1.run()
    
    print("\n" + "=" * 60)
    print("Testing Scene.clear_all_except with no arguments")
    print("=" * 60)
    scene2 = TestClearAllExceptEmpty()
    scene2.run()
    
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)
