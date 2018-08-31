# Notedown & Scriptedforms

Turn your notebook in interactive markdown
https://github.com/SimonBiggs/scriptedforms  
https://github.com/aaren/notedown

```python
# !pip install scriptedforms
# !pip install notedown
```

### Convert a notebook into markdown  

Flags:
 - stripping all output:
**--strip**
 - stripping all cellmagics: **--nomagic**
 - pre-install packages:
'%matplotlib inline' 'import numpy as np' **--pre**

```python
!notedown notedown.ipynb --to markdown --strip --nomagic > notedown.md
```

### Running markdown notebook - with scriptedforms

```python
!scriptedforms notedown.md
```

### Add Jupyter markdown kernel
add to config:
c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'

## Example

```python
%%js

#### Enter name 

<section-live>

<variable-string>your_name</variable-string>
```

```python
print('Hello {}!'.format(your_name))
```
</section-live>