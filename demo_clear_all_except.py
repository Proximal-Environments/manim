#!/usr/bin/env python
"""
Visual demonstration of the clear_all_except method
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle, Line
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.constants import RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE
from manimlib.constants import UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR


class DemoClearAllExcept(Scene):
    """
    Demonstrates the clear_all_except method with visual examples
    """
    
    def construct(self):
        # Create a title
        title = Tex("clear\\_all\\_except() Demo").scale(1.5)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Create several shapes
        shapes = [
            Circle(color=RED).shift(UL * 2),
            Square(color=BLUE).shift(UP * 2),
            Triangle(color=GREEN).shift(UR * 2),
            Circle(color=YELLOW).shift(LEFT * 2),
            Square(color=ORANGE).shift(RIGHT * 2),
            Triangle(color=PURPLE).shift(DL * 2),
        ]
        
        # Add all shapes
        self.add(*shapes)
        self.wait(2)
        
        # Clear all except the first three shapes
        subtitle1 = Tex("Keep first 3 shapes").scale(0.8)
        subtitle1.next_to(title, DOWN)
        self.add(subtitle1)
        self.wait(1)
        
        self.clear_all_except(title, subtitle1, shapes[0], shapes[1], shapes[2])
        self.wait(2)
        
        # Add back all shapes
        self.remove(subtitle1)
        subtitle2 = Tex("Add all shapes back").scale(0.8)
        subtitle2.next_to(title, DOWN)
        self.add(subtitle2, *shapes[3:])
        self.wait(2)
        
        # Keep only yellow circle
        self.remove(subtitle2)
        subtitle3 = Tex("Keep only yellow circle").scale(0.8)
        subtitle3.next_to(title, DOWN)
        self.add(subtitle3)
        self.wait(1)
        
        self.clear_all_except(title, subtitle3, shapes[3])  # Yellow circle
        self.wait(2)
        
        # Clear everything except title
        self.remove(subtitle3)
        subtitle4 = Tex("Clear all user objects").scale(0.8)
        subtitle4.next_to(title, DOWN)
        self.add(subtitle4)
        self.wait(1)
        
        self.clear_all_except(title, subtitle4)
        self.wait(2)
        
        # Show that we can add new objects
        final_text = Tex("Add new content").scale(0.8)
        final_text.next_to(title, DOWN)
        self.clear_all_except(title, final_text)
        
        new_shapes = [
            Circle(color=RED).shift(LEFT),
            Square(color=BLUE),
            Triangle(color=GREEN).shift(RIGHT),
        ]
        self.add(*new_shapes)
        self.wait(2)
        
        # Final clear
        end_text = Tex("Done!").scale(2)
        self.clear_all_except(end_text)
        self.wait(2)


class DemoClearAllExceptInteractive(Scene):
    """
    A simpler demo that can work with InteractiveScene as well
    """
    
    def construct(self):
        # Create title
        title = Tex("Interactive Demo").to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Create three circles
        c1 = Circle(color=RED).shift(LEFT * 2)
        c2 = Circle(color=GREEN)
        c3 = Circle(color=BLUE).shift(RIGHT * 2)
        
        self.add(c1, c2, c3)
        self.wait(1)
        
        # Keep only the middle one
        label = Tex("Keep only green").scale(0.7)
        label.next_to(title, DOWN)
        self.add(label)
        self.wait(0.5)
        
        self.clear_all_except(title, label, c2)
        self.wait(1)
        
        # Add new circles
        self.remove(label)
        label2 = Tex("Add new circles").scale(0.7)
        label2.next_to(title, DOWN)
        self.add(label2)
        
        c4 = Circle(color=YELLOW).shift(UP * 2)
        c5 = Circle(color=ORANGE).shift(DOWN * 2)
        self.add(c4, c5)
        self.wait(1)
        
        # Keep only new circles
        self.remove(label2)
        label3 = Tex("Keep only new circles").scale(0.7)
        label3.next_to(title, DOWN)
        self.add(label3)
        self.wait(0.5)
        
        self.clear_all_except(title, label3, c4, c5)
        self.wait(2)


if __name__ == "__main__":
    # Run the demo
    import sys
    import subprocess
    
    # Choose which demo to run
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        scene_name = "DemoClearAllExceptInteractive"
    else:
        scene_name = "DemoClearAllExcept"
    
    # Run with manimgl
    cmd = ["manimgl", __file__, scene_name, "--write"]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd)
