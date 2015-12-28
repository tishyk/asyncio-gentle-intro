Syncronous

```
$ time python test_sync.py
preheat:: temp is now 200
preheat:: temp is now 300
preheat:: temp is now 400
mix_ingredients:: mixing things 0
mix_ingredients:: mixing things 1
mix_ingredients:: mixing things 2
bake_cake:: baking for 0 minutes
bake_cake:: baking for 4 minutes
bake_cake:: baking for 8 minutes
bake_cake:: baking for 12 minutes
make_frosting:: making frosting for 0 minutes
make_frosting:: making frosting for 4 minutes
make_frosting:: making frosting for 8 minutes
apply_frosting:: frosting for 0 minutes
apply_frosting:: frosting for 2 minutes

real	0m1.602s
user	0m0.024s
sys	0m0.009s
```

Asyncronous version
```
$ time python test_async.py
preheat:: temp is now 200
mix_ingredients:: mixing things 0
preheat:: temp is now 300
mix_ingredients:: mixing things 1
preheat:: temp is now 400
mix_ingredients:: mixing things 2
bake_cake:: baking for 0 minutes
make_frosting:: making frosting for 0 minutes
bake_cake:: baking for 4 minutes
make_frosting:: making frosting for 4 minutes
bake_cake:: baking for 8 minutes
make_frosting:: making frosting for 8 minutes
bake_cake:: baking for 12 minutes
apply_frosting:: frosting for 0 minutes
apply_frosting:: frosting for 2 minutes

real	0m1.053s
user	0m0.081s
sys	0m0.019s
```
