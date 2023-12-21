import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        from_attributes = True
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
