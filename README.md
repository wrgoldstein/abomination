This is

1. the basic result of `dbt init`, with local postgres as the backend
2. the addition of a python model
3. the hackery involved to run the dbt models outside dbt
4. including python in containers

These models

```
models
└── example
    ├── my_first_dbt_model.sql
    ├── my_second_dbt_model.sql
    ├── python_model.py         <-- ooh
    └── schema.yml
macros
└── my_py_func.py
```

can be run with 

```
python wirtl run
```

but not 

```
dbt run
```

👺
