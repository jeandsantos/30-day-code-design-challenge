from models import Event
from sqlalchemy import select
from sqlalchemy.orm import Session


def query_get_all_events(session: Session):
    query = select(
        Event.id,
        Event.title,
        Event.location,
        Event.start_date,
        Event.end_date,
        Event.available_tickets,
    )

    for event in session.get(query):
        print(type(event))
        print(event)
