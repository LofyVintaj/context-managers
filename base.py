# оператор with - важная сущность готорая гарантирует выполнение кода

from example_of_a_context_manager_for_working_with_a_database import DatabaseConnection

with DatabaseConnection("my_db.sqlite") as conn:
    # действия с базой данных
    pass

# соединение с базой данных автоматически закрывается после выхода из блока