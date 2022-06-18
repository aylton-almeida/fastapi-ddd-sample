from __future__ import annotations

from sqlalchemy import Column, DateTime
from sqlalchemy.sql.elements import BinaryExpression

from src.utils.date_utils import get_current_datetime


class BaseEntity:

    # TODO: figure out how to make this work
    session = None
    query: any  # ? Added here only for pylint

    created_at = Column(DateTime, default=get_current_datetime, nullable=False)
    updated_at = Column(
        DateTime,
        default=get_current_datetime,
        onupdate=get_current_datetime,
        nullable=False,
    )

    def __init__(self, _session=None) -> None:
        pass
        # self.session = _session or db.session

    def save(self, commit=True):
        """Save model"""

        self.session.add(self)
        self.session.flush()

        if commit:
            self.session.commit()

    def update(self, data: dict, commit=True):
        """Update model with given data

        Args:
            data (dict): Data to update model with
        """

        for key, item in data.items():
            setattr(self, key, item)
        self.session.flush()

        if commit:
            self.session.commit()

    def delete(self, commit=True):
        """Delete model from db"""

        self.session.delete(self)

        if commit:
            self.session.commit()

    @staticmethod
    def commit():
        """Commits current transaction"""

        BaseEntity.session.commit()

    @classmethod
    def get_one_filtered(cls, filters: list[BinaryExpression]):
        """Gets one of given model given filters"""

        return cls.query.filter(*filters).first()

    @classmethod
    def get_many_filtered(cls, filters: list[BinaryExpression]):
        """Gets many of given model given filters"""

        return cls.query.filter(*filters).all()
