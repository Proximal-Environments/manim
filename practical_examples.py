#!/usr/bin/env python
"""Practical examples of clear_all_except usage"""

from manimlib import *

class PresentationScene(Scene):
    """Example: Multi-slide presentation using clear_all_except"""
    
    def construct(self):
        # Slide 1
        title = Text("Presentation Title", font_size=48)
        subtitle = Text("Using clear_all_except", font_size=30)
        subtitle.next_to(title, DOWN)
        
        self.add(title, subtitle)
        print("Slide 1: Title slide")
        
        # Transition - keep title, remove subtitle
        self.clear_all_except(title)
        print("Transition: Kept title, cleared subtitle")
        
        # Slide 2 - Content
        title.scale(0.7).to_edge(UP)
        content = VGroup(
            Text("Point 1: Easy transitions", font_size=24),
            Text("Point 2: Clean code", font_size=24),
            Text("Point 3: Flexible", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.to_edge(LEFT).shift(DOWN * 0.5)
        
        self.add(content)
        print("Slide 2: Content slide")
        
        # Slide 3 - keep title, change content
        self.clear_all_except(title)
        
        new_content = Text("Thank you!", font_size=40)
        self.add(new_content)
        print("Slide 3: Conclusion")


class DiagramBuildingScene(Scene):
    """Example: Building complex diagrams step by step"""
    
    def construct(self):
        # Label that persists through all steps
        step_label = Text("Building Diagram", font_size=36).to_edge(UP)
        self.add(step_label)
        
        # Step 1: Base structure
        base = Square(side_length=2)
        self.add(base)
        print("Step 1: Added base square")
        
        # Step 2: Add details, keep base
        details = VGroup(
            Circle(radius=0.3).shift(UP * 0.5),
            Circle(radius=0.3).shift(DOWN * 0.5),
        )
        self.add(details)
        print("Step 2: Added details")
        
        # Step 3: Focus on base only
        self.clear_all_except(step_label, base)
        print("Step 3: Focused on base (removed details)")
        
        # Step 4: Add different details
        new_details = VGroup(
            Triangle().scale(0.3).shift(LEFT * 0.5),
            Triangle().scale(0.3).shift(RIGHT * 0.5),
        )
        self.add(new_details)
        print("Step 4: Added new details")
        
        # Final: Complete diagram
        step_label.become(Text("Complete!", font_size=36, color=GREEN).to_edge(UP))
        print("Step 5: Diagram complete")


class DataVisualizationScene(Scene):
    """Example: Updating data visualizations"""
    
    def construct(self):
        # Persistent axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            width=8,
            height=6
        )
        x_label = Text("X", font_size=24).next_to(axes, DOWN)
        y_label = Text("Y", font_size=24).next_to(axes, LEFT)
        
        self.add(axes, x_label, y_label)
        print("Setup: Created axes")
        
        # Dataset 1
        points1 = VGroup(*[
            Dot(axes.c2p(x, x + np.random.uniform(-1, 1)), color=RED)
            for x in range(1, 10)
        ])
        label1 = Text("Linear Data", font_size=24, color=RED).to_edge(UP)
        
        self.add(points1, label1)
        print("Visualization 1: Linear data")
        
        # Switch to dataset 2 - keep axes
        self.clear_all_except(axes, x_label, y_label)
        
        # Dataset 2
        points2 = VGroup(*[
            Dot(axes.c2p(x, x**1.5 / 3), color=BLUE)
            for x in range(1, 10)
        ])
        label2 = Text("Exponential Data", font_size=24, color=BLUE).to_edge(UP)
        
        self.add(points2, label2)
        print("Visualization 2: Exponential data")
        
        # Switch to dataset 3 - keep axes
        self.clear_all_except(axes, axes_labels)
        
        # Dataset 3
        points3 = VGroup(*[
            Dot(axes.c2p(x, 5 + 3 * np.sin(x)), color=GREEN)
            for x in np.linspace(0, 10, 20)
        ])
        label3 = Text("Sinusoidal Data", font_size=24, color=GREEN).to_edge(UP)
        
        self.add(points3, label3)
        print("Visualization 3: Sinusoidal data")


class LayerManagementScene(Scene):
    """Example: Managing layers in complex scenes"""
    
    def construct(self):
        # Background layer (always visible)
        background = Rectangle(
            width=14, height=8,
            fill_opacity=0.1,
            stroke_width=2
        )
        bg_label = Text("Background", font_size=20).to_corner(UL)
        
        # UI layer (persistent)
        ui_elements = VGroup(
            Text("Frame: 1", font_size=16).to_corner(DR),
        )
        
        self.add(background, bg_label, ui_elements)
        print("Setup: Added persistent layers")
        
        # Content layer 1
        content1 = VGroup(
            Circle(color=RED),
            Text("Content 1", font_size=24).shift(DOWN * 2)
        )
        self.add(content1)
        print("Frame 1: Added content layer 1")
        
        # Switch content - keep background and UI
        self.clear_all_except(background, bg_label, ui_elements)
        ui_elements[0].become(Text("Frame: 2", font_size=16).to_corner(DR))
        
        # Content layer 2
        content2 = VGroup(
            Square(color=BLUE),
            Text("Content 2", font_size=24).shift(DOWN * 2)
        )
        self.add(content2)
        print("Frame 2: Added content layer 2")
        
        # Switch content again
        self.clear_all_except(background, bg_label, ui_elements)
        ui_elements[0].become(Text("Frame: 3", font_size=16).to_corner(DR))
        
        # Content layer 3
        content3 = VGroup(
            Triangle(color=GREEN),
            Text("Content 3", font_size=24).shift(DOWN * 2)
        )
        self.add(content3)
        print("Frame 3: Added content layer 3")


class InteractiveDemoScene(InteractiveScene):
    """Example: Interactive scene with persistent UI"""
    
    def construct(self):
        # Persistent UI
        instructions = Text(
            "UI Elements Persist",
            font_size=24
        ).to_edge(UP)
        
        self.add(instructions)
        print("Setup: Added persistent instructions")
        
        # Work area 1
        shapes1 = VGroup(
            Circle(color=RED).shift(LEFT),
            Square(color=BLUE).shift(RIGHT)
        )
        self.add(shapes1)
        print("Work area 1: Added shapes")
        
        # Clear work area, keep UI
        self.clear_all_except(instructions)
        print("Cleared work area, kept UI")
        
        # Work area 2
        shapes2 = VGroup(
            Triangle(color=GREEN).shift(LEFT),
            Dot(color=YELLOW, radius=0.3).shift(RIGHT)
        )
        self.add(shapes2)
        print("Work area 2: Added new shapes")
        
        # Verify selection system works
        print(f"Selection search set size: {len(self.selection_search_set)}")


if __name__ == "__main__":
    examples = [
        ("Presentation", PresentationScene),
        ("Diagram Building", DiagramBuildingScene),
        ("Data Visualization", DataVisualizationScene),
        ("Layer Management", LayerManagementScene),
        ("Interactive Demo", InteractiveDemoScene),
    ]
    
    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLES OF CLEAR_ALL_EXCEPT")
    print("=" * 70 + "\n")
    
    for name, scene_class in examples:
        print(f"\n{'=' * 70}")
        print(f"Example: {name}")
        print('=' * 70 + "\n")
        
        try:
            scene = scene_class()
            scene.run()
            print(f"\n✓ {name} example completed\n")
        except Exception as e:
            print(f"\n✗ {name} example failed: {e}\n")
            import traceback
            traceback.print_exc()
    
    print("=" * 70)
    print("ALL PRACTICAL EXAMPLES COMPLETED!")
    print("=" * 70 + "\n")
