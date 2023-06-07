import csv


def save_instances_to_csv(instances):
    # Dynamically detects object's type
    class_name = instances[0].__name__

    file_path = f"csv/{class_name}Data.csv"
    # Dynamically get field names from object
    field_names = list(vars(instances[0]).keys())

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for instance in instances:
            writer.writerow(vars(instance))


def load_instances_from_csv(class_type):
    file_path = f"csv/{class_type.__name__}Data.csv"

    instances = []

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Creates an instance of the given class
            instance = class_type(**row)
            for key, value in row.items():
                setattr(instance, key, value)
            instances.append(instance)

    return instances
