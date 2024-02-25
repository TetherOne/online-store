from pydantic import ConfigDict
from pydantic import BaseModel
from pydantic import EmailStr



class UserBase(BaseModel):

    username: str


class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int