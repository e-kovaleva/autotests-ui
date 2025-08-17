from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    'id': 1,
    'username': 'zara',
    'email': 'zara.bond@gmail.com'
}

user = User(**user_data)  # type: ignore
print(user)
print(user.is_active)

invalid_user_data = {
    'id': 'one',
    'username': 'zara',
    'email': 'zara.bond@gmail.com'
}

invalid_user = User(**invalid_user_data)  # type: ignore
print(invalid_user)
print(invalid_user.is_active)
