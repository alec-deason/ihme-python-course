## Variable Scoping Rules (LEGB)

- **L**, Local — Names assigned in any way within a function, and not declared `global` in that function.

- **E**, Enclosing-function locals — Name in the local scope of any and all statically 
enclosing functions, from inner to outer.

- **G**, Global (module) — Names assigned at the top-level of a module file, 
or by executing a `global` statement in a def within the file.

- **B**, Built-in (Python) — Names preassigned in the built-in names module: 
`open`, `range`, `SyntaxError`, etc.



