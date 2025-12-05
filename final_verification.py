#!/usr/bin/env python3
"""
Final comprehensive verification of clear_all_except implementation
"""

import sys
sys.path.insert(0, '/root/proximal/workspace')

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text

def test_scene():
    """Test Scene.clear_all_except"""
    print("Testing Scene.clear_all_except...")
    
    scene = Scene(skip_animations=True)
    
    # Test 1: Basic functionality
    c1, c2, c3 = Circle(), Square(), Triangle()
    scene.add(c1, c2, c3)
    assert len(scene.mobjects) == 4  # 3 objects + camera frame
    
    scene.clear_all_except(c1)
    assert len(scene.mobjects) == 2  # 1 object + camera frame
    assert c1 in scene.mobjects
    assert c2 not in scene.mobjects
    assert scene.camera.frame in scene.mobjects
    print("  ✓ Basic functionality")
    
    # Test 2: Multiple objects
    scene.add(c2, c3)
    scene.clear_all_except(c1, c2)
    assert len(scene.mobjects) == 3  # 2 objects + camera frame
    assert c1 in scene.mobjects
    assert c2 in scene.mobjects
    assert c3 not in scene.mobjects
    print("  ✓ Multiple objects preservation")
    
    # Test 3: Clear all
    scene.clear_all_except()
    assert len(scene.mobjects) == 1  # only camera frame
    assert scene.camera.frame in scene.mobjects
    print("  ✓ Clear all (empty keep list)")
    
    # Test 4: Method chaining
    result = scene.clear_all_except(c1)
    assert result is scene
    print("  ✓ Method chaining")
    
    print("✅ Scene tests passed!\n")

def test_interactive_scene():
    """Test InteractiveScene.clear_all_except"""
    print("Testing InteractiveScene.clear_all_except...")
    
    scene = InteractiveScene(skip_animations=True)
    scene.setup()
    
    # Test 1: Basic functionality with selection_search_set
    c1, c2, c3 = Circle(), Square(), Triangle()
    scene.add(c1, c2, c3)
    
    initial_search_set_size = len(scene.selection_search_set)
    assert initial_search_set_size == 3, f"Expected 3, got {initial_search_set_size}"
    
    scene.clear_all_except(c1)
    after_search_set_size = len(scene.selection_search_set)
    assert after_search_set_size == 1, f"Expected 1, got {after_search_set_size}"
    assert c1 in scene.mobjects
    assert c2 not in scene.mobjects
    assert scene.camera.frame in scene.mobjects
    print("  ✓ Basic functionality with selection_search_set update")
    
    # Test 2: Unselectables not affected
    scene.add(c2, c3)
    initial_unselectables = len(scene.unselectables)
    scene.clear_all_except(c1)
    assert len(scene.unselectables) == initial_unselectables
    print("  ✓ Unselectables preserved")
    
    # Test 3: Clear all updates search set
    scene.clear_all_except()
    assert len(scene.selection_search_set) == 0
    print("  ✓ Clear all updates selection_search_set")
    
    # Test 4: Method chaining
    result = scene.clear_all_except(c1)
    assert result is scene
    print("  ✓ Method chaining")
    
    print("✅ InteractiveScene tests passed!\n")

def test_edge_cases():
    """Test edge cases"""
    print("Testing edge cases...")
    
    scene = Scene(skip_animations=True)
    
    # Test 1: Object not in scene
    c1 = Circle()
    c2 = Square()
    scene.add(c1)
    scene.clear_all_except(c1, c2)  # c2 not in scene
    assert c1 in scene.mobjects
    print("  ✓ Handle objects not in scene")
    
    # Test 2: Duplicate objects
    scene.add(c2)
    scene.clear_all_except(c1, c1)  # duplicate
    assert c1 in scene.mobjects
    assert c2 not in scene.mobjects
    print("  ✓ Handle duplicate objects in keep list")
    
    # Test 3: Camera frame explicitly included
    scene.add(c2)
    scene.clear_all_except(c1, scene.camera.frame)
    assert scene.camera.frame in scene.mobjects
    assert c1 in scene.mobjects
    print("  ✓ Camera frame explicitly included (redundant but safe)")
    
    print("✅ Edge case tests passed!\n")

def test_practical_scenarios():
    """Test practical usage scenarios"""
    print("Testing practical scenarios...")
    
    # Scenario 1: Slideshow
    scene = Scene(skip_animations=True)
    title = Text("Title")
    scene.add(title)
    
    for i in range(3):
        content = Text(f"Slide {i+1}")
        scene.add(content)
        scene.clear_all_except(title)  # Keep title between slides
    
    assert title in scene.mobjects
    print("  ✓ Slideshow with persistent title")
    
    # Scenario 2: Coordinate system
    scene.clear_all_except()
    axes = Circle()  # pretend it's axes
    scene.add(axes)
    
    for i in range(3):
        point = Square()
        scene.add(point)
        scene.clear_all_except(axes)  # Keep axes
    
    assert axes in scene.mobjects
    print("  ✓ Coordinate system with changing points")
    
    print("✅ Practical scenario tests passed!\n")

if __name__ == "__main__":
    try:
        print("="*60)
        print("FINAL COMPREHENSIVE VERIFICATION")
        print("="*60 + "\n")
        
        test_scene()
        test_interactive_scene()
        test_edge_cases()
        test_practical_scenarios()
        
        print("="*60)
        print("🎉 ALL VERIFICATION TESTS PASSED! 🎉")
        print("="*60)
        print("\nThe clear_all_except() method is working correctly in:")
        print("  ✓ manimlib/scene/scene.py")
        print("  ✓ manimlib/scene/interactive_scene.py")
        print("\nFeatures verified:")
        print("  ✓ Basic clearing with selective preservation")
        print("  ✓ Camera frame automatic preservation")
        print("  ✓ Multiple object preservation")
        print("  ✓ Empty keep list (clear all)")
        print("  ✓ Method chaining")
        print("  ✓ InteractiveScene selection_search_set updates")
        print("  ✓ Edge case handling")
        print("  ✓ Practical usage scenarios")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
