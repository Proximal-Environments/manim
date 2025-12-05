#!/usr/bin/env python3
"""
Demonstration of the clear_all_except method in both Scene and InteractiveScene
"""

from manimlib import Scene, InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle, Rectangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import UP, DOWN, LEFT, RIGHT, RED, BLUE, GREEN, YELLOW


class DemoClearAllExceptScene(Scene):
    """
    Demonstrates the clear_all_except method in a regular Scene.
    This example shows how to clear the scene while keeping specific objects.
    """
    
    def construct(self):
        # Create and display some shapes
        title = Text("clear_all_except() Demo").to_edge(UP)
        circle = Circle(color=RED).shift(2*LEFT + UP)
        square = Square(color=BLUE).shift(2*RIGHT + UP)
        triangle = Triangle(color=GREEN).shift(2*LEFT + DOWN)
        rectangle = Rectangle(color=YELLOW).shift(2*RIGHT + DOWN)
        
        # Add all objects
        self.add(title, circle, square, triangle, rectangle)
        self.wait(1)
        
        # Clear everything except the circle and title
        info_text = Text("Keeping only circle...", font_size=36).next_to(title, DOWN)
        self.add(info_text)
        self.wait(1)
        
        self.clear_all_except(circle, title, info_text)
        self.wait(1)
        
        # Add new shapes
        new_text = Text("Adding new shapes...", font_size=36).next_to(title, DOWN)
        self.add(new_text)
        self.wait(0.5)
        
        square2 = Square(color=BLUE).shift(RIGHT)
        triangle2 = Triangle(color=GREEN).shift(LEFT)
        self.add(square2, triangle2)
        self.wait(1)
        
        # Clear all except title
        final_text = Text("Clearing all!", font_size=36).next_to(title, DOWN)
        self.add(final_text)
        self.wait(1)
        
        self.clear_all_except(title, final_text)
        self.wait(1)


class DemoClearAllExceptInteractive(InteractiveScene):
    """
    Demonstrates the clear_all_except method in an InteractiveScene.
    Shows that interactive elements are properly managed.
    """
    
    def construct(self):
        # Create and display some shapes
        title = Text("Interactive clear_all_except()").scale(0.7).to_edge(UP)
        
        shapes = []
        colors = [RED, BLUE, GREEN, YELLOW]
        positions = [2*LEFT + UP, 2*RIGHT + UP, 2*LEFT + DOWN, 2*RIGHT + DOWN]
        
        for i, (color, pos) in enumerate(zip(colors, positions)):
            shape = Circle(color=color, radius=0.5).shift(pos)
            shapes.append(shape)
        
        # Add all objects
        self.add(title, *shapes)
        self.wait(1)
        
        # Demonstrate clearing with interactive scene
        info = Text("Try selecting objects!", font_size=24).next_to(title, DOWN)
        self.add(info)
        self.wait(1)
        
        # Clear all except first two shapes and text
        info2 = Text("Clearing some objects...", font_size=24).next_to(title, DOWN)
        self.add(info2)
        self.wait(0.5)
        
        self.clear_all_except(title, info2, shapes[0], shapes[1])
        self.wait(1)
        
        # Note that selection_search_set is automatically updated
        info3 = Text(f"Search set has {len(self.selection_search_set)} items", 
                     font_size=24).next_to(title, DOWN)
        self.add(info3)
        self.wait(2)


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Running Scene Demo")
    print("="*60 + "\n")
    
    scene = DemoClearAllExceptScene(skip_animations=False)
    scene.run()
    
    print("\n" + "="*60)
    print("Running InteractiveScene Demo")
    print("="*60 + "\n")
    
    scene2 = DemoClearAllExceptInteractive(skip_animations=False)
    scene2.run()
    
    print("\n" + "="*60)
    print("✅ Demos completed successfully!")
    print("="*60 + "\n")
