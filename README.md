# Gentle introduction to asyncio

A gentle introduction to the concepts behind asyncio primitives, using code examples.

**WORK IN PROGRESS: I'm a beginner at asyncio so this is my attempt to document the learning process. I'm not an expert - please speak up if you see docs or code that could be done better.**

## Intro 

Python 3.4 introduced **`asyncio`** a new proposed standard for asyncronous programming.
This module promises to unify the many competing models (...) into a single 
set of primitives for programming in a non-linear fashion.

However, I personally found the documentation too terse to understand the big picture. There
seemed to be conflicting ways to accomplish the same tasks. There are many pitfalls and complexities
that are not immediately obvious unless you're familiar with the vocabulary.

This guide is intended for developers who are already comfortable with Python but 
are completely new to asyncio (or new to asynchronous programming in general). The
concepts will be explained with code examples which demonstrate practical 
design patterns that you can use in your own projects.

This code will use Python 3.4 but includes sections for how to port to 3.5+ and back to 2.6.

## Table of contents

1. The [difference between asyncronous and syncronous programming](01_sync_vs_async_example/) - Baking a cake as an analogy for why we need asyncronous programming. *We can be mixing ingredients while our oven preheats*. Asyncio and syncronous code examples compared.
1. Core concepts: Defining the main players
    - The `yield from` keyword, avoiding callbacks
    - The event loop
    - Tasks, coroutines and Futures
    - Transports and Protocols
1. Guide
    1. Calling blocking code in another thread with `run_in_executor`
    1. Running the loop: `run_until_complete` versus `forever`, in main only
    1. Subprocesses and UNIX Pipes
    1. Unix Signals
    1. open_connection for Readers and Writers
    1. Creating servers
    1. Handling Exceptions
1. Portability
    1. Coming from Other techniques like gevent, tornado, twisted, JS callbacks, etc
    1. Porting to Python 2.6 with `Trollius`
    1. Porting to Python 3.5 with `async` keywords
1. Pragmatic lessons
    - Things the API allows but are not encourages
        - loop.stop
        - run loop in main only
        - multiple event loops in threads
        - setting event loop policy
        - use gather instead of wait unless you need a timeout
        - queues as a last resort
    - Things that are generally too low level for daily use
