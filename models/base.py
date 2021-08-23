import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Credentials:
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY')
    aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')

## Example model for a basic user class
#class UserModel(Model):
#    """
#    A DynamoDB User
#    """
#    class Meta(Credentials):
#        table_name = 'dynamodb-user'
#        region = 'us-west-1'
#    email = UnicodeAttribute(null=True)
#    first_name = UnicodeAttribute(range_key=True)
#    last_name = UnicodeAttribute(hash_key=True)

## Create the table with
# UserModel.create_table(read_capacity_units=1, write_capacity_units=1)

## Create a new user
#user = UserModel("John", "Denver")
#user.email = "djohn@company.org"
#user.save()

## Query for the user
#for user in UserModel.query("John", UserModel.first_name.startswith("J")):
#    print(user.first_name)

