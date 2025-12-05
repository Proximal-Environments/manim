#!/usr/bin/env python
"""
Test script for the clear_all_except method in Scene and InteractiveScene
"""
from manimlib import *

class TestClearAllExceptScene(Scene):
    def construct(self):
        # Create some test objects
        circle = Circle(color=BLUE)
        square = Square(color=RED).shift(LEFT * 2)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Text("Test", color=YELLOW).shift(UP * 2)
        
        # Add all objects to the scene
        self.add(circle, square, triangle, text)
        
        # Verify all objects are in the scene
        print(f"Number of mobjects after adding all: {len(self.mobjects)}")
        assert circle in self.mobjects, "Circle should be in scene"
        assert square in self.mobjects, "Square should be in scene"
        assert triangle in self.mobjects, "Triangle should be in scene"
        assert text in self.mobjects, "Text should be in scene"
        
        self.wait(0.5)
        
        # Clear all except circle and text
        self.clear_all_except(circle, text)
        
        # Verify only circle and text remain
        print(f"Number of mobjects after clear_all_except: {len(self.mobjects)}")
        assert circle in self.mobjects, "Circle should still be in scene"
        assert text in self.mobjects, "Text should still be in scene"
        assert square not in self.mobjects, "Square should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        self.wait(0.5)
        
        # Test clearing everything (no arguments)
        self.clear_all_except()
        print(f"Number of mobjects after clear_all_except(): {len(self.mobjects)}")
        assert circle not in self.mobjects, "Circle should be removed"
        assert text not in self.mobjects, "Text should be removed"
        
        self.wait(0.5)
        
        # Add new objects
        dot1 = Dot(color=PINK).shift(UP)
        dot2 = Dot(color=ORANGE).shift(DOWN)
        self.add(dot1, dot2)
        
        # Keep only dot1
        self.clear_all_except(dot1)
        assert dot1 in self.mobjects, "Dot1 should be in scene"
        assert dot2 not in self.mobjects, "Dot2 should be removed"
        
        self.wait(0.5)
        
        print("All tests passed!")


class TestClearAllExceptInteractiveScene(InteractiveScene):
    def construct(self):
        # Create some test objects
        circle = Circle(color=BLUE)
        square = Square(color=RED).shift(LEFT * 2)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Add all objects to the scene
        self.add(circle, square, triangle)
        
        # Verify all objects are in the scene
        print(f"[Interactive] Number of mobjects after adding all: {len(self.mobjects)}")
        
        # The interactive scene has additional UI elements, so we check differently
        selectable_mobs = [m for m in self.mobjects if m not in self.unselectables]
        assert circle in selectable_mobs, "Circle should be in scene"
        assert square in selectable_mobs, "Square should be in scene"
        assert triangle in selectable_mobs, "Triangle should be in scene"
        
        self.wait(0.5)
        
        # Clear all except circle
        self.clear_all_except(circle)
        
        # Verify only circle remains (among selectable objects)
        selectable_mobs = [m for m in self.mobjects if m not in self.unselectables]
        print(f"[Interactive] Number of selectable mobjects after clear_all_except: {len(selectable_mobs)}")
        assert circle in selectable_mobs, "Circle should still be in scene"
        assert square not in self.mobjects, "Square should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        # Verify selection search set was regenerated
        assert hasattr(self, 'selection_search_set'), "Selection search set should exist"
        
        self.wait(0.5)
        
        print("[Interactive] All tests passed!")


if __name__ == "__main__":
    import sys
    
    # Test basic Scene
    print("=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    scene1 = TestClearAllExceptScene()
    scene1.run()
    
    # Test InteractiveScene
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except()")
    print("=" * 60)
    scene2 = TestClearAllExceptInteractiveScene()
    scene2.run()
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
