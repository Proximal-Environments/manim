#!/usr/bin/env python
"""
Simple example demonstrating the clear_all_except method
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.constants import RED, BLUE, GREEN, UP, LEFT, RIGHT


class SimpleClearExample(Scene):
    """A simple example showing how clear_all_except works"""
    
    def construct(self):
        # Create a title that we want to keep throughout
        title = Tex("clear\\_all\\_except() Example")
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Create three shapes
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Show all three shapes
        instruction = Tex("Three shapes").scale(0.8)
        instruction.next_to(title, DOWN)
        self.add(instruction, circle, square, triangle)
        self.wait(2)
        
        # Clear all except title and square
        instruction2 = Tex("Keep only square").scale(0.8)
        instruction2.next_to(title, DOWN)
        self.clear_all_except(title, instruction2, square)
        self.wait(2)
        
        # Add new shapes and clear again
        instruction3 = Tex("Add new shapes").scale(0.8)
        instruction3.next_to(title, DOWN)
        self.clear_all_except(title, instruction3, square)
        
        new_circle = Circle(color=GREEN).shift(UP * 2)
        self.add(new_circle)
        self.wait(2)
        
        # Final clear - keep only the new circle
        final_text = Tex("Keep only new circle").scale(0.8)
        final_text.next_to(title, DOWN)
        self.clear_all_except(title, final_text, new_circle)
        self.wait(2)


if __name__ == "__main__":
    # This can be run with: manimgl example_clear_all_except.py SimpleClearExample
    pass
