# -*- encoding: utf-8 -*-
from django import template
from django.contrib import admin
from django.conf import settings

register = template.Library()


'''
templatetag, obtiene la configuración del menú
'''
def get_config_menu():
    return Menu.get_menu(self)
register.filter('get_config_menu')

class Menu(object):
    
    menu_key = 'SOMBRA_MENU'
    
    def __init__(self):
        return None
    
    def get_default_menu(self):
        '''
        Devuelve las opciones por defecto del menú
        '''
        return {
            'MENU': (
                'sites',
                {'label': 'Custom', 'icon':None, 'models': (
                    'auth.group',
                    {'model': 'auth.user', 'label': 'Staff'}
                )},
                ),
                'LIST_PER_PAGE': 20,
            }
        
    def get_menu(self, param=None):
        '''
        Obtiene la configuración de settings.py
        Ex: get_menu()
        Ex: get_menu('MENU')
        return dicc
        '''
        if hasattr(settings, menu_key):
            menu = getattr(settings, menu_key, {})
        else:
            menu = get_default_menu()
        
        if param:
            menu_value = menu.get(param)
            return menu_value
        return menu