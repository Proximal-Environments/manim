#!/usr/bin/env python
"""Demonstration of the clear_all_except method"""

from manimlib import *

class DemoClearAllExceptBasic(Scene):
    """Basic demonstration of clear_all_except"""
    
    def construct(self):
        # Create a title
        title = Text("clear_all_except() Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(0.5)
        
        # Create multiple objects
        objects = VGroup(
            Circle(color=RED).shift(LEFT * 3),
            Square(color=BLUE).shift(LEFT * 1),
            Triangle(color=GREEN).shift(RIGHT * 1),
            Dot(color=YELLOW, radius=0.5).shift(RIGHT * 3)
        )
        
        labels = VGroup(*[
            Text(name, font_size=20).next_to(obj, DOWN)
            for obj, name in zip(objects, ["Circle", "Square", "Triangle", "Dot"])
        ])
        
        # Show all objects
        self.play(FadeIn(objects), FadeIn(labels))
        self.wait(1)
        
        # Demonstrate clearing all except specific objects
        instruction = Text(
            "Keeping only Square and Triangle...",
            font_size=30,
            color=YELLOW
        ).to_edge(DOWN)
        self.add(instruction)
        self.wait(1)
        
        # Clear all except title, square, triangle, and their labels
        self.clear_all_except(
            title,
            objects[1],  # Square
            objects[2],  # Triangle
            labels[1],   # Square label
            labels[2]    # Triangle label
        )
        self.wait(2)
        
        # Show final message
        final_msg = Text(
            "Only specified objects remain!",
            font_size=36,
            color=GREEN
        )
        self.play(FadeIn(final_msg))
        self.wait(2)


class DemoClearAllExceptAnimations(Scene):
    """Demonstrate clear_all_except with animations"""
    
    def construct(self):
        # Title
        title = Text("Animated Clear Demo", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create a grid of objects
        grid = VGroup(*[
            Square(side_length=0.8, fill_opacity=0.5).set_color(
                interpolate_color(RED, BLUE, i / 8)
            )
            for i in range(9)
        ]).arrange_in_grid(3, 3, buff=0.5)
        
        self.play(LaggedStartMap(FadeIn, grid, lag_ratio=0.1))
        self.wait(1)
        
        # Highlight the center square
        center_square = grid[4]
        self.play(
            center_square.animate.scale(1.5).set_color(YELLOW),
            run_time=1
        )
        self.wait(0.5)
        
        # Text indicating what will happen
        msg = Text("Keeping only the center square", font_size=30)
        msg.to_edge(DOWN)
        self.play(FadeIn(msg))
        self.wait(1)
        
        # Fade out everything except title and center square
        to_fade = [obj for obj in grid if obj != center_square] + [msg]
        self.play(*[FadeOut(obj) for obj in to_fade])
        
        # Now use clear_all_except to clean up
        self.clear_all_except(title, center_square)
        self.wait(1)
        
        # Add final text
        final_text = Text("Clean scene!", font_size=36, color=GREEN)
        self.play(Write(final_text))
        self.wait(2)


class DemoClearAllExceptGroups(Scene):
    """Demonstrate clear_all_except with VGroups"""
    
    def construct(self):
        title = Text("Working with Groups", font_size=48)
        title.to_edge(UP)
        self.add(title)
        
        # Create two groups
        group1 = VGroup(
            Circle(color=RED).shift(LEFT * 2),
            Square(color=RED).shift(LEFT * 1)
        )
        
        group2 = VGroup(
            Triangle(color=BLUE).shift(RIGHT * 1),
            Star(color=BLUE).shift(RIGHT * 2)
        )
        
        label1 = Text("Group 1", font_size=24, color=RED).next_to(group1, DOWN, buff=0.5)
        label2 = Text("Group 2", font_size=24, color=BLUE).next_to(group2, DOWN, buff=0.5)
        
        # Show everything
        self.play(
            FadeIn(group1),
            FadeIn(group2),
            FadeIn(label1),
            FadeIn(label2)
        )
        self.wait(1)
        
        # Message
        msg = Text("Keeping only Group 2...", font_size=30)
        msg.to_edge(DOWN)
        self.add(msg)
        self.wait(1)
        
        # Clear all except title, group2 and its label
        self.clear_all_except(title, group2, label2)
        self.wait(2)
        
        # Animate the remaining group
        self.play(group2.animate.scale(1.5).move_to(ORIGIN))
        self.wait(2)


class DemoClearAllExceptInteractive(InteractiveScene):
    """Demonstrate clear_all_except in InteractiveScene"""
    
    def construct(self):
        title = Text("Interactive Scene Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        
        # Create multiple layers of objects
        background = Rectangle(
            width=12, height=6,
            stroke_width=3,
            stroke_color=WHITE,
            fill_opacity=0.1
        )
        
        shapes = VGroup(
            Circle(color=RED),
            Square(color=BLUE).shift(RIGHT * 2),
            Triangle(color=GREEN).shift(LEFT * 2)
        )
        
        labels = VGroup(*[
            Text(f"Shape {i+1}", font_size=20).next_to(s, DOWN)
            for i, s in enumerate(shapes)
        ])
        
        self.add(background, shapes, labels)
        self.wait(1)
        
        # Message about interaction
        msg = Text(
            "In interactive mode, selection is preserved",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        self.add(msg)
        self.wait(1)
        
        # Clear all except title, first shape and its label
        self.clear_all_except(title, shapes[0], labels[0])
        self.wait(1)
        
        # Verify selection system still works
        final_msg = Text(
            "Selection system updated!",
            font_size=30,
            color=GREEN
        )
        self.add(final_msg)
        self.wait(2)


class DemoClearAllExceptEmpty(Scene):
    """Demonstrate clearing everything"""
    
    def construct(self):
        # Create many objects
        objects = VGroup(*[
            Circle(radius=0.3, color=random_color()).move_to(
                np.array([
                    np.random.uniform(-5, 5),
                    np.random.uniform(-3, 3),
                    0
                ])
            )
            for _ in range(20)
        ])
        
        title = Text("Clearing Everything", font_size=48).to_edge(UP)
        
        self.add(title, objects)
        self.wait(1)
        
        msg = Text("Calling clear_all_except()...", font_size=30)
        msg.to_edge(DOWN)
        self.add(msg)
        self.wait(1)
        
        # Clear everything (no arguments)
        self.clear_all_except()
        self.wait(1)
        
        # Add new content to show scene is still functional
        new_text = Text("Everything cleared!", font_size=48, color=GREEN)
        self.play(Write(new_text))
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    demos = [
        ("Basic Usage", DemoClearAllExceptBasic),
        ("With Animations", DemoClearAllExceptAnimations),
        ("With Groups", DemoClearAllExceptGroups),
        ("Interactive Scene", DemoClearAllExceptInteractive),
        ("Clear Everything", DemoClearAllExceptEmpty),
    ]
    
    print("\n" + "=" * 70)
    print("CLEAR_ALL_EXCEPT METHOD DEMONSTRATIONS")
    print("=" * 70 + "\n")
    
    for name, scene_class in demos:
        print(f"\n{'=' * 70}")
        print(f"Running: {name}")
        print('=' * 70)
        
        try:
            scene = scene_class()
            scene.run()
            print(f"✓ {name} completed successfully")
        except Exception as e:
            print(f"✗ {name} failed: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    
    print("\n" + "=" * 70)
    print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 70 + "\n")
