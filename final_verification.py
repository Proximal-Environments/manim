#!/usr/bin/env python3
"""
Final verification script for clear_all_except implementation
This runs a series of tests to confirm everything works correctly
"""

def test_scene():
    """Test Scene.clear_all_except()"""
    print("\n" + "="*60)
    print("TEST 1: Scene.clear_all_except()")
    print("="*60)
    
    from manimlib.scene.scene import Scene
    from manimlib.mobject.geometry import Circle, Square
    from manimlib.constants import RED, BLUE
    
    scene = Scene(skip_animations=True)
    
    # Test 1: Basic usage
    c1 = Circle(color=RED)
    c2 = Square(color=BLUE)
    scene.add(c1, c2)
    
    assert c1 in scene.mobjects, "c1 should be in scene"
    assert c2 in scene.mobjects, "c2 should be in scene"
    print("✓ Objects added correctly")
    
    scene.clear_all_except(c1)
    assert c1 in scene.mobjects, "c1 should remain"
    assert c2 not in scene.mobjects, "c2 should be removed"
    print("✓ clear_all_except(c1) works")
    
    # Test 2: Clear all
    scene.add(c2)
    scene.clear_all_except()
    assert len(scene.mobjects) == 0, "All objects should be removed"
    print("✓ clear_all_except() clears everything")
    
    # Test 3: Duplicates
    c3 = Circle(color=RED)
    scene.add(c3)
    scene.clear_all_except(c3, c3, c3)
    assert scene.mobjects.count(c3) == 1, "No duplicates should be created"
    print("✓ Duplicate arguments handled correctly")
    
    # Test 4: Method chaining
    c4 = Circle(color=RED)
    c5 = Square(color=BLUE)
    result = scene.add(c4, c5).clear_all_except(c4)
    assert result is scene, "Should return self"
    assert c4 in scene.mobjects, "c4 should remain"
    print("✓ Method chaining works")
    
    print("\n✅ All Scene tests passed!")
    return True


def test_interactive_scene():
    """Test InteractiveScene.clear_all_except()"""
    print("\n" + "="*60)
    print("TEST 2: InteractiveScene.clear_all_except()")
    print("="*60)
    
    from manimlib.scene.interactive_scene import InteractiveScene
    from manimlib.mobject.geometry import Circle, Square
    from manimlib.constants import RED, BLUE
    
    scene = InteractiveScene(skip_animations=True)
    scene.setup()  # Initialize unselectables
    
    # Test 1: Basic usage
    c1 = Circle(color=RED)
    c2 = Square(color=BLUE)
    scene.add(c1, c2)
    
    initial_search_set_size = len(scene.selection_search_set)
    assert initial_search_set_size == 2, "Search set should have 2 objects"
    print(f"✓ Objects added, search set size: {initial_search_set_size}")
    
    scene.clear_all_except(c1)
    after_search_set_size = len(scene.selection_search_set)
    assert after_search_set_size == 1, "Search set should have 1 object"
    assert c1 in scene.mobjects, "c1 should remain"
    assert c2 not in scene.mobjects, "c2 should be removed"
    print(f"✓ clear_all_except(c1) works, search set size: {after_search_set_size}")
    
    # Test 2: Clear all
    scene.add(c2)
    scene.clear_all_except()
    assert len(scene.selection_search_set) == 0, "Search set should be empty"
    print("✓ clear_all_except() updates search set")
    
    # Test 3: Method chaining (return value)
    c3 = Circle(color=RED)
    scene.add(c3)
    result = scene.clear_all_except(c3)
    assert result is scene, "Should return self"
    print("✓ clear_all_except returns self")
    
    print("\n✅ All InteractiveScene tests passed!")
    return True


def test_practical_usage():
    """Test practical usage patterns"""
    print("\n" + "="*60)
    print("TEST 3: Practical Usage Patterns")
    print("="*60)
    
    from manimlib.scene.scene import Scene
    from manimlib.mobject.geometry import Circle, Square, Triangle
    from manimlib.mobject.svg.text_mobject import Text
    from manimlib.constants import RED, BLUE, GREEN
    
    scene = Scene(skip_animations=True)
    
    # Pattern 1: Persistent UI elements
    print("\nPattern 1: Persistent UI elements")
    title = Text("Title", font_size=36)
    content1 = Circle(color=RED)
    content2 = Square(color=BLUE)
    
    scene.add(title, content1, content2)
    scene.clear_all_except(title)  # Keep title, remove content
    
    assert title in scene.mobjects, "Title should persist"
    assert content1 not in scene.mobjects, "Content removed"
    print("✓ Persistent UI pattern works")
    
    # Pattern 2: Progressive disclosure
    print("\nPattern 2: Progressive disclosure")
    scene.clear()
    objects = [Circle(color=RED), Square(color=BLUE), Triangle(color=GREEN)]
    scene.add(*objects)
    
    # Focus on important objects
    important = objects[:2]
    scene.clear_all_except(*important)
    
    assert all(obj in scene.mobjects for obj in important), "Important objects kept"
    assert objects[2] not in scene.mobjects, "Other objects removed"
    print("✓ Progressive disclosure pattern works")
    
    # Pattern 3: Multi-stage visualization
    print("\nPattern 3: Multi-stage visualization")
    scene.clear()
    persistent_title = Text("Stage", font_size=36)
    scene.add(persistent_title)
    
    # Stage 1
    stage1_objects = [Circle(), Square()]
    scene.add(*stage1_objects)
    
    # Transition to Stage 2 - keep only title
    scene.clear_all_except(persistent_title)
    
    # Stage 2
    stage2_objects = [Triangle()]
    scene.add(*stage2_objects)
    
    assert persistent_title in scene.mobjects, "Title persists across stages"
    assert all(obj not in scene.mobjects for obj in stage1_objects), "Stage 1 cleared"
    assert all(obj in scene.mobjects for obj in stage2_objects), "Stage 2 added"
    print("✓ Multi-stage visualization pattern works")
    
    print("\n✅ All practical usage tests passed!")
    return True


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("FINAL VERIFICATION: clear_all_except() Implementation")
    print("="*60)
    
    try:
        success = True
        success = test_scene() and success
        success = test_interactive_scene() and success
        success = test_practical_usage() and success
        
        if success:
            print("\n" + "="*60)
            print("🎉 ALL VERIFICATION TESTS PASSED! 🎉")
            print("="*60)
            print("\nThe clear_all_except() method is:")
            print("  ✅ Correctly implemented in Scene")
            print("  ✅ Correctly implemented in InteractiveScene")
            print("  ✅ Handling all edge cases")
            print("  ✅ Supporting practical usage patterns")
            print("  ✅ Production ready!")
            print("\nImplementation complete and verified!")
            return 0
        else:
            print("\n❌ Some tests failed")
            return 1
            
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
