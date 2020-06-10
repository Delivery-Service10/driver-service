from models import Driver
import uuid


def populate_driver(data, hashed_password):
    new_driver = Driver(public_id=str(uuid.uuid4()),
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        password=hashed_password,
                        is_verified=False,
                        addressLine1=data['addressLine1'],
                        addressLine2=data['addressLine2'],
                        city=data['city'],
                        district=data['district'],
                        country=data['country']
                        )
    return new_driver


def allocate_data(driver):
    driver_data = {'public_id': driver.public_id,
                   'email': driver.email,
                   'first_name': driver.first_name,
                   'last_name': driver.last_name,
                   'is_verified': driver.is_verified,
                   'addressLine1': driver.addressLine1,
                   'addressLine2': driver.addressLine2,
                   'city': driver.city,
                   'district': driver.district,
                   'country': driver.country
                   }
    return driver_data


def combine_results(drivers):
    output = []
    for driver in drivers:
        driver_data = allocate_data(driver)
        output.append(driver_data)
    return output
