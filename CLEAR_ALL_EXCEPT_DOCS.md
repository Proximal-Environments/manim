# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all objects from the scene while preserving specific objects that you want to keep.

## Location

- `manimlib/scene/scene.py` - Base implementation in `Scene` class
- `manimlib/scene/interactive_scene.py` - Extended implementation in `InteractiveScene` class

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Self
```

### Parameters

- `*mobjects_to_keep`: Variable number of `Mobject` instances to keep on the scene after clearing

### Returns

- Returns `self` to allow method chaining

## Behavior

### In Scene

1. Clears all mobjects from the scene
2. Automatically preserves the camera frame (unless it was already manually removed)
3. Adds back only the specified mobjects

### In InteractiveScene

1. Clears all mobjects from the scene
2. Automatically preserves:
   - The camera frame
   - Internal InteractiveScene objects (selection_highlight, selection_rectangle, crosshair, information_label, etc.)
3. Adds back only the specified mobjects

## Usage Examples

### Basic Usage in Scene

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT

class MyScene(Scene):
    def construct(self):
        # Create several shapes
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Add all shapes
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only the circle and square, remove the triangle
        self.clear_all_except(circle, square)
        self.wait(1)
```

### Keeping Text and One Shape

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.constants import RED, UP

class TextAndShapeScene(Scene):
    def construct(self):
        title = Tex("My Animation").to_edge(UP)
        circle = Circle(color=RED)
        
        self.add(title, circle)
        self.wait(1)
        
        # Later, add more objects
        square = Square()
        self.add(square)
        self.wait(1)
        
        # Clear everything except the title and circle
        self.clear_all_except(title, circle)
        self.wait(1)
```

### Progressive Scene Clearing

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT

class ProgressiveScene(Scene):
    def construct(self):
        # Add multiple objects
        c1 = Circle(color=RED).shift(LEFT * 2)
        c2 = Circle(color=BLUE)
        c3 = Circle(color=GREEN).shift(RIGHT * 2)
        
        self.add(c1, c2, c3)
        self.wait(1)
        
        # Keep only the middle circle
        self.clear_all_except(c2)
        self.wait(1)
        
        # Add new circles
        c4 = Circle(color=YELLOW).shift(UP)
        c5 = Circle(color=ORANGE).shift(DOWN)
        self.add(c4, c5)
        self.wait(1)
        
        # Clear and keep only the new circles
        self.clear_all_except(c4, c5)
        self.wait(1)
```

### Method Chaining

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square

class ChainingScene(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        # Method chaining is supported
        self.add(circle, square).clear_all_except(circle).add(Square().shift(UP))
        self.wait(1)
```

## Important Notes

### Frame Preservation

The camera frame is automatically preserved by default. This means:

```python
# The frame will still be present after this call
self.clear_all_except(my_circle)

# Even if you clear everything
self.clear_all_except()  # Frame is preserved
```

If you need to remove the frame (unusual case), you must explicitly remove it before calling `clear_all_except()`.

### InteractiveScene Special Objects

In `InteractiveScene`, internal objects are automatically preserved:
- `selection_highlight`
- `selection_rectangle`
- `crosshair`
- `information_label`
- `camera.frame`

These don't need to be explicitly included in the `mobjects_to_keep` list.

### Comparison with Other Methods

| Method | Description | Preserves Frame? | Preserves Interactive Objects? |
|--------|-------------|------------------|-------------------------------|
| `clear()` | Removes all mobjects | No | No |
| `remove(*mobs)` | Removes specific mobjects | Yes (if not specified) | Yes (if not specified) |
| `clear_all_except(*mobs)` | Removes all except specified | Yes (automatic) | Yes (automatic in InteractiveScene) |

## Implementation Details

### Scene Implementation

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

### InteractiveScene Implementation

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

## Testing

Run the test suite to verify the implementation:

```bash
xvfb-run -a python test_clear_all_except.py
```

Run the visual demo:

```bash
manimgl demo_clear_all_except.py DemoClearAllExcept --write
```

## Use Cases

1. **Scene Transitions**: Quickly clear the scene while keeping persistent elements like titles or watermarks
2. **Progressive Animations**: Show different sets of objects without manually tracking what to remove
3. **Interactive Development**: Quickly reset the scene to a specific state during development
4. **Conditional Display**: Show different objects based on logic without complex remove calls

## Migration from Manual Clearing

### Before

```python
# Manual approach
self.remove(obj1, obj2, obj3, obj4)
# Hope you didn't forget any objects!
```

### After

```python
# Cleaner approach
self.clear_all_except(title, important_object)
# Everything else is automatically removed
```

## Performance

The method has similar performance characteristics to calling `clear()` followed by `add()`. The `@affects_mobject_list` decorator ensures that render groups are properly reassembled.
