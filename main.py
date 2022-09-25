from db_create_and_check import check_db
from excel_import_and_export import export_file, input_file

database_name = 'tests.db'
# Проверка базы данных
check_db(database_name)

# экспорт файла
output_file_name = 'export.xlsx'
export_file(database_name, output_file_name)

#импорт файла
input_file_name = 'import.xlsx'
input_file(database_name, input_file_name)