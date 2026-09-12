import pytest
from install import extract_prompt_block

def test_extract_prompt_block_simple():
    prompt = """```markdown
You are an agent.
```
"""
    expected = "You are an agent.\n"
    assert extract_prompt_block(prompt) == expected

def test_extract_prompt_block_no_fence():
    prompt = """You are an agent.
Do something.
"""
    expected = "You are an agent.\nDo something.\n"
    assert extract_prompt_block(prompt) == expected

def test_extract_prompt_block_nested_fence():
    prompt = """````markdown
You are an agent.
Output this:
```python
print("hello")
```
````
"""
    expected = """You are an agent.
Output this:
```python
print("hello")
```
"""
    assert extract_prompt_block(prompt) == expected

def test_extract_prompt_block_nested_same_length():
    prompt = """```
Outer start
```
Inner
```
Outer end
```
"""
    expected = """Outer start
```
Inner
```
Outer end\n"""
    assert extract_prompt_block(prompt) == expected
