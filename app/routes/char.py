from flask import Blueprint, render_template,redirect,url_for,flash
from app.dataBase import DabataseConnection
import requests

personaje_router = Blueprint('personaje_router', __name__)
db = DabataseConnection(5)