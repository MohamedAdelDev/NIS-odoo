{
    'name': 'Bus Notion',
    'version': '1.0',
    'category': 'Hidden',
    'website': 'www.notion-edu.com',
    'description': "Instant Messaging Bus allow you to send messages to users, in live.",
    'depends': ['base', 'contacts', 'hr', 'contact_edit'],
    'data': [
        'security/ir.model.access.csv',
        'views/bus_info.xml',
        'views/bus_maintenance.xml',
        'views/drivers_information.xml',
    ],
    'installable': True,
    'application': True,


}