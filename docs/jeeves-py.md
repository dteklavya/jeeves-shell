---
title: jeeves.py
hello: examples/hello.py
hide:
  - toc
---

# :simple-python: jeeves.py

{# todo: draw a picture where Makefile is crossed away and jeeves.py is shown instead #}

While GNU make goals are specified in a file named `Makefile`, Jeeves looks for commands in a file named `jeeves.py` in current directory.

## Commands

Every Python function in `jeeves.py` is converted into a command.

* Docstrings are used as command documentation,
* Command arguments are configured by arguments of respective functions (and their type hints!)

Let's recall the Hello World script we [:arrow_backward: had referenced before](../#get-started):

{{ code(page.meta.hello, language='python', title='jeeves.py') }}

Check out how automated documentation works:

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

Or, for the given command:

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', '--help']) }}
