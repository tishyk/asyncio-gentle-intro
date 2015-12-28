# Gentle introduction to asyncio

A gentle introduction to the concepts behind asyncio primitives, using code examples.

## Intro 

Python 3.4 introduced a new proposed standard for asyncronous programming - `asyncio`.
This module promises to unify the many competing models (...) into a single 
set of primitives for programming in a non-linear fashion. However, I personally found
the documentation too terse and difficult to understand the big picture. There
seemed to be conflicting ways to accomplish the same tasks with many pitfalls and complexities
that are only explained in prose (accessible only if you know the new vocabulary).

The **intended audience** for this guide is developers who are already comfortable with Python but 
are completely new to asyncio (or new to asynchronous programming in general). The
concepts will be explained with code examples which demonstrate practical 
design patterns that you can use in your own projects.


## Table of contents

1. The [difference between asyncronous and syncronous programming](01_sync_vs_async_example/) - Baking a cake as an analogy for why we need asyncronous programming. *We can be mixing ingredients while our oven preheats*. Asyncio and syncronous code examples compared.
