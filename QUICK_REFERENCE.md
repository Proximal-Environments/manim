# clear_all_except() - Quick Reference Guide

## Syntax
```python
scene.clear_all_except(*mobjects_to_keep)
```

## Parameters
- `*mobjects_to_keep`: Variable number of Mobject instances to keep in the scene

## Returns
- `Scene` (self) - for method chaining

## Usage

### Clear everything except one object
```python
scene.clear_all_except(my_circle)
```

### Clear everything except multiple objects
```python
scene.clear_all_except(title, subtitle, circle)
```

### Clear everything (empty scene)
```python
scene.clear_all_except()
```

### Method chaining
```python
scene.clear_all_except(title).add(new_content).wait(1)
```

### Using with unpacking
```python
objects_to_keep = [obj1, obj2, obj3]
scene.clear_all_except(*objects_to_keep)
```

## What Gets Preserved
- ✅ Camera frame (automatic)
- ✅ Objects specified in arguments
- ❌ Everything else is removed

## Common Use Cases

### 1. Slideshow with Persistent Title
```python
title = Text("My Presentation").to_edge(UP)
self.add(title)

# Slide 1
content1 = Text("Content 1")
self.add(content1)
self.wait()

# Slide 2
self.clear_all_except(title)  # Title stays, content1 removed
content2 = Text("Content 2")
self.add(content2)
self.wait()
```

### 2. Coordinate System with Changing Points
```python
# Setup axes
axes = create_axes()
self.add(axes)

# Show different points
for point_data in points:
    self.clear_all_except(axes)  # Keep axes
    point = create_point(point_data)
    self.add(point)
    self.wait()
```

### 3. Interactive Scene Cleanup
```python
# In InteractiveScene
self.clear_all_except(persistent_ui)
# selection_search_set is automatically updated
```

## Key Differences from clear()

| Feature | clear() | clear_all_except() |
|---------|---------|-------------------|
| Removes all objects | Yes | Yes |
| Preserves camera frame | No | Yes (automatic) |
| Can keep specific objects | No | Yes |
| Updates selection_search_set (InteractiveScene) | No | Yes |

## Tips

1. **Always preserved**: Camera frame is always kept automatically
2. **Order maintained**: Objects maintain their z-index ordering
3. **Safe to use**: Won't error if object not in scene
4. **Chainable**: Returns self for method chaining
5. **Interactive-friendly**: Works seamlessly with InteractiveScene

## Examples in This Repository

- `test_clear_all_except_simple.py` - Complete test suite
- `example_usage.py` - Practical usage examples
- `demo_clear_all_except.py` - Visual demonstrations

## Testing

Run tests with:
```bash
xvfb-run -a python test_clear_all_except_simple.py
```

Run examples with:
```bash
xvfb-run -a python example_usage.py
```

## See Also

- `CLEAR_ALL_EXCEPT_DOCUMENTATION.md` - Full documentation
- `SUMMARY.md` - Implementation details
