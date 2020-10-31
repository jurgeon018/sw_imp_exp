from django import apps 


class ImportExportConfig(apps.AppConfig):
    name = 'sw_imp_exp'
    verbose_name = 'Імпорт/Експорт'

default_app_config = 'sw_imp_exp.ImportExportConfig'


