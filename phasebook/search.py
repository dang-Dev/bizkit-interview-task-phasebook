from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!
    
    users = get_users(USERS, args)
    if users:
        return users

    return USERS

def get_users(users, params):
    results = []
    for user in users:
        score = sum(value in str(user.get(param)) for param, value in params.items())
        if score > 0:
            results.append((user, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return [result[0] for result in results]