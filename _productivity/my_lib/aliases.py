# Generic aliases
%alias show echo
%alias mop echo Monty Python
%alias tree pwd && tree . %s
%alias find find ~ | grep -i %s
%alias find.. find .. | grep -i %s
%alias find. find . | grep -i %s
%alias findx find ~ | grep -Ei %s
%alias read cat %s
%alias aug ls -al | grep Aug | grep -v 2018

# !brew install cowsay
%alias say cowsay
%alias_magic t timeit

# Create directory with packages for importing
%alias make_lib mkdir my_lib && touch my_lib/__init__.py  
%alias add_lib cp %s my_lib/my_module.py
%alias to_lib mkdir my_lib && touch my_lib/__init__.py && cp %s my_lib/my_module.py