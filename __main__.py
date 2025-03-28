from zodable_idschema import Id
from pydantic import BaseModel

# Example of a model with an Id field (int or UUID)

class User(BaseModel):
    id: Id
    name: str

if __name__ == "__main__":
    user1 = User(id=1, name="John")
    print(user1, user1.model_dump_json())
    user2 = User(id="e82cd85b-2657-48c0-b3e2-780ddb7976e8", name="John")
    print(user2, user2.model_dump_json())

    json_data3 = '{"id": 123, "name": "John"}'
    json_data4 = '{"id": "550e8400-e29b-41d4-a716-446655440000", "name": "John"}'
    user3 = User.model_validate_json(json_data3)
    print(user3, user3.model_dump_json())
    user4 = User.model_validate_json(json_data4)
    print(user4, user4.model_dump_json())
