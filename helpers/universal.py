from plexapi.myplex import MyPlexUser
from models.jellyfin.user import JellyfinUser

from .settings import get_setting
from .plex import get_plex_users, get_plex_user, sync_plex_users
from .jellyfin import get_jellyfin_users, get_jellyfin_user, sync_jellyfin_users

# ANCHOR - Get Server Type
def _get_server_type() -> str:
    """Get the server type from the settings

    return: str - [plex, jellyfin]
    """

    # Get the server type from the settings
    server_type = get_setting("server_type")

    # Raise an error if the server type is not set
    if server_type is None:
        raise ValueError("Server type not set")

    # Return the server type
    return server_type


# ANCHOR - Global Get Users
def global_get_users() -> dict[MyPlexUser or JellyfinUser]:
    """Get all users from the media server

    :return: A list of users
    """

    # Get the server type and set the users variable
    server_type = _get_server_type()
    users = None

    # Get the users from the media server
    if server_type == "plex":
        users = get_plex_users()
    elif server_type == "jellyfin":
        users = get_jellyfin_users()

    # Raise an error if the users are None
    if users is None:
        raise ValueError("Unable to get users")

    # Return the users
    return users


# ANCHOR - Global Get User
def global_get_user(user_id: str) -> MyPlexUser or JellyfinUser:
    """Get a user from the media server
    :param user_id: The id of the user
    :type user_id: str

    :return: A user
    """

    # Get the server type and set the user variable
    server_type = _get_server_type()
    user = None

    # Get the user from the media server
    if server_type == "plex":
        user = get_plex_user(user_id)
    elif server_type == "jellyfin":
        user = get_jellyfin_user(user_id)

    # Raise an error if the user is None
    if user is None:
        raise ValueError("Unable to get user")

    # Return the user
    return user


# ANCHOR - Global Sync Users
def global_sync_users() -> None:
    """Sync users from the media server to the database

    :return: None
    """

    # Get the server type
    server_type = _get_server_type()
    users = None

    # Sync users from the media server to the database
    if server_type == "plex":
        users = sync_plex_users()
    elif server_type == "jellyfin":
        users = sync_jellyfin_users()

    # Return the users
    return users

