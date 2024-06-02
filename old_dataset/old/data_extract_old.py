class DataExtract:
    
    def __init__(self):
        pass
    
    def extract_data_ids(self, data_file):
        with open(data_file, 'r') as file:
            lines = file.readlines()
        
        data_dict = {}
        
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            
            data_id = parts[2]
            data_dict[data_id] = None
        return data_dict


    def save_dict(self, output_file, data_dict):
        with open(output_file, 'w') as file:
            file.write("{\n")
            for key in data_dict:
                file.write(f"'{key}',\n")
            file.write("}\n")
            
    
    # script_rotulador.py
    def label_data(self, input_data, ids_benignos, attack_type='maligno'):
        with open(input_data, 'r') as file:
            lines = file.readlines()
        
        labeled_data = []
        
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
    
            id_data = parts[2] # seleciona a parte do id e campo de dados
            # print(id_data)
            if id_data in ids_benignos:
                label = 'benign'
            else:
                label = attack_type
            labeled_data.append((line.strip(), label))
        return labeled_data


    def save_labeled_data(self, output_file, labeled_data):
        with open(output_file, 'w') as file:
            for line, label in labeled_data:
                file.write(f"{line} {label}\n")


    def read_file_to_variable(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read().strip()
        return content
    