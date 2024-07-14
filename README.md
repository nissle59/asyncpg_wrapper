# AsyncPG Wrapper
## _Легкая в обращении обёртка над AsyncPG_
### _версия 0.1.0_

Wrapper принимает и возращает только объекты типа __dict()__ и __List[dict]__

### Установка
```shell
pip install asyncpg-wrapper
```
### Инициализация в коде
```python
from asyncpg_wrapper import AsyncDB

dsn = "postgresql://username:password@host:port/dbname"
db = AsyncDB(dsn)
```

### Примеры операций:

```python
new_record = await db.insert('users', {'first_name': 'John', 'last_name': 'Doe'})
print(new_record)
```

```python
l = [{'first_name': f'John{i}', 'last_name': f'Doe{i}'} for i in range(0, 1000)]
new_records = await db.insertmany('users', l)
print(new_records)
```

```python
updated_record = await db.update('users', "id=1", {'first_name': 'Jane'})
print(updated_record)
```

```python
deleted_records = await db.delete('users', "first_name='Jane'")
print(deleted_records)
```

```python
deleted_records = await db.delete('users')
print(deleted_records)
```

```python
selected_records = await db.select('users', 'id=1')
print(selected_records)
```

```python
selected_records = await db.select('users')
print(selected_records)
```
