from sqlmodel import Session

from app.database import engine, create_db_and_tables
from app.models import PhoneBook


def seed_database():
    create_db_and_tables()
    
    sample_data = [
        {'name': 'Juan Dela Cruz', 'phone_number': '09171234567'},
        {'name': 'Maria Santos', 'phone_number': '09181234567'},
        {'name': 'Pedro Garcia', 'phone_number': '09191234567'},
        {'name': 'Ana Reyes', 'phone_number': '09201234567'},
        {'name': 'Jose Lopez', 'phone_number': '09211234567'},
        {'name': 'Sofia Martinez', 'phone_number': '09221234567'},
        {'name': 'Luis Rodriguez', 'phone_number': '09231234567'},
        {'name': 'Carmen Torres', 'phone_number': '09241234567'},
        {'name': 'Miguel Fernandez', 'phone_number': '09251234567'},
        {'name': 'Isabella Gonzales', 'phone_number': '09261234567'}
    ]

    with Session(engine) as session:
        # Clear existing data
        session.query(PhoneBook).delete()
        
        # Add new data
        for data in sample_data:
            entry = PhoneBook(**data)
            session.add(entry)
        
        session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database() 