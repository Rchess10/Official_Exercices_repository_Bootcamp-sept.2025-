# Copilot Instructions for Bootcamp-Sept-2025

## Project Overview
This repository contains Python exercises for learning basic programming concepts. Each file is a standalone script focused on a specific topic (variables, data types, control flow, collections, etc.). There is no complex architecture or inter-file dependencies—each script is independent and can be run directly.

## File Structure
- `1_Exercice.py`, `Exercice.py`, `New_exercice.py`, `lists.py`, `Python_Data_Types.py`: Each file contains simple Python exercises, often with numbered comments and direct print statements.
- No test framework, build system, or external dependencies are present.

## Developer Workflow
- Run any script using `python <filename>.py` from the project root.
- No setup or environment configuration is required beyond having Python installed.
- No custom build or test commands; scripts are intended for direct execution and experimentation.

## Coding Conventions
- Exercises are written in a clear, beginner-friendly style.
- Use descriptive variable names and comments for each step.
- Print statements are used for output and demonstration.
- Each exercise is self-contained; avoid cross-file imports or shared state.
- For control flow, use standard Python if/elif/else and loops.
- For collections, use lists, tuples, sets, and dictionaries as shown in examples.

## Example Patterns
- Assign variables and print their values:
  ```python
  x = 3
  print(x)
  ```
- Use if/else for logic:
  ```python
  if x > 2:
      print("x is greater than 2")
  else:
      print("x is not greater than 2")
  ```
- Loop through a list:
  ```python
  for item in my_list:
      print(item)
  ```
- Use f-strings for formatted output:
  ```python
  name = "Alice"
  print(f"Hello, {name}!")
  ```

## Key Files
- All main logic is in the top-level `.py` files. There are no submodules or packages.
- No README.md or additional documentation is present.

## Guidance for AI Agents
- Focus on direct, readable code for each exercise.
- When adding new exercises, follow the existing style: numbered comments, clear variable names, and print statements.
- Do not introduce unnecessary complexity or external dependencies.
- If a new convention emerges, document it here for future agents.
