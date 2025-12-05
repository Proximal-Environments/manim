#!/usr/bin/env python
"""
Demo script showing clear_all_except functionality with visual examples
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle, Rectangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import UP, DOWN, LEFT, RIGHT, RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE


class ClearAllExceptDemo(Scene):
    """
    Demo showing clear_all_except method functionality
    """
    
    def construct(self):
        # Create a title
        title = Text("clear_all_except() Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Scene 1: Create multiple objects
        scene1_text = Text("Scene 1: Create multiple shapes", font_size=36)
        scene1_text.next_to(title, DOWN)
        self.add(scene1_text)
        
        circle = Circle(color=RED, radius=0.5).shift(LEFT * 3 + DOWN * 0.5)
        square = Square(color=BLUE, side_length=1).shift(LEFT * 1 + DOWN * 0.5)
        triangle = Triangle(color=GREEN).shift(RIGHT * 1 + DOWN * 0.5)
        rect = Rectangle(color=YELLOW, width=1.5, height=1).shift(RIGHT * 3 + DOWN * 0.5)
        
        circle_label = Text("Circle", font_size=24).next_to(circle, DOWN, buff=0.2)
        square_label = Text("Square", font_size=24).next_to(square, DOWN, buff=0.2)
        triangle_label = Text("Triangle", font_size=24).next_to(triangle, DOWN, buff=0.2)
        rect_label = Text("Rectangle", font_size=24).next_to(rect, DOWN, buff=0.2)
        
        self.add(circle, square, triangle, rect)
        self.add(circle_label, square_label, triangle_label, rect_label)
        self.wait(2)
        
        # Scene 2: Keep only circle and square
        self.remove(scene1_text)
        scene2_text = Text("Scene 2: Keep only Circle and Square", font_size=36)
        scene2_text.next_to(title, DOWN)
        self.add(scene2_text)
        self.wait(1)
        
        # Use clear_all_except
        self.clear_all_except(title, scene2_text, circle, square, circle_label, square_label)
        self.wait(2)
        
        # Scene 3: Add new objects
        self.remove(scene2_text)
        scene3_text = Text("Scene 3: Add new shapes", font_size=36)
        scene3_text.next_to(title, DOWN)
        self.add(scene3_text)
        
        new_shape1 = Circle(color=PURPLE, radius=0.7).shift(RIGHT * 2 + DOWN * 0.5)
        new_shape2 = Square(color=ORANGE, side_length=1.2).shift(RIGHT * 4 + DOWN * 0.5)
        new_label1 = Text("New 1", font_size=24).next_to(new_shape1, DOWN, buff=0.2)
        new_label2 = Text("New 2", font_size=24).next_to(new_shape2, DOWN, buff=0.2)
        
        self.add(new_shape1, new_shape2, new_label1, new_label2)
        self.wait(2)
        
        # Scene 4: Keep only title and one new shape
        self.remove(scene3_text)
        scene4_text = Text("Scene 4: Keep only title and one new shape", font_size=36)
        scene4_text.next_to(title, DOWN)
        self.add(scene4_text)
        self.wait(1)
        
        self.clear_all_except(title, scene4_text, new_shape1, new_label1)
        self.wait(2)
        
        # Final scene: Clear everything except title
        self.remove(scene4_text)
        final_text = Text("Final: Clear all except title", font_size=36)
        final_text.next_to(title, DOWN)
        self.add(final_text)
        self.wait(1)
        
        self.clear_all_except(title, final_text)
        self.wait(2)
        
        # Show completion message
        complete = Text("Demo Complete!", font_size=48, color=GREEN)
        complete.next_to(final_text, DOWN, buff=1)
        self.add(complete)
        self.wait(2)


class MethodChainingDemo(Scene):
    """
    Demo showing that clear_all_except returns self for method chaining
    """
    
    def construct(self):
        title = Text("Method Chaining Demo", font_size=48)
        title.to_edge(UP)
        
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Demonstrate method chaining
        self.add(title, circle, square, triangle)
        self.wait(1)
        
        info = Text("Chaining: clear_all_except().add()", font_size=36)
        info.next_to(title, DOWN)
        self.add(info)
        self.wait(1)
        
        # Method chaining example
        new_circle = Circle(color=YELLOW, radius=1.5)
        self.clear_all_except(title, info).add(new_circle)
        
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    print("Running visual demos of clear_all_except()...")
    print("=" * 60)
    
    # Run the demo with skip_animations for faster testing
    try:
        print("\n1. Running ClearAllExceptDemo...")
        demo1 = ClearAllExceptDemo(skip_animations=True)
        demo1.run()
        print("✓ ClearAllExceptDemo completed successfully")
        
        print("\n2. Running MethodChainingDemo...")
        demo2 = MethodChainingDemo(skip_animations=True)
        demo2.run()
        print("✓ MethodChainingDemo completed successfully")
        
        print("\n" + "=" * 60)
        print("ALL DEMOS COMPLETED SUCCESSFULLY! ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"✗ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
