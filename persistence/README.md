In this diagram we show how both of this modules work together.
'IPersistenceManager' defines the methods for CRUD operations.
'DataManager' implements these methods and uses an internal dictionary to store.

+-----------------------+              +-----------------------+
| IPersistenceManager   |<-------------|  DataManager          |
|-----------------------| Implements   |-----------------------|
| + save(entity)        | Interface    | - storage: dict       |
| + get(entity_id, ...) | ------------>| + save(entity)        |
| + update(entity)      |              | + get(entity_id, ...) |
| + delete(entity_id,...)|              | + update(entity)      |
+-----------------------+              | + delete(entity_id,...)|
                                       +-----------------------+
