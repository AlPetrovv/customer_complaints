from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(self):
        return self.__name__.lower()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.__name__}#{self.id}'