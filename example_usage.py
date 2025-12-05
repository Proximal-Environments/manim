#!/usr/bin/env python3
"""
Example usage of the clear_all_except method in ManimGL

This script demonstrates practical use cases for the new clear_all_except method.
"""

from manimlib import Scene, Square, Circle, Triangle, Text, VGroup
from manimlib.constants import (
    RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE,
    LEFT, RIGHT, UP, DOWN, ORIGIN
)


class Example1_SimpleTransition(Scene):
    """
    Example 1: Simple scene transition
    Shows how to transition between different sets of objects while keeping some constant.
    """
    def construct(self):
        # Title that persists throughout
        title = Text("Persistent Title", font_size=36)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # First set of objects
        label1 = Text("Scene 1", font_size=24).next_to(title, DOWN)
        self.add(label1)
        
        obj1 = Circle(color=RED).shift(LEFT * 2)
        obj2 = Square(color=BLUE)
        obj3 = Triangle(color=GREEN).shift(RIGHT * 2)
        
        self.add(obj1, obj2, obj3)
        self.wait(2)
        
        # Transition to Scene 2 - keep only title and middle object
        self.clear_all_except(title, obj2)
        
        label2 = Text("Scene 2", font_size=24).next_to(title, DOWN)
        self.add(label2)
        
        new_obj1 = Triangle(color=YELLOW).shift(LEFT * 2)
        new_obj2 = Circle(color=PURPLE).shift(RIGHT * 2)
        
        self.add(new_obj1, new_obj2)
        self.wait(2)


class Example2_LayeredReveal(Scene):
    """
    Example 2: Layered reveal
    Demonstrates revealing content layer by layer.
    """
    def construct(self):
        # Background that stays
        background = Square(
            side_length=8,
            fill_color=BLUE,
            fill_opacity=0.1,
            stroke_width=0
        )
        self.add(background)
        
        # Layer 1
        layer1_title = Text("Layer 1: Introduction", font_size=30)
        layer1_title.to_edge(UP)
        layer1_content = VGroup(
            Circle(color=RED),
            Square(color=BLUE),
        ).arrange(RIGHT, buff=1)
        
        self.add(layer1_title, layer1_content)
        self.wait(2)
        
        # Clear and show Layer 2
        self.clear_all_except(background)
        
        layer2_title = Text("Layer 2: Details", font_size=30)
        layer2_title.to_edge(UP)
        layer2_content = VGroup(
            Triangle(color=GREEN),
            Circle(color=YELLOW),
            Square(color=PURPLE),
        ).arrange(RIGHT, buff=0.5)
        
        self.add(layer2_title, layer2_content)
        self.wait(2)
        
        # Clear and show Layer 3
        self.clear_all_except(background)
        
        layer3_title = Text("Layer 3: Conclusion", font_size=30)
        layer3_title.to_edge(UP)
        layer3_content = Text("Thank you!", font_size=48)
        
        self.add(layer3_title, layer3_content)
        self.wait(2)


class Example3_ComparisonView(Scene):
    """
    Example 3: Comparison view
    Shows before and after states with a persistent comparison label.
    """
    def construct(self):
        # Setup comparison labels
        before_label = Text("Before", font_size=30, color=RED)
        before_label.to_edge(UP).shift(LEFT * 3)
        
        after_label = Text("After", font_size=30, color=GREEN)
        after_label.to_edge(UP).shift(RIGHT * 3)
        
        divider = Triangle(color=YELLOW).scale(0.5).to_edge(UP)
        
        self.add(before_label, divider, after_label)
        self.wait(1)
        
        # Before state
        before_obj = Circle(color=RED, radius=1)
        before_obj.shift(LEFT * 3)
        self.add(before_obj)
        self.wait(1)
        
        # Transform to after state
        self.clear_all_except(before_label, divider, after_label)
        
        after_obj = Square(color=GREEN, side_length=2)
        after_obj.shift(RIGHT * 3)
        self.add(after_obj)
        self.wait(2)


class Example4_MethodChaining(Scene):
    """
    Example 4: Method chaining
    Demonstrates using clear_all_except in a method chain.
    """
    def construct(self):
        # Initial objects
        obj1 = Circle(color=RED).shift(LEFT)
        obj2 = Square(color=BLUE)
        obj3 = Triangle(color=GREEN).shift(RIGHT)
        
        self.add(obj1, obj2, obj3)
        self.wait(1)
        
        # Chain multiple operations
        new_obj = Circle(color=YELLOW).shift(UP * 2)
        
        # Clear all except obj2, then add new_obj, then wait
        self.clear_all_except(obj2).add(new_obj)
        self.wait(2)


class Example5_ProgressiveClearing(Scene):
    """
    Example 5: Progressive clearing
    Shows how to progressively reduce objects on screen.
    """
    def construct(self):
        title = Text("Progressive Clearing", font_size=36)
        title.to_edge(UP)
        self.add(title)
        
        # Create multiple objects
        objects = VGroup(
            Circle(color=RED),
            Square(color=BLUE),
            Triangle(color=GREEN),
            Circle(color=YELLOW),
            Square(color=PURPLE),
        ).arrange(RIGHT, buff=0.5)
        
        self.add(objects)
        self.wait(1)
        
        # Progressively clear objects
        counter = Text("5 objects", font_size=24).to_edge(DOWN)
        self.add(counter)
        self.wait(1)
        
        # Keep 4
        self.remove(counter)
        self.clear_all_except(title, *objects[:4])
        counter = Text("4 objects", font_size=24).to_edge(DOWN)
        self.add(counter)
        self.wait(1)
        
        # Keep 3
        self.remove(counter)
        self.clear_all_except(title, *objects[:3])
        counter = Text("3 objects", font_size=24).to_edge(DOWN)
        self.add(counter)
        self.wait(1)
        
        # Keep 2
        self.remove(counter)
        self.clear_all_except(title, *objects[:2])
        counter = Text("2 objects", font_size=24).to_edge(DOWN)
        self.add(counter)
        self.wait(1)
        
        # Keep 1
        self.remove(counter)
        self.clear_all_except(title, objects[0])
        counter = Text("1 object", font_size=24).to_edge(DOWN)
        self.add(counter)
        self.wait(1)
        
        # Clear all
        self.clear_all_except(title)
        final = Text("All cleared!", font_size=24).to_edge(DOWN)
        self.add(final)
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    examples = [
        ("Simple Transition", Example1_SimpleTransition),
        ("Layered Reveal", Example2_LayeredReveal),
        ("Comparison View", Example3_ComparisonView),
        ("Method Chaining", Example4_MethodChaining),
        ("Progressive Clearing", Example5_ProgressiveClearing),
    ]
    
    print("=" * 60)
    print("ManimGL clear_all_except Examples")
    print("=" * 60)
    print()
    
    for name, SceneClass in examples:
        print(f"Running: {name}")
        print("-" * 60)
        scene = SceneClass()
        scene.run()
        print()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
