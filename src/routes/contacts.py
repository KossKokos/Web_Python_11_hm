from typing import List

from pydantic import EmailStr
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ContactResponce, ContactFirstNameUpdate, ContactLastNameUpdate, ContactEmailUpdate, ContactBirthdateUpdate, ContactPhoneUpdate, ContactDescriptionUpdate
from src.repository import contacts as repository_contacts

router = APIRouter(prefix='/contacts', tags=["contacts"])


# using list to return list of dictionaries with tables objects
# Session = Depends(get_db) for getting database 
@router.get('/', response_model=List[ContactResponce])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, db)
    return contacts


@router.get('/birthdays', response_model=List[ContactResponce])
async def read_birthdays(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_birthdays(db)
    return contacts


# adding parametr {contact_id} to path and finding a contact using that id
@router.get('/{contact_id}', response_model=ContactResponce)
async def read_contact_by_id(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    return contact


@router.get('/firstname/{contact_first_name}', response_model=ContactResponce)
async def read_contact_by_firstname(contact_first_name : str = Path(min_length=3, max_length=50), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_firstname(contact_first_name, db)
    return contact


@router.get('/lastname/{contact_last_name}', response_model=ContactResponce)
async def read_contact_by_lastname(contact_last_name: str = Path(min_length=3, max_length=60), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_lastname(contact_last_name, db)
    return contact


@router.get('/email/{contact_email}', response_model=ContactResponce)
async def read_contact_by_email(contact_email: EmailStr, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(contact_email, db)
    return contact


# adding a form ContactModel so user can create new contact by filling this form
@router.post('/', response_model=ContactResponce)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contacts.add_contact(body, db)
    return contact


# adding a form ContactFirstName so user can update old name by including new one in this form
@router.patch('/first_name/{contact_id}', response_model=ContactResponce)
async def update_contact_firstname(body: ContactFirstNameUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_firstname(body, contact_id, db)
    return contact


@router.patch('/last_name/{contact_id}', response_model=ContactResponce)
async def update_contact_lastname(body: ContactLastNameUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_lastname(body, contact_id, db)
    return contact


@router.patch('/email/{contact_id}', response_model=ContactResponce)
async def update_contact_email(body: ContactEmailUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_email(body, contact_id, db)
    return contact


@router.patch('/phone/{contact_id}', response_model=ContactResponce)
async def update_contact_phone(body: ContactPhoneUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_phone(body, contact_id, db)
    return contact


@router.patch('/birthdate/{contact_id}', response_model=ContactResponce)
async def update_contact_birthdate(body: ContactBirthdateUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_birthdate(body, contact_id, db)
    return contact


@router.patch('/description/{contact_id}', response_model=ContactResponce)
async def update_contact_description(body: ContactDescriptionUpdate, contact_id: int = Path(ge=1), 
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact_description(body, contact_id, db)
    return contact


# delete contact by usong contact_id
@router.delete('/{contact_id}', response_model=ContactResponce)
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    return contact