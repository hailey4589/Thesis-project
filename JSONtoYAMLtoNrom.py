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
        image_width = image.get('width', 1)  # Default width to 1 to avoid division by zero
        image_height = image.get('height', 1)  # Default height to 1 to avoid division by zero
        
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
                        # Normalize bounding box coordinates
                        normalized_bbox = [
                            bbox[0] / image_width,  # Normalize x-coordinate
                            bbox[1] / image_height,  # Normalize y-coordinate
                            bbox[2] / image_width,  # Normalize width
                            bbox[3] / image_height  # Normalize height
                        ]
                        bbox_str = ' '.join(map(str, normalized_bbox))
                        txt_file.write(f"{category_id} {bbox_str}\n")
# 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
# Example usage:
yaml_file_path = '/home/avl/Thesis-project/y.yaml'
output_folder = '/home/avl/Thesis-project/output_folder'  # Change this to the desired output folder
load_yaml_file(yaml_file_path, output_folder)
