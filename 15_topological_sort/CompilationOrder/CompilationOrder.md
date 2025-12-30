# Compilation Order

## Statement

There are a total of n classes labeled with the English alphabet (A, B, C, and so on). Some classes are dependent on other classes for compilation. For example, if class B extends class A, then B has a dependency on A. Therefore, A must be compiled before B.

Given a list of the dependency pairs, find the order in which the classes should be compiled.

## Constraints

- Class name should be an uppercase character.
- 0 ≤ dependencies.length ≤ 676
- dependencies[i].length = 2
- All dependency pairs should be unique.

