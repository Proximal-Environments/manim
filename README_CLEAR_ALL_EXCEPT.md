# clear_all_except() Method - Complete Implementation Guide

## Quick Start

The `clear_all_except()` method allows you to clear all objects from a scene while keeping specific objects. It's available in both `Scene` and `InteractiveScene` classes.

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square

class QuickExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle, square)
        
        # Keep only the circle, remove the square
        self.clear_all_except(circle)
```

## Implementation Details

### Files Modified

1. **manimlib/scene/scene.py**
   - Added `clear_all_except()` method (lines 398-416)
   
2. **manimlib/scene/interactive_scene.py**
   - Added `clear_all_except()` method (lines 248-270)

### Method Implementation

#### Scene.clear_all_except()

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list. The camera frame is automatically
    preserved unless explicitly removed.
    
    Args:
        *mobjects_to_keep: Mobjects to keep on screen after clearing
    """
    # Preserve the camera frame unless it's explicitly being removed
    frame = self.camera.frame
    keep_frame = frame not in mobjects_to_keep and frame in self.mobjects
    
    self.clear()
    if keep_frame:
        self.mobjects.append(frame)
    self.add(*mobjects_to_keep)
    return self
```

#### InteractiveScene.clear_all_except()

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list. Internal InteractiveScene objects
    (like selection_highlight, selection_rectangle, crosshair, etc.)
    are automatically preserved.
    
    Args:
        *mobjects_to_keep: Mobjects to keep on screen after clearing
    """
    # Save internal objects that should be preserved
    internal_objects = [m for m in self.mobjects if m in self.unselectables]
    
    # Call parent's clear_all_except (which handles frame preservation)
    super().clear_all_except(*mobjects_to_keep)
    
    # Re-add internal objects that were present before
    for obj in internal_objects:
        if obj not in self.mobjects:
            self.mobjects.append(obj)
    
    self.regenerate_selection_search_set()
    return self
```

## Key Features

### Automatic Preservation

The method automatically preserves:

**In Scene:**
- Camera frame

**In InteractiveScene (in addition to Scene features):**
- selection_highlight
- selection_rectangle
- crosshair
- information_label
- All other objects in `unselectables`

### Method Chaining

Returns `self` for fluent API:

```python
self.add(obj1, obj2).clear_all_except(obj1).add(obj3)
```

## Usage Examples

### Example 1: Basic Scene Clearing

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import RED, BLUE, GREEN

class BasicExample(Scene):
    def construct(self):
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only the circle
        self.clear_all_except(circle)
        self.wait(1)
```

### Example 2: Progressive Scene Transitions

```python
from manimlib import Scene
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.mobject.geometry import Circle

class TransitionExample(Scene):
    def construct(self):
        title = Tex("My Animation").to_edge(UP)
        self.add(title)
        
        # Scene 1
        obj1 = Circle()
        self.add(obj1)
        self.wait(1)
        
        # Transition to Scene 2 - keep title
        obj2 = Square()
        self.clear_all_except(title)
        self.add(obj2)
        self.wait(1)
        
        # Transition to Scene 3 - keep title
        obj3 = Triangle()
        self.clear_all_except(title)
        self.add(obj3)
        self.wait(1)
```

### Example 3: Multiple Objects

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square
from manimlib.mobject.svg.tex_mobject import Tex

class MultipleObjectsExample(Scene):
    def construct(self):
        title = Tex("Title")
        subtitle = Tex("Subtitle").next_to(title, DOWN)
        c1 = Circle()
        c2 = Square()
        
        self.add(title, subtitle, c1, c2)
        self.wait(1)
        
        # Keep title and subtitle, remove shapes
        self.clear_all_except(title, subtitle)
        self.wait(1)
```

## Testing

### Run Unit Tests

```bash
xvfb-run -a python test_clear_all_except.py
```

### Test Output

```
============================================================
Testing Scene.clear_all_except()
============================================================
Number of mobjects before clear_all_except: 4
Number of mobjects after clear_all_except: 3
Number of mobjects after adding new_square: 4
Number of mobjects after second clear_all_except: 2
Number of mobjects after manual frame removal: 2
Number of mobjects after clear_all_except with no frame: 1
✓ All Scene tests passed!

============================================================
Testing InteractiveScene.clear_all_except()
============================================================
Number of user objects before clear_all_except: 3
Number of user objects after clear_all_except: 2
Number of user objects after adding new_circle: 3
Number of user objects after second clear_all_except: 1
✓ All InteractiveScene tests passed!

============================================================
✓ ALL TESTS PASSED!
============================================================
```

### Run Visual Demo

```bash
manimgl demo_clear_all_except.py DemoClearAllExcept --write
```

or for interactive demo:

```bash
manimgl demo_clear_all_except.py DemoClearAllExceptInteractive --write
```

## Files Included

| File | Description |
|------|-------------|
| `test_clear_all_except.py` | Comprehensive unit tests |
| `demo_clear_all_except.py` | Visual demonstration with animations |
| `example_clear_all_except.py` | Simple usage example |
| `CLEAR_ALL_EXCEPT_DOCS.md` | Detailed documentation |
| `CLEAR_ALL_EXCEPT_SUMMARY.md` | Implementation summary |
| `README_CLEAR_ALL_EXCEPT.md` | This file - complete guide |

## Comparison with Other Methods

| Method | Removes All | Keeps Specified | Auto-Preserves Frame | Auto-Preserves Interactive |
|--------|-------------|-----------------|---------------------|---------------------------|
| `clear()` | ✓ | ✗ | ✗ | ✗ |
| `remove(*mobs)` | ✗ | implicit | ✓ | ✓ |
| `clear_all_except(*mobs)` | ✓ | ✓ | ✓ | ✓ (InteractiveScene) |

## Benefits

1. **Cleaner Code**: Single method call instead of tracking all objects to remove
2. **Safer**: Automatically preserves essential objects
3. **More Readable**: Intent is clear from method name
4. **Flexible**: Works with any number of objects
5. **Efficient**: Properly manages render groups via decorator

## Edge Cases Handled

1. **Empty Keep List**: `clear_all_except()` - Removes all user objects, keeps frame
2. **Single Object**: `clear_all_except(obj)` - Keeps only that object (and frame)
3. **All Objects**: Keeps all specified objects even if it's the entire scene
4. **Frame Already Removed**: If frame was manually removed, it stays removed
5. **Interactive Objects**: Always preserved in InteractiveScene

## Technical Notes

### Decorator

The `@affects_mobject_list` decorator ensures:
- Render groups are reassembled after clearing
- Scene state is properly updated
- Method can be chained

### Performance

- O(n) where n is the number of mobjects
- Same performance characteristics as `clear()` + `add()`
- Render group reassembly is handled efficiently by decorator

### Thread Safety

Not thread-safe (consistent with other Scene methods). Use in single-threaded animation construction.

## Troubleshooting

### Issue: Frame is missing after clear
**Solution**: The frame should be automatically preserved. If it's missing, check if it was manually removed before calling `clear_all_except()`.

### Issue: Interactive objects (selection_highlight) missing
**Solution**: Ensure you're using `InteractiveScene`, not `Scene`. The base `Scene` class doesn't have these objects.

### Issue: Objects not being kept
**Solution**: Make sure you're passing the actual mobject references, not new instances:

```python
# Wrong
circle = Circle()
self.add(circle)
self.clear_all_except(Circle())  # This creates a NEW circle!

# Right
circle = Circle()
self.add(circle)
self.clear_all_except(circle)  # Use the same reference
```

## Contributing

If you find issues or have suggestions:
1. Check the test suite passes
2. Add tests for new behavior
3. Update documentation
4. Submit a pull request

## License

Same as ManimGL project.
