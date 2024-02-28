from pydantic import BaseModel


class ProfileBase(BaseModel):

    city: str | None

class Profile(ProfileBase):

    id: int
    user_id: int


class ProfileUpdate(ProfileBase):
    pass


class ProfileUpdatePartial(ProfileBase):

    city: str | None = None
