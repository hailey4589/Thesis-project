import yaml
import os

def load_yaml_file(yaml_file_path, output_folder):
    with open(yaml_file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    images = data.get('images', [])
    annotations = data.get('annotations', [])
    
    for image in images:
        image_id = image.get('id')
        file_name = image.get('file_name')
        if image_id is not None and file_name is not None:
            print(f"Processing image: {file_name}")
            
            # Find corresponding annotations for the current image_id
            image_annotations = [annotation for annotation in annotations if annotation.get('image_id') == image_id]
            print(f"Annotations for image {image_id}: {image_annotations}")
            
            # Create a folder to store text files if it doesn't exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Write annotations to a text file with the name of the image
            txt_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.txt')
            with open(txt_file_path, 'w') as txt_file:
                for annotation in image_annotations:
                    category_id = annotation.get('category_id')
                    bbox = annotation.get('bbox')
                    print(f"Category ID: {category_id}, Bbox: {bbox}")
                    if category_id is not None and bbox is not None:
                        bbox_str = ' '.join(map(str, bbox))
                        txt_file.write(f"{category_id} {bbox_str}\n")
                        
            
# Example usage:
yaml_file_path = '/home/avl/Thesis-project/yaml.yaml'
output_folder = '/home/avl/Thesis-project/output_folder'  # Change this to the desired output folder
load_yaml_file(yaml_file_path, output_folder)
