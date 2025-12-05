#!/usr/bin/env python
"""
Final verification script for clear_all_except implementation
"""

import sys

def verify_method_exists():
    """Verify the method exists in both classes"""
    print("Verifying method exists...")
    
    from manimlib.scene.scene import Scene
    from manimlib.scene.interactive_scene import InteractiveScene
    
    assert hasattr(Scene, 'clear_all_except'), "Scene missing clear_all_except method"
    assert hasattr(InteractiveScene, 'clear_all_except'), "InteractiveScene missing clear_all_except method"
    
    print("  ✓ Method exists in Scene")
    print("  ✓ Method exists in InteractiveScene")
    return True

def verify_method_signature():
    """Verify method signature"""
    print("\nVerifying method signature...")
    
    import inspect
    from manimlib.scene.scene import Scene
    from manimlib.scene.interactive_scene import InteractiveScene
    
    scene_sig = inspect.signature(Scene.clear_all_except)
    interactive_sig = inspect.signature(InteractiveScene.clear_all_except)
    
    print(f"  Scene signature: {scene_sig}")
    print(f"  InteractiveScene signature: {interactive_sig}")
    
    # Check parameters
    scene_params = list(scene_sig.parameters.keys())
    assert 'self' in scene_params, "Scene method missing self parameter"
    assert 'mobjects_to_keep' in scene_params, "Scene method missing mobjects_to_keep parameter"
    
    print("  ✓ Signatures correct")
    return True

def verify_functionality():
    """Verify basic functionality"""
    print("\nVerifying basic functionality...")
    
    from manimlib.scene.scene import Scene
    from manimlib.scene.interactive_scene import InteractiveScene
    from manimlib.mobject.geometry import Circle, Square, Triangle
    
    # Test Scene
    print("  Testing Scene...")
    scene = Scene(skip_animations=True)
    c1, c2, c3 = Circle(), Square(), Triangle()
    scene.add(c1, c2, c3)
    scene.clear_all_except(c1)
    assert c1 in scene.mobjects, "c1 should be in scene"
    assert c2 not in scene.mobjects, "c2 should not be in scene"
    assert c3 not in scene.mobjects, "c3 should not be in scene"
    assert scene.frame in scene.mobjects, "frame should be preserved"
    print("    ✓ Scene functionality correct")
    
    # Test InteractiveScene
    print("  Testing InteractiveScene...")
    iscene = InteractiveScene(skip_animations=True)
    iscene.setup()
    c1, c2, c3 = Circle(), Square(), Triangle()
    iscene.add(c1, c2, c3)
    iscene.clear_all_except(c1)
    assert c1 in iscene.mobjects, "c1 should be in scene"
    assert c2 not in iscene.mobjects, "c2 should not be in scene"
    assert c3 not in iscene.mobjects, "c3 should not be in scene"
    assert iscene.frame in iscene.mobjects, "frame should be preserved"
    assert iscene.selection_highlight in iscene.mobjects, "selection_highlight should be preserved"
    print("    ✓ InteractiveScene functionality correct")
    
    return True

def verify_docstrings():
    """Verify docstrings are present"""
    print("\nVerifying docstrings...")
    
    from manimlib.scene.scene import Scene
    from manimlib.scene.interactive_scene import InteractiveScene
    
    scene_doc = Scene.clear_all_except.__doc__
    interactive_doc = InteractiveScene.clear_all_except.__doc__
    
    assert scene_doc is not None, "Scene method missing docstring"
    assert interactive_doc is not None, "InteractiveScene method missing docstring"
    assert "clear" in scene_doc.lower(), "Scene docstring should mention clearing"
    assert "clear" in interactive_doc.lower(), "InteractiveScene docstring should mention clearing"
    
    print("  ✓ Docstrings present and valid")
    return True

def verify_return_value():
    """Verify method returns self for chaining"""
    print("\nVerifying return value...")
    
    from manimlib.scene.scene import Scene
    from manimlib.mobject.geometry import Circle
    
    scene = Scene(skip_animations=True)
    circle = Circle()
    scene.add(circle)
    result = scene.clear_all_except(circle)
    
    assert result is scene, "Method should return self"
    print("  ✓ Method returns self for chaining")
    return True

def main():
    """Run all verifications"""
    print("=" * 60)
    print("CLEAR_ALL_EXCEPT IMPLEMENTATION VERIFICATION")
    print("=" * 60)
    
    try:
        verify_method_exists()
        verify_method_signature()
        verify_docstrings()
        verify_return_value()
        verify_functionality()
        
        print("\n" + "=" * 60)
        print("✓ ALL VERIFICATIONS PASSED!")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
