from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.types import DateTime, Integer, String


class Base(DeclarativeBase):
    pass


class Tickets(Base):
    __tablename__ = "events"


# Information needed to create an event
class EventCreate(BaseModel):
    title: str
    location: str
    start_date: str
    end_date: str
    available_tickets: int


# Information needed to create a ticket
class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: str
