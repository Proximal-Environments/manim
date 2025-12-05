# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all objects from the scene while keeping only specific objects that you want to preserve.

## Location

- `manimlib/scene/scene.py` - Base implementation in the `Scene` class
- `manimlib/scene/interactive_scene.py` - Override in `InteractiveScene` class

## Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list. The camera frame is automatically
    preserved.
    
    Parameters
    ----------
    mobjects_to_keep : Mobject
        The mobjects that should remain in the scene after clearing
        
    Returns
    -------
    Scene
        Returns self for method chaining
    """
```

## Features

1. **Automatic Camera Frame Preservation**: The camera frame is always preserved automatically, so you don't need to include it in the list of objects to keep.

2. **Method Chaining**: Returns `self` to allow method chaining with other scene methods.

3. **InteractiveScene Integration**: In `InteractiveScene`, the method automatically updates the `selection_search_set` to reflect the new scene state.

4. **Uses @affects_mobject_list Decorator**: Properly reassembles render groups after clearing.

## Usage Examples

### Basic Scene Usage

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Clear everything except the circle
        self.clear_all_except(circle)
        self.wait(1)
        
        # Clear everything (empty scene)
        self.clear_all_except()
        self.wait(1)
```

### InteractiveScene Usage

```python
from manimlib import InteractiveScene
from manimlib.mobject.geometry import Circle, Square
from manimlib.mobject.svg.text_mobject import Text

class MyInteractiveScene(InteractiveScene):
    def construct(self):
        # Create objects
        title = Text("My Scene").to_edge(UP)
        circle = Circle()
        square = Square()
        
        # Add objects
        self.add(title, circle, square)
        self.wait(1)
        
        # Clear all except title
        # The selection_search_set is automatically updated
        self.clear_all_except(title)
        self.wait(1)
```

### Method Chaining

```python
# You can chain methods
scene.clear_all_except(circle).add(square).wait(1)
```

### Keeping Multiple Objects

```python
# Keep multiple objects by passing them as separate arguments
self.clear_all_except(obj1, obj2, obj3)

# Or unpack a list
objects_to_keep = [obj1, obj2, obj3]
self.clear_all_except(*objects_to_keep)
```

## Implementation Details

### Scene Implementation

The base implementation in `Scene`:
1. Stores a reference to the camera frame
2. Clears the mobjects list completely
3. Re-adds the camera frame as the first mobject
4. Adds back the specified mobjects to keep

### InteractiveScene Implementation

The `InteractiveScene` override:
1. Calls the parent `clear_all_except()` method
2. Regenerates the `selection_search_set` to update the list of selectable objects
3. Maintains proper integration with the interactive selection system

## Notes

- The camera frame (`self.camera.frame`) is always preserved and doesn't need to be explicitly included in `mobjects_to_keep`
- Objects passed to `mobjects_to_keep` maintain their z-index ordering
- The method properly triggers the `@affects_mobject_list` decorator, ensuring render groups are reassembled
- In `InteractiveScene`, unselectable objects (like `selection_highlight`, `selection_rectangle`, etc.) are handled separately and not affected by this method

## Testing

Comprehensive tests have been added in `test_clear_all_except_simple.py` which verify:
- Basic functionality in `Scene`
- Proper camera frame preservation
- Multiple object preservation
- Empty scene clearing
- Method chaining
- InteractiveScene-specific behavior
- Selection search set regeneration

To run tests:
```bash
xvfb-run -a python test_clear_all_except_simple.py
```

## Comparison with clear()

| Feature | `clear()` | `clear_all_except()` |
|---------|-----------|----------------------|
| Removes all mobjects | ✓ | ✓ |
| Removes camera frame | ✓ | ✗ |
| Can keep specific objects | ✗ | ✓ |
| Method chaining | ✓ | ✓ |
| Updates render groups | ✓ | ✓ |

## Related Methods

- `clear()` - Clears all mobjects including the camera frame
- `add()` - Adds mobjects to the scene
- `remove()` - Removes specific mobjects from the scene
- `replace()` - Replaces one mobject with others
