from queries import book_ticket, create_new_event, delete_event, see_all_events


def main():
    create_new_event()
    create_new_event()
    see_all_events()
    book_ticket()
    delete_event(event_id=2)


if __name__ == "__main__":
    main()
