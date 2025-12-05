#!/usr/bin/env python3
"""Test script for the clear_all_except method in InteractiveScene"""

from manimlib import InteractiveScene, Square, Circle, Triangle
from manimlib.constants import RED, BLUE, GREEN, YELLOW, LEFT, RIGHT, UP, DOWN


class TestInteractiveClearAllExcept(InteractiveScene):
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
        
        # Verify that only the circle remains (plus selection_highlight)
        print(f"Number of mobjects after clear_all_except: {len(self.mobjects)}")
        print(f"Circle in mobjects: {circle in self.mobjects}")
        print(f"Square in mobjects: {square in self.mobjects}")
        print(f"Triangle in mobjects: {triangle in self.mobjects}")
        print(f"Selection highlight in mobjects: {self.selection_highlight in self.mobjects}")
        
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
        print(f"Selection highlight in mobjects: {self.selection_highlight in self.mobjects}")
        
        print("\nTest completed successfully!")


if __name__ == "__main__":
    print("=" * 60)
    print("Testing InteractiveScene.clear_all_except")
    print("=" * 60)
    scene = TestInteractiveClearAllExcept()
    scene.run()
    
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)
