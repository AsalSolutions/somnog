
from flask_jwt_extended import (verify_jwt_in_request, get_jwt_identity)
from functools import wraps
from api.auth.User import User, Role


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        role = Role.query.filter_by(name="Admin").first()
        # Check if if the current user is Admin
        current_user = User.query.filter_by(
            username=get_jwt_identity()).first()
        # Only then this we can perform admin tasks
        if current_user.role.name == role.name:
            return fn(*args, **kwargs)
        else:
            return {"msg": "You're NOT allowed to perform this action!"}, 403

    return wrapper
