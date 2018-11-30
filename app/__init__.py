from flask import Blueprint

from app.api.v1.views.incidence_view import app, Incidence, Incidences, api_incidence, api_incidences
# from app.api.v1.views.auth_api import register, login, user_username, logout, all_users

app.register_blueprint(api_incidences)
app.register_blueprint(api_incidence)

# app.register_blueprint(register)
# app.register_blueprint(login)
# app.register_blueprint(user_username)
# app.register_blueprint(logout)
# app.register_blueprint(all_users)
