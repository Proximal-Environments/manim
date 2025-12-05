# clear_all_except - Quick Reference

## Syntax

```python
scene.clear_all_except(*mobjects_to_keep)
```

## Description

Removes all mobjects from the scene except the ones specified in the arguments.

## Parameters

- `*mobjects_to_keep` (Mobject): Variable number of mobject arguments that should remain in the scene

## Returns

- `self` (Scene): Returns the scene instance for method chaining

## Examples

### Keep one object
```python
circle = Circle()
square = Square()
triangle = Triangle()

self.add(circle, square, triangle)
self.clear_all_except(square)  # Only square remains
```

### Keep multiple objects
```python
self.clear_all_except(square, circle)  # Both remain, triangle removed
```

### Clear everything
```python
self.clear_all_except()  # Same as self.clear()
```

### Method chaining
```python
self.clear_all_except(square).add(new_circle)
```

## Available In

- ✅ `Scene` class (`manimlib/scene/scene.py`)
- ✅ `InteractiveScene` class (`manimlib/scene/interactive_scene.py`)

## Differences by Class

| Feature | Scene | InteractiveScene |
|---------|-------|------------------|
| Clears mobjects | ✅ | ✅ |
| Keeps specified objects | ✅ | ✅ |
| Clears selection | ❌ | ✅ |
| Regenerates search set | ❌ | ✅ |

## Important Notes

1. ⚠️ Only mobjects **already in the scene** will be kept
2. ⚠️ Objects not in the scene are ignored (not added)
3. ⚠️ In InteractiveScene, selection is **always cleared**
4. ✅ Duplicate arguments are handled gracefully
5. ✅ Works with grouped objects
6. ✅ Maintains z-index ordering

## Common Use Cases

### 1. Progressive scene building
```python
background = Square()
self.add(background)

# Add temporary objects
temp = Circle()
self.add(temp)
self.wait(1)

# Keep only background
self.clear_all_except(background)
```

### 2. Scene transitions
```python
# Keep title and background, remove all else
self.clear_all_except(title, background)
self.add(new_content)
```

### 3. Cleanup after animation
```python
# Remove everything except result
self.clear_all_except(final_result)
```

## Testing

All tests use `xvfb-run -a` for headless environments:

```bash
# Basic tests
xvfb-run -a python test_clear_all_except.py

# Edge case tests
xvfb-run -a python test_edge_cases.py

# Visual demo
xvfb-run -a python demo_clear_all_except.py
```

## See Also

- `clear()` - Remove all mobjects
- `remove(*mobjects)` - Remove specific mobjects
- `add(*mobjects)` - Add mobjects to scene

## Full Documentation

See `CLEAR_ALL_EXCEPT_DOCUMENTATION.md` for complete documentation.
