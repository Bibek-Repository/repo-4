import sys
import os

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("You are using a virtual environment.")
else:
    print("You are not using a virtual environment.") 

value=os.environ.get('VARIABLE_NAME')
if value is not None:
    print(f"The environment variable is set to: {value}")
else:
    print("The envvironment variable is not set.")  