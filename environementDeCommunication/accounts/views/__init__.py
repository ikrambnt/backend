from .signup import SignUpView
from .signin import SignInView
from .signout import signout
from .ChangePassword import PasswordsChangeView, MyPasswordResetView
from .profile import profile , update_user , update_user_admin
from .UsersCRUD import list_users
__all__ = [SignUpView, SignInView, signout,PasswordsChangeView, profile, update_user, MyPasswordResetView , update_user_admin, list_users]
