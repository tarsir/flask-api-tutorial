class Customer:
    name = ''
    email_address = ''
    phone_number = ''
    location = None
    is_registered = False
    password = 'ENCRYPTED'

    def __str__(self):
        registered = "Registered" if self.is_registered else "Unregistered"
        location = "({0})".format(self.location) if self.location else ""
        return "{name} ({email}, {phone})".format(
            name=self.name,
            email=self.email_address,
            phone=''.join([self.phone_number[0:3], '-', self.phone_number[3:6], '-', self.phone_number[7:]])
        )