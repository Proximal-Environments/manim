#!/usr/bin/env python3
"""
Demonstration of the clear_all_except method
This creates a visual animation showing how the method works
"""

from manimlib import *


class DemoClearAllExcept(Scene):
    """
    Visual demonstration of clear_all_except method
    """
    
    def construct(self):
        # Create a title
        title = Text("clear_all_except() Demo", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create several objects
        circle = Circle(color=RED, radius=0.8)
        circle.shift(2.5 * LEFT)
        
        square = Square(color=BLUE, side_length=1.5)
        square.shift(0 * RIGHT)
        
        triangle = Triangle(color=GREEN)
        triangle.shift(2.5 * RIGHT)
        
        # Add labels
        label_circle = Text("Circle", font_size=24).next_to(circle, DOWN)
        label_square = Text("Square", font_size=24).next_to(square, DOWN)
        label_triangle = Text("Triangle", font_size=24).next_to(triangle, DOWN)
        
        # Show all objects
        subtitle = Text("Adding three shapes...", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        
        self.play(
            FadeIn(circle),
            FadeIn(square),
            FadeIn(triangle),
            FadeIn(label_circle),
            FadeIn(label_square),
            FadeIn(label_triangle),
        )
        self.wait(2)
        
        # Update subtitle
        self.play(FadeOut(subtitle))
        subtitle = Text("Now calling clear_all_except(circle)", font_size=30, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        # Highlight the circle
        highlight = Circle(color=YELLOW, radius=1.0).move_to(circle)
        highlight.set_stroke(width=8)
        self.play(ShowCreation(highlight))
        self.wait(1)
        
        # Use clear_all_except to keep only the circle and title
        self.play(
            FadeOut(square),
            FadeOut(triangle),
            FadeOut(label_square),
            FadeOut(label_triangle),
            FadeOut(highlight),
        )
        
        # Actually clear the scene (the fade out was just visual)
        self.clear_all_except(title, circle, label_circle, subtitle)
        
        self.wait(2)
        
        # Show that we can still add new objects
        self.play(FadeOut(subtitle))
        subtitle = Text("Scene is cleared! Only circle remains.", font_size=30, color=GREEN)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        # Add new shapes
        self.play(FadeOut(subtitle))
        subtitle = Text("We can still add new objects!", font_size=30, color=GREEN)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        
        new_square = Square(color=PURPLE, side_length=1.2)
        new_square.next_to(circle, RIGHT, buff=1)
        
        new_text = Text("New!", font_size=36, color=ORANGE)
        new_text.next_to(new_square, UP)
        
        self.play(
            FadeIn(new_square),
            FadeIn(new_text)
        )
        self.wait(2)
        
        # Final message
        self.play(
            FadeOut(subtitle),
            FadeOut(new_text)
        )
        
        final_msg = Text("clear_all_except() is useful for scene management!", 
                        font_size=28, color=WHITE)
        final_msg.to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(3)


class InteractiveDemoClearAllExcept(InteractiveScene):
    """
    Interactive demonstration showing clear_all_except with InteractiveScene
    """
    
    def construct(self):
        # Title
        title = Text("InteractiveScene Demo", font_size=42)
        title.to_edge(UP)
        self.add(title)
        
        # Create a grid of objects
        objects = VGroup()
        colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE]
        
        for i in range(3):
            for j in range(2):
                if i * 2 + j < len(colors):
                    color = colors[i * 2 + j]
                    if (i + j) % 2 == 0:
                        mob = Circle(color=color, radius=0.5)
                    else:
                        mob = Square(color=color, side_length=0.8)
                    
                    mob.shift([i * 2 - 2, j * 1.5 - 0.5, 0])
                    objects.add(mob)
        
        self.play(*[FadeIn(obj) for obj in objects])
        self.wait()
        
        # Info text
        info = Text("Keeping only the first two objects...", font_size=30, color=YELLOW)
        info.to_edge(DOWN)
        self.play(FadeIn(info))
        self.wait(1)
        
        # Highlight objects to keep
        to_keep = objects[:2]
        highlights = VGroup(*[
            Circle(radius=0.7, color=YELLOW).move_to(obj).set_stroke(width=6)
            for obj in to_keep
        ])
        
        self.play(*[ShowCreation(h) for h in highlights])
        self.wait(1)
        
        # Fade out the objects we're removing
        to_remove = objects[2:]
        self.play(
            *[FadeOut(obj) for obj in to_remove],
            FadeOut(highlights),
        )
        
        # Actually clear the scene
        self.clear_all_except(title, info, *to_keep)
        
        self.wait(1)
        
        # Update info
        self.remove(info)
        info = Text("Selection search set updated automatically!", 
                   font_size=28, color=GREEN)
        info.to_edge(DOWN)
        self.add(info)
        
        self.wait(2)


class PracticalExample(Scene):
    """
    Practical example: Clearing between different visualization stages
    """
    
    def construct(self):
        # Stage 1: Show a mathematical concept
        title = Text("Practical Use Case", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        stage_label = Text("Stage 1: Initial Setup", font_size=30, color=BLUE)
        stage_label.next_to(title, DOWN)
        self.play(FadeIn(stage_label))
        
        # Create some mathematical visualization
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            axis_config={"include_tip": True}
        )
        axes.scale(0.8)
        
        func = axes.get_graph(lambda x: np.sin(x), color=RED)
        func_label = MathTex(r"f(x) = \sin(x)", font_size=36)
        func_label.next_to(axes, RIGHT)
        
        self.play(
            ShowCreation(axes),
            ShowCreation(func),
            Write(func_label)
        )
        self.wait(2)
        
        # Stage 2: Clear and show something else, but keep the title
        self.play(FadeOut(stage_label))
        stage_label = Text("Stage 2: New Visualization", font_size=30, color=GREEN)
        stage_label.next_to(title, DOWN)
        self.play(FadeIn(stage_label))
        self.wait(0.5)
        
        # Use clear_all_except to keep only the title and stage label
        self.play(
            FadeOut(axes),
            FadeOut(func),
            FadeOut(func_label)
        )
        self.clear_all_except(title, stage_label)
        
        # Show new content
        explanation = Text(
            "clear_all_except() makes it easy to\ntransition between visualization stages",
            font_size=28,
            line_spacing=1.5
        )
        explanation.move_to(ORIGIN)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # Final stage
        self.play(FadeOut(stage_label))
        stage_label = Text("Stage 3: Conclusion", font_size=30, color=YELLOW)
        stage_label.next_to(title, DOWN)
        self.play(FadeIn(stage_label))
        
        self.play(Transform(explanation, Text(
            "This keeps your scene organized\nand code clean!",
            font_size=32,
            line_spacing=1.5,
            color=GREEN
        ).move_to(explanation)))
        
        self.wait(3)


if __name__ == "__main__":
    # You can run this script directly
    # For example: manimgl demo_clear_all_except.py DemoClearAllExcept
    pass
